# 🚦 Smart Traffic Controller

An adaptive, real-time traffic signal control system built on a **Raspberry Pi + PIC18F4550** dual-microcontroller architecture, using computer vision (OpenCV / TFLite) to detect vehicle density and dynamically allocate green-light duration to the most congested lane.

> Mini Project — Microcontrollers & Applications, Dept. of E&TC Engineering, Symbiosis Institute of Technology, Pune (July–December 2025)

---

## 📌 Overview

Traditional traffic lights run on fixed timers, which wastes time and fuel when roads are empty. This project replaces that with a **closed-loop, sensor-driven system**:

1. **IR sensors** detect vehicle presence at each of three road directions on the intersection.
2. The **PIC18F4550** drives a **servo motor** to rotate a Pi Camera to the corresponding direction (0°, 90°, 180°).
3. The **Raspberry Pi** captures a frame, runs it through an **object detection model (TFLite)** to count vehicles, and computes the required green-light duration.
4. The Pi drives traffic **LEDs directly via GPIO**, prioritizing the lane with the highest vehicle count.
5. The cycle repeats, allowing the system to continuously adapt to changing traffic conditions.

---

## 🏗️ System Architecture

| Unit | Role |
|---|---|
| **PIC18F4550** | Dedicated servo/camera positioning controller — reads IR sensors, generates PWM to rotate the camera, displays current position on LCD |
| **Raspberry Pi 4** | Central processing unit — image acquisition, OpenCV/TFLite vehicle detection, traffic light logic via GPIO |

The two controllers were deliberately decoupled (rather than run on a single MCU) to isolate the precision-timing task of servo control from the compute-heavy task of image processing.

---

## 🔧 Hardware Components

| Component | Qty | Purpose |
|---|---|---|
| PIC18F4550 Development Kit | 1 | Servo & IR sensor control |
| Raspberry Pi 4 Model B | 1 | Image processing & traffic light control |
| Pi Camera Module V2 (8MP) | 1 | Captures live traffic images |
| Servo Motor (SG90/MG995) | 1 | Rotates camera to 0°/90°/180° |
| IR Sensors | 4 | Vehicle presence detection |
| LEDs (Red/Yellow/Green) | 12 | Traffic signal simulation |
| Breadboard/PCB + wiring | — | Prototyping |

Full specs are in [`docs/appendix.md`](#) (operating voltages, response times, torque ratings, etc.).

---

## 💻 Software Stack

- **Embedded C** (MPLAB X IDE) — PIC18F4550 firmware for IR sensing + PWM servo control
- **Python 3** — Raspberry Pi control logic
- **OpenCV** — frame preprocessing and visualization
- **TFLite Runtime** — lightweight on-device vehicle detection
- **RPi.GPIO** — LED and sensor interfacing

---

## ⚙️ How It Works

```
IR Sensor Triggered → PIC rotates camera to matching angle (PWM)
        ↓
Raspberry Pi captures frame via Pi Camera (CSI)
        ↓
TFLite model detects & counts vehicles in frame
        ↓
Green-light duration computed from vehicle count
        ↓
Raspberry Pi drives GPIO LEDs (green for busiest lane, red for others)
        ↓
Cycle repeats → system re-scans all directions
```

Green-light duration scaling used in this prototype:

| Vehicles detected | Green duration |
|---|---|
| 1 | 3s |
| 2 | 6s |
| 3+ | 10s |

---

## 📂 Repository Structure

```
smart-traffic-controller/
├── firmware/
│   └── servo_ir_control.c      # PIC18F4550 embedded C code
├── raspberry-pi/
│   ├── servo_ir_control.py     # IR-triggered servo positioning
│   └── traffic_detection.py    # OpenCV/TFLite vehicle counting + LED control
├── models/
│   └── detect.tflite           # Object detection model
├── docs/
│   ├── block_diagram.png
│   ├── circuit_images/
│   └── project_report.pdf
└── README.md
```

---

## 🚀 Getting Started

### Raspberry Pi setup
```bash
sudo apt update && sudo apt install python3-opencv python3-pip
pip3 install tflite-runtime RPi.GPIO
python3 raspberry-pi/traffic_detection.py
```

### PIC18F4550 setup
1. Open `firmware/servo_ir_control.c` in **MPLAB X IDE**.
2. Compile with the XC8 compiler.
3. Flash to the PIC18F4550 dev kit via PICkit/ICD programmer.

---

## 🧪 Simulation & Testing

Servo positioning and IR sensor logic were first validated in **MPLAB X IDE** before hardware integration. OpenCV-based detection was tested standalone with LEDs simulating the traffic lights to confirm correct prioritization of the busiest lane before full assembly.

---

## ⚠️ Known Challenges

- **Logic-level mismatch** — Raspberry Pi GPIO (3.3V) vs. PIC18F4550 (5V) caused unreliable direct UART communication; a level shifter is required for robust interfacing.
- **UART resource conflict** — Using an Arduino Uno as a USB-to-serial bridge conflicted with the Pi's own USB-serial usage, leading to dropped data. A dedicated level-shifter IC (e.g., logic-level converter) is the recommended fix over a microcontroller relay.

---

## 📈 Applications

- Urban intersection traffic management
- Emergency vehicle priority routing (future scope)
- Fuel/emissions reduction via reduced idling
- Smart campus / smart city traffic automation

## 🔭 Future Scope

- Multi-class vehicle detection (car/bus/truck/two-wheeler) for weighted density scoring
- Emergency vehicle recognition via siren/RFID/GPS
- Networked, city-wide adaptive intersections
- Cloud/IoT dashboard for real-time traffic analytics

---

## 📄 References

- [PIC18F4550 Datasheet — Microchip](https://www.microchip.com)
- [Raspberry Pi 4 Documentation](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html)
- [Pi Camera Module Documentation](https://www.raspberrypi.com/documentation/accessories/camera.html)
- [OpenCV-Python Tutorials](https://docs.opencv.org/)
- [UART Communication Protocol — Analog Devices](https://www.analog.com)

---
