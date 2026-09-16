import RPi.GPIO as GPIO 
import time 
# --- GPIO Pin Setup --- 
SERVO_PIN = 18 
IR1_PIN = 17 
IR2_PIN = 5 
IR3_PIN = 22 
# --- GPIO Initialization --- 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(SERVO_PIN, GPIO.OUT) 
GPIO.setup(IR1_PIN, GPIO.IN) 
GPIO.setup(IR2_PIN, GPIO.IN) 
GPIO.setup(IR3_PIN, GPIO.IN) 
# --- Servo Setup --- 
servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz PWM for 
servo 
servo.start(0) 
def set_servo_angle(angle): 
    """Set servo position (0–180°).""" 
    duty = 2 + (angle / 18)  # Map angle to duty cycle 
    GPIO.output(SERVO_PIN, True) 
    servo.ChangeDutyCycle(duty) 
    time.sleep(0.5) 
    GPIO.output(SERVO_PIN, False) 
    servo.ChangeDutyCycle(0) 
# --- Main Loop --- 
try: 
    print("Starting Servo Control (Press Ctrl+C to 
stop)") 
    last_angle = -1
               
import RPi.GPIO as GPIO 
import time 
# --- GPIO Pin Setup --- 
SERVO_PIN = 18 
IR1_PIN = 17 
IR2_PIN = 5 
IR3_PIN = 22 
# --- GPIO Initialization --- 
GPIO.setmode(GPIO.BCM) 
GPIO.setwarnings(False) 
GPIO.setup(SERVO_PIN, GPIO.OUT) 
GPIO.setup(IR1_PIN, GPIO.IN) 
GPIO.setup(IR2_PIN, GPIO.IN) 
GPIO.setup(IR3_PIN, GPIO.IN) 
# --- Servo Setup --- 
servo = GPIO.PWM(SERVO_PIN, 50)  # 50Hz PWM for 
servo 
servo.start(0) 
def set_servo_angle(angle): 
    """Set servo position (0–180°).""" 
    duty = 2 + (angle / 18)  # Map angle to duty cycle 
    GPIO.output(SERVO_PIN, True) 
    servo.ChangeDutyCycle(duty) 
    time.sleep(0.5) 
    GPIO.output(SERVO_PIN, False) 
    servo.ChangeDutyCycle(0) 
# --- Main Loop --- 
try: 
    print("Starting Servo Control (Press Ctrl+C to 
stop)") 
    last_angle = -1 
 
 
 
while True: 
        if GPIO.input(IR1_PIN) == 0: 
            angle = 0 
        elif GPIO.input(IR2_PIN) == 0: 
            angle = 90 
        elif GPIO.input(IR3_PIN) == 0: 
            angle = 180 
        else: 
            angle = 0  # Default position if no IR detected 
 
        if angle != last_angle: 
            print(f"→ Moving Servo to {angle}°") 
            set_servo_angle(angle) 
            last_angle = angle 
        time.sleep(0.1) 
except KeyboardInterrupt: 
    print("\nExiting program...") 
finally: 
    servo.stop() 
    GPIO.cleanup()
