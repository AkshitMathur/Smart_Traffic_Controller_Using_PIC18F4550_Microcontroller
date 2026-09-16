# 🚦 Smart Traffic Controller

### Intelligent Traffic Density Monitoring and Adaptive Signal Control using PIC18F4550, Raspberry Pi and Computer Vision

<p align="center">
  <b>
    A hybrid embedded and computer-vision system for real-time vehicle detection,
    traffic-density estimation and adaptive traffic signal control.
  </b>
</p>

<p align="center">

![PIC18F4550](https://img.shields.io/badge/MCU-PIC18F4550-blue)
![Raspberry Pi](https://img.shields.io/badge/Platform-Raspberry%20Pi-red)
![Embedded C](https://img.shields.io/badge/Embedded%20C-XC8-orange)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![OpenCV](https://img.shields.io/badge/Computer%20Vision-OpenCV-green)
![TensorFlow Lite](https://img.shields.io/badge/ML-TensorFlow%20Lite-orange)
![Project](https://img.shields.io/badge/Type-Embedded%20Systems-success)
![Status](https://img.shields.io/badge/Status-Prototype%20Implemented-brightgreen)

</p>

---

## 📌 Overview

Conventional traffic signal systems commonly operate using predefined timing cycles, regardless of the actual traffic present on individual roads. This can result in inefficient signal utilization and unnecessary vehicle waiting.

**Smart Traffic Controller** is an academic engineering prototype that demonstrates an adaptive traffic-management approach using **embedded systems, computer vision and machine learning**.

The system combines two computing layers:

- **PIC18F4550** — handles low-level embedded control, IR sensor interfacing, PWM generation and servo-based camera positioning.
- **Raspberry Pi** — performs camera acquisition, image processing, vehicle detection, vehicle counting and traffic-signal decision making.

A **Pi Camera Module V2** is mounted on a servo motor and positioned toward different road directions. The Raspberry Pi processes the captured frames using **OpenCV and a TensorFlow Lite object-detection model**.

Detected vehicles are counted and the vehicle count is used as an indicator of traffic density. The controller then selects a predefined green-light duration based on the detected traffic level.

The project demonstrates the integration of:

> **Embedded Systems + Sensors + PWM + Computer Vision + Machine Learning + Edge Computing + GPIO Control**

---

# 🎯 Objectives

- Detect vehicles from live camera frames.
- Estimate traffic density using detected vehicle count.
- Interface IR sensors with the PIC18F4550.
- Control a servo motor using PWM.
- Position a camera toward multiple road directions.
- Process camera frames using OpenCV.
- Perform lightweight object detection using TensorFlow Lite.
- Count detected vehicles.
- Determine adaptive green-light duration.
- Control traffic signal LEDs using Raspberry Pi GPIO.
- Demonstrate integration between an 8-bit microcontroller and edge-computing platform.

---

# 🏛️ System Architecture

```mermaid
flowchart LR

    subgraph TRAFFIC["Traffic Intersection"]
        A[IR Sensors]
    end

    subgraph PIC["PIC18F4550 - Embedded Control"]
        B[IR Sensor Interface]
        C[PWM Generation]
        D[Servo Control]
        E[16x2 LCD]
    end

    subgraph CAMERA["Camera Positioning"]
        F[Servo Motor]
        G[Pi Camera Module V2]
    end

    subgraph PI["Raspberry Pi - Intelligent Processing"]
        H[Image Acquisition]
        I[OpenCV]
        J[TensorFlow Lite]
        K[Vehicle Detection]
        L[Vehicle Counting]
        M[Traffic Density Estimation]
        N[Adaptive Signal Decision]
    end

    subgraph SIGNAL["Traffic Signal"]
        O[Red LEDs]
        P[Yellow LEDs]
        Q[Green LEDs]
    end

    A --> B
    B --> C
    C --> D
    D --> F
    F --> G

    G --> H
    H --> I
    I --> J
    J --> K
    K --> L
    L --> M
    M --> N

    N --> O
    N --> P
    N --> Q

    B --> E

```
