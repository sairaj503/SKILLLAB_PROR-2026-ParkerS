import cv2
import time
import RPi.GPIO as GPIO
import numpy as np

# --- 1. SETUP ULTRASONIC SENSOR ---
TRIG_PIN = 23
ECHO_PIN = 24
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# --- 2. SETUP THE AI BRAIN ---
print("Loading Caffe Model...")
prototxt = "MobileNetSSD_deploy.prototxt"
model = "MobileNetSSD_deploy.caffemodel"
net = cv2.dnn.readNetFromCaffe(prototxt, model)

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

# --- 3. SETUP THE CAMERA ---
# Using the V4L2 fix that got your ribbon camera working!
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
# Let the camera warm up for a second
time.sleep(2)

def get_distance():
    # Send a quick pulse
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)
    
    start_time = time.time()
    stop_time = time.time()
    
    # Listen for the echo
    while GPIO.input(ECHO_PIN) == 0:
        start_time = time.time()
    while GPIO.input(ECHO_PIN) == 1:
        stop_time = time.time()
        
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300) / 2
    return distance

print("\n--- SMART PARKING SYSTEM ACTIVE ---")
print("Waiting for vehicle...")

try:
    while True:
        dist = get_distance()
        
        # If something breaks the 15cm tripwire...
        if dist < 15.0:
            print(f"\n[!] Tripwire broken! Object at {dist:.1f} cm. Waking camera...")
            
            # Flush the old frames and grab a fresh picture
            for _ in range(5): 
                cap.read()
            ret, frame = cap.read()
            
            if not ret:
                print("Camera failed to take a picture.")
                continue
                
            # Feed the picture to the AI
            blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
            net.setInput(blob)
            detections = net.forward()
            
            vehicle_found = False
            
            # Check the AI's answers
            for i in np.arange(0, detections.shape[2]):
                confidence = detections[0, 0, i, 2]
                
                if confidence > 0.50:
                    class_id = int(detections[0, 0, i, 1])
                    object_name = CLASSES[class_id]
                    
                    # THE PARKING LOGIC
                    if object_name in ["car", "motorbike", "bicycle"]:
                        print(f"-> VALID VEHICLE: {object_name.upper()} ({confidence*100:.0f}% confidence)")
                        print("-> SLOT STATUS: OCCUPIED")
                        vehicle_found = True
                        break # Stop looking, we found our vehicle!
                        
                    elif object_name == "person":
                        print(f"-> FALSE ALARM: Detected a person ({confidence*100:.0f}% confidence)")
                        print("-> SLOT STATUS: EMPTY")
                        vehicle_found = True
                        break
            
            if not vehicle_found:
                print("-> Unknown object. SLOT STATUS: EMPTY")
            
            # Wait 5 seconds so it doesn't spam the camera while the car is parked
            time.sleep(5) 
            print("\nWaiting for vehicle...")
            
        # Check the sensor twice a second
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nShutting down system...")
finally:
    GPIO.cleanup()
    cap.release()