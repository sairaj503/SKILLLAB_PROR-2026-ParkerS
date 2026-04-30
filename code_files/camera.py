import cv2
import numpy as np

print("1. Loading the AI Model...")
# Tell OpenCV the exact names of your downloaded files
prototxt = "MobileNetSSD_deploy.prototxt"
model = "MobileNetSSD_deploy.caffemodel"

# Build the brain!
net = cv2.dnn.readNetFromCaffe(prototxt, model)

# These are the 20 specific words this Caffe model knows
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]

print("2. Starting the Camera...")
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Camera not opened")
    exit()

while True:
    # Snap a picture
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Resize the frame so it fits nicely on your monitor
    frame = cv2.resize(frame, (640, 480))

    # --- THIS IS WHERE THE MAGIC HAPPENS ---
    # Convert the picture into a "Blob" the AI can understand
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843, (300, 300), 127.5)
    
    # Feed the Blob to the AI
    net.setInput(blob)
    
    # Tell the AI to calculate what it sees!
    detections = net.forward()
    
    # --- NOW WE FILTER THE RESULTS ---
    # Loop over everything the AI found
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2] # Get the confidence score
        
        # Only pay attention if the AI is more than 50% sure
        if confidence > 0.50:
            class_id = int(detections[0, 0, i, 1])
            object_name = CLASSES[class_id]
            
            # If it's a Car, Motorbike, Bicycle, or Person, draw a box!
            if object_name in ["car", "motorbike", "bicycle", "person"]:
                
                # Math to draw a box around the object on your screen
                (h, w) = frame.shape[:2]
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")
                
                # Choose box color: Green for vehicles, Red for person
                color = (0, 255, 0) if object_name in ["car", "motorbike", "bicycle"] else (0, 0, 255)
                
                # Draw the rectangle and the text on the video feed
                cv2.rectangle(frame, (startX, startY), (endX, endY), color, 2)
                text = f"{object_name.upper()}: {confidence * 100:.0f}%"
                cv2.putText(frame, text, (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Show the live video feed on your screen!
    cv2.imshow("Smart Parking Camera Test", frame)

    # Press 'q' on your keyboard to quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Clean up when you exit
cap.release()
cv2.destroyAllWindows()