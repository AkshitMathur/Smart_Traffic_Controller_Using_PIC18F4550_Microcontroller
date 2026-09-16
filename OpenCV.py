import cv2 
import numpy as np 
import tflite_runtime.interpreter as tflite 
import RPi.GPIO as GPIO 
from time import time, sleep 
# === GPIO Setup === 
RED_LED = 16 
GREEN_LED = 26 
GPIO.setmode(GPIO.BCM) 
GPIO.setup(RED_LED, GPIO.OUT) 
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.output(RED_LED, GPIO.HIGH)   # Start with RED 
ON 
GPIO.output(GREEN_LED, GPIO.LOW) 
# === Load TFLite Model === 
MODEL_PATH = 
"/home/kautik/tflite_car_recognition/detect.tflite" 
LABEL_PATH = 
"/home/kautik/tflite_car_recognition/labels.txt" 
interpreter = 
tflite.Interpreter(model_path=MODEL_PATH) 
interpreter.allocate_tensors() 
input_details = interpreter.get_input_details() 
output_details = interpreter.get_output_details() 
input_shape = input_details[0]['shape'][1:3] 
# === Load labels === 
with open(LABEL_PATH, "r") as f: 
    labels = [line.strip() for line in f.readlines()] 
# === Initialize Camera === 
gst_pipeline = ( 
    "libcamerasrc ! video/x
raw,width=640,height=480,framerate=30/1,format=
RGB ! " 
    "videoconvert ! appsink" 
) 
cap = cv2.VideoCapture(gst_pipeline, 
cv2.CAP_GSTREAMER) 
if not cap.isOpened(): 
    print("  Failed to open CSI camera.") 
    GPIO.cleanup() 
    exit(1) 
print("   Starting Smart Traffic System (press 'q' to 
quit)") 
# === Helper function for LED control === 
def control_lights(car_count): 
    if car_count == 0:
    return 
# Define green durations 
    duration = {1: 3, 2: 6}.get(car_count, 10)  # default 
10 for >=3 
    print(f"         {car_count} car(s) detected → GREEN for 
{duration}s") 
    # Turn GREEN ON 
    GPIO.output(RED_LED, GPIO.LOW) 
    GPIO.output(GREEN_LED, GPIO.HIGH) 
    sleep(duration) 
    # Turn RED back ON 
    GPIO.output(GREEN_LED, GPIO.LOW) 
    GPIO.output(RED_LED, GPIO.HIGH) 
    print("  Back to RED, waiting for new input...\n") 
# === Main Loop === 
while True: 
    ret, frame = cap.read() 
    if not ret or frame is None: 
        print("    Frame capture failed. Retrying...") 
        continue 
    frame_bgr = cv2.cvtColor(frame, 
cv2.COLOR_RGB2BGR) 
    input_data = cv2.resize(frame, tuple(input_shape)) 
    input_data = np.expand_dims(input_data, 
axis=0).astype(np.uint8) 
    start_time = time() 
    interpreter.set_tensor(input_details[0]['index'], 
input_data) 
    interpreter.invoke() 
    boxes = 
interpreter.get_tensor(output_details[0]['index'])[0] 
    classes = 
interpreter.get_tensor(output_details[1]['index'])[0] 
    scores = 
interpreter.get_tensor(output_details[2]['index'])[0]
car_count = 0 
    for i in range(len(scores)): 
        if scores[i] > 0.5 and int(classes[i]) < len(labels): 
            label_name = labels[int(classes[i])].lower() 
            if label_name == "car": 
                car_count += 1 
                ymin, xmin, ymax, xmax = boxes[i] 
                left, top, right, bottom = int(xmin*640), 
int(ymin*480), int(xmax*640), int(ymax*480) 
                cv2.rectangle(frame_bgr, (left, top), (right, 
bottom), (0, 255, 0), 2) 
    car_count = min(car_count, 3) 
    control_lights(car_count) 
    fps = 1 / (time() - start_time) 
    cv2.putText(frame_bgr, f"Cars: {car_count}  FPS: 
{fps:.1f}", (10, 25), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 
255), 2) 
    cv2.imshow("Smart Traffic - Car Detection", 
frame_bgr) 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        print("   Quitting...") 
        break 
# === Cleanup === 
cap.release() 
cv2.destroyAllWindows() 
GPIO.cleanup()
