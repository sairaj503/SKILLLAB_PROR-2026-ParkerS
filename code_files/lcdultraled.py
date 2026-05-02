import RPi.GPIO as GPIO
from RPLCD.i2c import CharLCD
from time import sleep, time
from datetime import datetime
import cv2
import numpy as np
from picamera2 import Picamera2
import threading
import os

# ─── Model Paths ─────────────────────────────────────────────────────────────
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
PROTOTXT   = os.path.join(BASE_DIR, "MobileNetSSD_deploy.prototxt")
CAFFEMODEL = os.path.join(BASE_DIR, "MobileNetSSD_deploy.caffemodel")

# Full MobileNet SSD class list (required by model — do not remove)
CLASSES = [
    "background", "aeroplane", "bicycle", "bird", "boat",
    "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
    "dog", "horse", "motorbike", "person", "pottedplant",
    "sheep", "sofa", "train", "tvmonitor"
]

# Only car and person trigger OCCUPIED
DETECT_CLASSES       = {"car", "person"}
CONFIDENCE_THRESHOLD = 0.15
TRIGGER_DISTANCE     = 50    # cm — ultrasonic threshold to start detection

print("Loading MobileNet SSD model...")
net = cv2.dnn.readNetFromCaffe(PROTOTXT, CAFFEMODEL)
print("Model loaded OK.")

# ─── LCD ─────────────────────────────────────────────────────────────────────
lcd = CharLCD('PCF8574', 0x27, port=1, cols=16, rows=2)

# ─── Camera ──────────────────────────────────────────────────────────────────
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(
    main={"size": (640, 480), "format": "BGR888"}
))
picam2.start()
sleep(2)

# ─── GPIO Pins ───────────────────────────────────────────────────────────────
TRIG      = 17
ECHO      = 27
GREEN_LED = 22
RED_LED   = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG,      GPIO.OUT)
GPIO.setup(ECHO,      GPIO.IN)
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED,   GPIO.OUT)

# ─── Shared State ────────────────────────────────────────────────────────────
distance      = 999.0
dist_lock     = threading.Lock()
frame_lock    = threading.Lock()
result_lock   = threading.Lock()
running       = True
detect_frame  = None
detect_result = {"is_car": False, "label": None, "conf": 0.0, "boxes": []}

# ─── Thread 1: Distance Sensing ──────────────────────────────────────────────
def distance_thread():
    global distance
    while running:
        try:
            GPIO.output(TRIG, True)
            sleep(0.00001)
            GPIO.output(TRIG, False)

            timeout     = time() + 0.04
            pulse_start = time()
            while GPIO.input(ECHO) == 0:
                pulse_start = time()
                if time() > timeout: break

            timeout   = time() + 0.04
            pulse_end = time()
            while GPIO.input(ECHO) == 1:
                pulse_end = time()
                if time() > timeout: break

            d = round((pulse_end - pulse_start) * 17150, 2)
            if 2 < d < 400:
                with dist_lock:
                    distance = d
        except Exception as e:
            print(f"Distance error: {e}")
        sleep(0.06)   # ~15 readings/sec

# ─── Thread 2: Object Detection ──────────────────────────────────────────────
def detection_thread():
    while running:
        with dist_lock:
            d = distance

        if d <= TRIGGER_DISTANCE:
            with frame_lock:
                f = detect_frame.copy() if detect_frame is not None else None

            if f is not None:
                h, w = f.shape[:2]
                blob = cv2.dnn.blobFromImage(
                    cv2.resize(f, (300, 300)), 0.007843, (300, 300), 127.5
                )
                net.setInput(blob)
                detections = net.forward()

                boxes      = []
                is_car     = False
                best_label = None
                best_conf  = 0.0

                print(f"\n--- Detection scan (dist={d}cm) ---")
                for i in range(detections.shape[2]):
                    conf = float(detections[0, 0, i, 2])
                    if conf < 0.1:
                        continue
                    idx   = int(detections[0, 0, i, 1])
                    label = CLASSES[idx]
                    print(f"  {label}: {conf:.2f}")

                    if conf >= CONFIDENCE_THRESHOLD and label in DETECT_CLASSES:
                        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                        boxes.append((label, conf, box.astype("int")))
                        if conf > best_conf:
                            best_conf  = conf
                            best_label = label
                        is_car = True

                print(f"  → is_car={is_car}, best={best_label}({best_conf:.2f})")

                with result_lock:
                    detect_result.update({
                        "is_car": is_car,
                        "label":  best_label,
                        "conf":   best_conf,
                        "boxes":  boxes
                    })
        else:
            with result_lock:
                detect_result.update({
                    "is_car": False, "label": None,
                    "conf": 0.0, "boxes": []
                })
        sleep(0.5)   # detection runs 2x/sec, not every frame

# ─── Start Threads ────────────────────────────────────────────────────────────
threading.Thread(target=distance_thread,  daemon=True).start()
threading.Thread(target=detection_thread, daemon=True).start()

# ─── LED Control ─────────────────────────────────────────────────────────────
def set_leds(d):
    if d <= TRIGGER_DISTANCE:
        GPIO.output(RED_LED,   True)
        GPIO.output(GREEN_LED, False)
    else:
        GPIO.output(GREEN_LED, True)
        GPIO.output(RED_LED,   False)

# ─── LCD Update (only redraws when value changes) ────────────────────────────
lcd_last = ""
def update_lcd(status, d):
    global lcd_last
    key = f"{status}|{d}"
    if key == lcd_last:
        return
    lcd_last = key
    lcd.home()
    if status == "OCCUPIED":
        lcd.write_string('Slot 1:OCCUPIED ')
    else:
        lcd.write_string('Slot 1:EMPTY    ')
    lcd.crlf()
    lcd.write_string(f'Dist:{d} cm      ')

# ─── Camera Overlay ──────────────────────────────────────────────────────────
def draw_overlay(frame, d, status, boxes, label, conf):
    h, w = frame.shape[:2]

    # Bounding boxes from detection
    for (lbl, c, box) in boxes:
        x1, y1, x2, y2 = box
        color = (0, 255, 0) if lbl == "car" else (0, 165, 255)
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"{lbl}: {c:.2f}",
                    (x1, max(y1 - 8, 10)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)

    # Bottom status bar
    bar_color = (0, 0, 150) if status == "OCCUPIED" else (0, 80, 0)
    overlay = frame.copy()
    cv2.rectangle(overlay, (0, h - 55), (w, h), bar_color, -1)
    cv2.addWeighted(overlay, 0.55, frame, 0.45, 0, frame)

    txt_color = (0, 0, 255) if status == "OCCUPIED" else (0, 255, 0)
    det_str   = f"[{label}: {conf:.2f}]" if label else "[no detection]"
    cv2.putText(frame,
                f"Dist: {d}cm  |  Slot 1: {status}  {det_str}",
                (10, h - 18), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, txt_color, 2, cv2.LINE_AA)

# ─── Preview Window ───────────────────────────────────────────────────────────
cv2.namedWindow("Smart Parking", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Smart Parking", cv2.WND_PROP_FULLSCREEN,
                       cv2.WINDOW_FULLSCREEN)

# ─── Startup ─────────────────────────────────────────────────────────────────
lcd.write_string('Distance Meter  ')
sleep(2)
lcd.clear()
lcd.write_string('Smart Parking   ')
lcd.crlf()
lcd.write_string('Initializing... ')
sleep(2)
lcd.clear()
update_lcd("EMPTY", 0)

prev_car         = False
saved_this_event = False
print(f"System running. Trigger distance: {TRIGGER_DISTANCE}cm. Press Q or Ctrl+C to quit.")

try:
    while True:
        # Grab frame at full camera speed — no blocking here
        frame = picam2.capture_array()

        with frame_lock:
            detect_frame = frame.copy()

        with dist_lock:
            d = distance
        with result_lock:
            is_car = detect_result["is_car"]
            boxes  = list(detect_result["boxes"])
            label  = detect_result["label"]
            conf   = detect_result["conf"]

        # LEDs
        set_leds(d)

        # Slot status logic
        if d <= TRIGGER_DISTANCE and is_car:
            status = "OCCUPIED"
        else:
            status = "EMPTY"

        # Reset save flag when object moves away
        if d > TRIGGER_DISTANCE:
            saved_this_event = False

        # Save image once per car detection event
        if is_car and not prev_car and not saved_this_event:
            fname = datetime.now().strftime("car_%Y%m%d_%H%M%S.jpg")
            cv2.imwrite(fname, frame)
            print(f"Image saved: {fname}")
            saved_this_event = True

        prev_car = is_car

        # Update LCD, overlay, and show frame
        update_lcd(status, d)
        draw_overlay(frame, d, status, boxes, label, conf)
        cv2.imshow("Smart Parking", frame)

        print(f"Dist: {d}cm | Slot 1: {status} | LED: {'RED' if d <= TRIGGER_DISTANCE else 'GREEN'}")

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    pass

finally:
    running = False
    lcd.clear()
    lcd.write_string('Goodbye!        ')
    sleep(1)
    lcd.close(clear=True)
    GPIO.output(RED_LED,   False)
    GPIO.output(GREEN_LED, False)
    GPIO.cleanup()
    picam2.stop()
    cv2.destroyAllWindows()
    print("Shutdown complete.")