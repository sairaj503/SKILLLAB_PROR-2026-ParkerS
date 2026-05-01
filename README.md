# SKILL LAB PRATICAL HACKATHON

## Final Project README

> **Project Weight:** 100%  
> **Team Size:** 4/3 students  
> **Project Duration:** 16 hours  
> **Total Time Available:** 32 effort-hours per team  
> **Project Type:** Playful, interactive, technology-based experience

---

# Before you begin

## Fork and rename this repository

After forking this repository, rename it using the format:

`SKILLLAB_PROR-2026-TeamName`

### Example

`SKILLLAB_PROR-2026-AuroWizards`

Do not keep the default repository name.

---

# How to use this README

This file is your team’s **working project document**.

You must keep updating it throughout the build period.  
By the final review, this README should clearly show:

- your idea,
- your planning,
- your design decisions,
- your technical process,
- your build progress,
- your testing,
- your failures and changes,
- your final outcome.

## Rules

- Fill every section.
- Do not delete headings.
- If something does not apply, write `Not applicable` and explain why.
- Add images, screenshots, sketches, links, and videos wherever useful.
- Update task status and weekly logs regularly.
- Use this file as evidence of process, not only as a final report.

---

# 1. Team Identity

## 1.1 Studio / Group Name

`ParkerS`

## 1.2 Team Members

| Name              | Primary Role                  | Secondary Role | Strengths Brought to the Project |
| ----------------- | ----------------------------- | -------------- | -------------------------------- |
| Dhriti Mohata     | [Electronics / Fabrication]   | [Documentation]| Material Handling, Hardware      |
| Sairaj Indulkar   | [Electronics / Fabrication]   | [Coding]       | Material Handling,Hardware       |
| Vivek Thakare     | [Electronics / Fabrication]   | [Coding]       | Material Handling, Hardware      |
| Werda Wasey       | [Electronics / Coding]        | [Documentation]| Software                         |

## 1.3 Project Title

`Smart Parking System`

## 1.4 One-Line Pitch

`A smart parking system that detects and displays real-time slot occupancy using sensors and camera-based verification.`

## 1.5 Expanded Project Idea

`This project presents a Smart Parking System that combines sensor-based detection with camera-assisted verification to efficiently manage parking spaces. Each parking slot is equipped with an ultrasonic sensor that continuously monitors the presence of an object. When an object is detected, the system triggers a camera module connected to the Raspberry Pi 4 Model B to capture an image and classify whether the object is a vehicle (car/bike) or a non-relevant object such as a human. Based on this classification, the system updates the slot status as occupied or vacant and stores this information in a real-time availability table. This hybrid approach improves accuracy by reducing false detections and optimizes computational efficiency by activating the camera only when necessary. The system is scalable and can be extended with IoT integration, mobile applications, and number plate recognition for smart city implementations.`

---

# 2. Inspiration

## 2.1 References

List what inspired the project.

| Source Type | Title / Link                                                        | What Inspired You                                                                         |
| ----------- | ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `[Video]`   | `https://www.instagram.com/reel/DW4CT7WCDry/?igsh=cXg3dzAxYmdncDBo` | `How projection mapping can be used to create interactive digital + physical experiences` |
|             |                                                                     |                                                                                           |
|             |                                                                     |                                                                                           |

## 2.2 Original Twist

What makes your project original?

**Response:**  


---

# 3. Project Intent

## 3.1 User Journey 

A driver enters a parking area looking for a place to park his car. Instead of guessing or driving around aimlessly, he notices a display board at the entrance showing the current status of parking slots. It clearly indicates how many slots are occupied and how many are available. As a car leaves a slot, the system instantly updates—changing the slot status from occupied to vacant using sensor detection and camera verification. The user quickly checks the display, sees that a slot is free, and parks his car without confusion or delay. Once he parks, the system detects his car, verifies it, and updates the display again to reflect the new occupancy. This continuous real-time update ensures that every user gets accurate parking information, making the process faster, more efficient, and hassle-free.


                                  
---

# 4. Definition of Success

## 4.1 Definition of “Usable”

A usable smart parking system is one that can reliably detect whether a parking slot is occupied or vacant and clearly display this information to users in real time. The system should respond quickly to changes, such as a vehicle entering or leaving a slot, and update the display without noticeable delay. It must be simple to understand, with clear indicators (LED or LCD) so that users can easily identify parking availability without confusion. Even with a limited number of slots, the system should function accurately and consistently under normal conditions.

## 4.2 Minimum Usable Version

The minimum usable version of the project consists of a basic setup with at least one or two parking slots monitored using ultrasonic sensors. Each slot should have an indicator (such as red and green LEDs) to show whether it is occupied or vacant. A central controller like the Raspberry Pi 4 Model B processes the sensor data and updates a simple LCD display showing the total number of available and occupied slots. This version does not require a dashboard but must demonstrate accurate detection and real-time updates.

## 4.3 Stretch Features

Stretch features extend the system and make it more intelligent and scalable. These include integrating a camera module to classify detected objects and reduce false positives, adding a database or cloud connectivity to store parking data, and developing a mobile or web application to remotely view slot availability. Additional enhancements can include number plate recognition, automated entry logging, and integration with smart city infrastructure. These features improve accuracy, usability, and real-world applicability of the system.

---

# 5. System Overview

## 5.1 Project Type

Check all that apply.

- [x] Electronics-based

- [ ] Mechanical

- [x] Sensor-based

- [ ] App-connected

- [ ] Motorized

- [ ] Sound-based

- [ ] Light-based

- [x] Screen/UI-based

- [ ] Fabricated structure

- [x] Game logic based

- [ ] Installation

- [ ] Other:

## 5.2 High-Level System Description

Explain how the system works in simple terms.

Include:

- input,
- processing,
- output,
- physical structure,
- app interaction if any.

**Input:** 
The system takes input from ultrasonic sensors installed in each parking slot. These sensors detect the presence of an object by measuring distance. When an object is detected, the camera module is triggered to capture an image for verification.

**Processing:**
A central controller, such as the Raspberry Pi 4 Model B, processes the sensor data. If the ultrasonic sensor detects an object, the system activates the camera and classifies whether the object is a vehicle (car or bike) or something else. Based on this classification, the system decides whether the slot should be marked as occupied or vacant. The status of each slot is then stored in memory and updated continuously.

**Physical Structure:**
The setup consists of a small parking model with defined slots. Each slot is equipped with an ultrasonic sensor and LEDs. A camera module is positioned to capture images of the slots when triggered. All components are connected to the central controller through wires and mounted on a base structure.

**Output:**
The system displays the parking status using LEDs and an LCD display. Each slot has a visual indicator (red for occupied, green for vacant), while the LCD shows the total number of available and occupied slots in real time.

## 5.3 Input / Output Map

| System Part                              | Type            | What It Does                                                               |


---

# 6. System Design, Sketches and Visual Planning 

## 6.1 Concept Architecture/sketch/schematic

Add an early sketch of the full idea.

**Insert image below:**  
`<img width="1152" height="2272" alt="image" src="https://github.com/user-attachments/assets/8db896a4-f7ac-415e-bdc9-bcebd244a392" />
`

Example:

```md

```



## 6.2 Labeled Build Sketch/architecture/flow diagram/algorithm

Add a sketch with labels showing:

- structure,
- electronics placement,
- user touch points,
- moving parts,
- output elements.

**Insert image below:**  

## 6.3 Approximate Dimensions

| Dimension        | Value   |
| ---------------- | ------- |
| Length           | `16 cm` |
| Width            | `16 cm` |
| Height           | `8 cm`  |
| Estimated weight | `400 g` |

---

# 7. Electronics Planning

## 7.1 Electronics Used

| Component                 | Quantity | Purpose                               |
| ------------------------- | --------:| ------------------------------------- |
| `[Raspberry Pi 4B]`       | `1`      | `[Main controller]`                   |
| `[HC-SR04 Ultrsonic sensor]`| `1`      | `[Acts as the "low-power" trigger; measures distance to detect an arriving vehicle within 15cm]`      |
| `[I2C 16x2 LCD Display]`    | `1`      | `[Provides real-time visual feedback]`|
| `Rpi camera `             | `1`      | `[Captures image frames for object detection when triggered by the "tripwire."]` |

## 7.2 Wiring Plan

The Raspberry Pi 4B is connected to the 3.3V-compatible ultrasonic sensor (HC-SR04) using two GPIO pins. The trigger pin (Trig) is connected to GPIO 17 to send the polling signal, and the echo pin (Echo) is connected directly to GPIO 27 to safely receive the return pulse without needing a voltage divider. The camera module (OV5647) handles image capture separately and is connected directly to the Pi using the dedicated CSI ribbon cable port.

The system's visual feedback is handled by an I2C LCD and two 3.3V status LEDs. The 16x2 LCD uses two dedicated I2C pins: the data line (SDA) is connected to GPIO 2, and the clock line (SCL) is connected to GPIO 3. The status LEDs are connected to standard GPIO pins, with the green LED connected to GPIO 22 and the red LED connected to GPIO 23.

Power distribution is split based on the components' specific voltage requirements. The LCD display is powered by the Pi's 5V supply pin, while the ultrasonic sensor receives regulated power from the Pi's 3.3V supply pin. The LEDs operate safely on the 3.3V logic provided directly by their assigned GPIO pins. All components share a common ground with the Raspberry Pi to ensure stable logic levels and reliable system operation.

## 7.3 Circuit Diagram/architecture diagram

Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`
<img width="867" height="1156" alt="" src="" />


# 7.4. Power Plan

| Question         | Response                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Power source     | `Official Raspberry Pi USB-C Power Supply (or a high-quality equivalent wall adapter)`                                                                                                                           |
| Voltage required | `The system requires a stable 5.1V DC input. Internally, power is distributed as 5V to the I2C LCD and 3.3V to the ultrasonic sensor and status LEDs.`                                                                  |
| Current concerns | `The Raspberry Pi 4B can experience significant current spikes (up to 2.5A - 3.0A) when the camera activates and the CPU processes the MobileNet SSD AI inference. A power supply that cannot deliver a steady 3A will cause "low voltage" warnings, CPU throttling, or sudden system reboots during object detection.`                                       |
| Safety concerns  | `Exposed jumper wires on the breadboard or accidental bridging of GPIO pins could damage the Pi. Continuous or frequent AI inference can cause the Pi's CPU to overheat; adequate passive (heatsinks) or active (fan) cooling is highly recommended. Extreme care must be taken to ensure no 5V line (like the LCD VCC) accidentally touches any of the 3.3V-rated GPIO pins.`|

# 8. Software Planning/

## 8.1 Software Tools

| Tool / Platform | Purpose |
| :--- | :--- |
| **Raspberry Pi OS (Bookworm)** | The underlying Debian-based operating system providing hardware management, GPIO access, and the execution environment. |
| **Python 3** | The primary programming language used to integrate sensor polling, I2C communication, and the AI inference pipeline. |
| **Thonny IDE** | A lightweight Integrated Development Environment used for writing, executing, and debugging the Python scripts directly on the Pi. |
| **OpenCV (cv2)** | The core computer vision library used to handle camera streams, preprocess image frames (`blobFromImage`), and execute the deep learning model. |
| **MobileNet SSD (Caffe)** | A highly efficient, pre-trained object detection neural network used to identify specific classes (cars, motorbikes, bicycles) in real-time on edge hardware. |
| **libcamerify** | A vital compatibility wrapper utilized to allow legacy OpenCV scripts to interface seamlessly with the V4L2 camera backend on the new Bookworm OS architecture. |

## 8.2 Software Logic/Algorithm
Here is the Software Logic/Algorithm section tailored specifically to your Edge-AI Smart Parking System, matching the exact format of your sample:

### 8.2 Software Logic/Algorithm

- **Startup behavior:**  
  The Raspberry Pi initializes the GPIO pins for the ultrasonic sensor (Trig/Echo) and status LEDs (GPIO 22 Green, GPIO 23 Red). It establishes the I2C connection to the 16x2 LCD and pre-loads the MobileNet SSD (`.caffemodel` and `.prototxt`) into memory via OpenCV. To save resources, the camera begins in a standby/asleep state.
- **Input handling:**  
  The system operates autonomously based on physical environmental triggers rather than human input. The primary input loop listens for distance threshold breaches registered by the ultrasonic polling loop.
- **Sensor reading:**  
  The HC-SR04 ultrasonic sensor acts as a low-power tripwire, actively polling the parking slot twice a second (2Hz). If the sensor detects an object at a distance of less than 15cm, the system wakes up the OV5647 camera to capture a single, high-resolution frame.
- **Decision logic:**  
  The system utilizes "Sensor Fusion." The captured camera frame is passed through the MobileNet SSD inference engine. If the AI detects a "car," "motorbike," or "bicycle" with a confidence score greater than 50%, the system confirms a valid park. If the AI detects a "person" or nothing, it flags the event as a false alarm.
- **Output behavior:**  
  Based on the AI's decision, the Pi updates the 16x2 LCD display to read "Slot: OCCUPIED" or "Slot: EMPTY". Simultaneously, it updates the visual status LEDs, turning the Red LED (GPIO 23) on for occupied, or the Green LED (GPIO 22) on for empty.
- **Communication logic:**  
  Communication is handled internally via hardware protocols. The Python script sends string data over the I2C bus (SDA/SCL) to update the LCD screen, communicates with the camera via the CSI interface utilizing the `libcamerify` wrapper/V4L2 backend, and drives the LEDs via standard GPIO high/low signals.
- **Reset behavior:**  
  If the ultrasonic sensor reads a distance greater than 15cm (indicating the vehicle has left) or if the AI flags a false alarm, the system immediately resets the slot status to EMPTY, updates the LCD and Green LED, puts the camera back to sleep, and returns to the standard 2Hz ultrasonic polling loop.

## 8.3 Code Flowchart

Insert a flowchart showing your code logic.

Suggested sequence:

- start,
- initialize,
- wait for input,
- read input,
- decision,
- trigger output,
- repeat or reset,
- error handling.

**Insert image below:**  
<img width="1600" height="1200" alt="image" src="" />
<img width="1600" height="1200" alt="image" src="" />




# 9. Bill of Materials

## 9.1 Full BOM
# 9. Bill of Materials

## 9.1 Full BOM

| Item | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec | Why This Choice? |
| :--- | :---: | :---: | :---: | :--- | :--- | :--- |
| **Raspberry Pi 4B** | 1 | No | No (Owned) | ₹4,500 - ₹6,000 | 4GB/8GB RAM | Provides the necessary CPU overhead to run the MobileNet SSD inference engine locally at the edge. |
| **MicroSD Card** | 1 | No | No (Owned) | ₹400 | 32GB+ Class 10 | Required to boot Raspberry Pi OS (Bookworm) and store the Caffe model and prototxt files. |
| **RPi Camera (OV5647)** | 1 | Yes | No | ₹500 | 5MP, CSI Interface | Connects directly to the hardware CSI port, freeing up USB ports and providing sufficient resolution for AI detection. |
| **Ultrasonic Sensor (HC-SR04)** | 1 | Yes | No | ₹100 | 3.3V Compatible | Acts as a low-power tripwire to wake the camera, ensuring the AI only runs when a vehicle is present. |
| **16x2 I2C LCD Display** | 1 | Yes | No | ₹250 | 5V, PCF8574 Backpack | The I2C protocol requires only two GPIO pins (SDA/SCL), saving valuable pins for other sensors. |
| **Status LEDs** | 2 | Yes | No | ₹10 | 5mm (1 Red, 1 Green) | Provides immediate, high-visibility status updates (Occupied vs. Empty) at the hardware level. |
| **Breadboard & Jumpers** | 1 Set | Yes | No | ₹150 | Half-size, M-F / M-M | Facilitates quick, solderless prototyping and testing of the sensor and LED circuits. |
| **Official RPi Power Supply** | 1 | No | No (Owned) | ₹900 | 5.1V / 3.0A USB-C | Prevents low-voltage warnings and CPU throttling during power-intensive AI inference tasks. |

## 9.2 Material Justification

The Raspberry Pi 4B was chosen as the main controller instead of a standard microcontroller (like an ESP32) because the system requires a full operating system and significant CPU/RAM overhead to execute the MobileNet SSD deep learning model locally at the edge. An HC-SR04 ultrasonic sensor was integrated as a low-power "tripwire" rather than relying on a continuous live video feed (which was avoided as continuous video processing would quickly lead to thermal throttling and high resource consumption on the Pi). This Sensor Fusion approach ensures that the OV5647 camera—selected for its native CSI hardware connection rather than relying on a slower, latency-prone USB webcam—only wakes up to capture a frame when an object is physically detected within 15cm. Finally, a 16x2 LCD with an I2C backpack was utilized instead of a standard parallel display to drastically reduce GPIO pin usage (requiring only SDA and SCL), leaving plenty of stable 3.3V pins for the direct ultrasonic and status LED connections.


## 9.3 Items You chose

| Item                 | Why Needed               |
| -------------------- | ------------------------ | 
| `RPi Camera (OV5647)` | `Capture frames for AI inference`   | 
| `Ultrasonic Sensor (HC-SR04)`     |`Low-power hardware tripwire` | 
| `16x2 I2C LCD Display`   | `Visual text status (Occupied/Empty)`      | 
| `Status LEDs`          | `Hardware status signaling`|

## 9.4 Budget Summary

| Budget Item           | Estimated Cost              |
| --------------------- | ---------------------------:|
| Electronics           | `[1010]`                     |
| Mechanical parts      | `[200]`                     |
| Fabrication materials | `[0 (Aldready Owned     )]` |
| Purchased extras      | `[0]`                       |
| Contingency           | `[300]`                     |
| **Total**             | `[1510]`                     |

## 9.5 Budget Reflection

To significantly reduce costs, the architecture could be modified in the following ways:

1. Compute Substitution (The Pi 4B): For an individual edge node, the Pi 4B could be swapped for a cheaper Raspberry Pi Zero 2 W. However, this trade-off requires software optimization; the MobileNet SSD inference model would need to be heavily quantized (e.g., using TFLite with INT8 precision) to run smoothly on the Zero's limited RAM and CPU architecture.

2. Component Removal (The LCD): The 16x2 I2C LCD display could be eliminated. The red and green status LEDs already provide immediate, high-visibility feedback to the driver at the physical parking spot. The text-based slot data can simply be routed to a headless web dashboard or a centralized parking lot display board, reducing both hardware costs and enclosure complexity at the individual slot level.

---

# 10. Planning the Work

## 10.1 Team Working Agreement

Write how your team will work together.

Include:

- how tasks are divided,
- how decisions are made,
- how progress will be checked,
- what happens if a task is delayed,
- how documentation will be maintained.

**Response:**  


## 10.2 Task Breakdown

| Task ID | Task                    | Owner    | Estimated Hours | Deadline     | Dependency | Status |
| ------- | ----------------------- | -------- | ---------------:| ------------ | ---------- | ------ |
| T1      | `[Finalize concept]`    | `[Both]` | `2`             | `1st April`  | `None`     | `Done` |


## 10.3 Responsibility Split

| Area                 | Main Owner     | Support Owner |
| -------------------- | ----------     | ------------- |
| Concept              | `[Mrugendra]`  | `[Jyoti]`     |
| Electronics          | `[]`           | `[]`          |
| Coding               | `[]`           | `[]`          |
| Mechanical build     | `[]`           | `[]`          |
| Testing              | `[]`           | `[]`          |
| Documentation        | `[]`           | `[]`          |

---

# 11 hour Milestones

## 11.1 8-hour Plan(tentetively you may set)

### Bi Hour 1 — Plan and De-risk

Expected outcomes:

- [x] Idea finalized
- [x] Core interaction decided
- [x] Sketches made
- [x] BOM completed
- [x] Purchase needs identified
- [ ] Key uncertainty identified
- [x] Basic feasibility tested

### Bi Hour 2 — Build Subsystems

Expected outcomes:

- [x] Electronics tests completed
- [ ] CAD / structure planning completed
- [ ] App UI started if needed
- [x] Mechanical concept tested
- [x] Main subsystems partially working

### Bi Hour 3 — Integrate

Expected outcomes:

- [x] Physical body built
- [x] Electronics integrated
- [x] Code connected to hardware
- [ ] App connected if required
- [x] First playable version exists

### Bi Hour 4 — Refine and Finish

Expected outcomes:

- [x] Technical bugs reduced
- [x] Playtesting completed
- [x] Improvements made
- [x] Documentation completed
- [x] Final build ready

## 12.2  Update Log

| Days   | Planned Goal   | What Actually Happened | What Changed   | Next Steps     |
| ------ | -------------- | ---------------------- | -------------- | -------------- |
| Day 1 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 2 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 3 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |
| Day 4 | `[Write here]` | `[Write here]`         | `[Write here]` | `[Write here]` |

---

# 13. Risks and Unknowns

## 13.1 Risk Register

| Risk                                                            | Type         | Likelihood | Impact   | Mitigation Plan                                                                       | Owner                |
| --------------------------------------------------------------- | ------------ | ---------- | -------- | ------------------------------------------------------------------------------------- | -------------------- |
| WiFi connection between laptop and ESP32 becomes unstable       | `Technical`  | `Medium`   | `High`   | Keep ESP32 close, ensure stable power supply, reduce network load, add fail-safe stop | `[Gopal]`           |


## 13.2 Biggest Unknown Right Now

What is the single biggest uncertainty in your project at this stage?

**Response:**  


---

# 14. Testing 

## 14.1 Technical Testing Plan

| What Needs Testing     | How You Will Test It                                                                 | Success Condition                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| `[Wifi connection]`    | `[Check if motor spins via app button]`                                              | `[Both motors accurately respond to wifi signals]`                                                   |
                       |
## 14.2 Testing and Debugging Log

| Date          | Problem Found                         | Type         | What You Tried                                | Result               | Next Action                                    |
| ------------- | ------------------------------------- | ------------ | --------------------------------------------- | -------------------- | ---------------------------------------------- |
| `18th April`  | `Car not balancing properly`          | `Mechanical` | `Add low-friction caster support to one side` | `Worked`             | `improve caster structure`                     |


## 14.3 Playtesting Notes

| Tester      | What They Did                        | What Confused Them                    | What They Enjoyed                         | What You Will Change                          |
| ----------- | ------------------------------------ | ------------------------------------- | ----------------------------------------- | --------------------------------------------- |
| `Gopal` | `Tried navigating through obstacles` | `Some obstacles ewren't clear enough` | `Liked projection + real car interaction` | `Add a slight red highlight around obstacles` |


---

# 15. Build Documentation

## 15.1 Fabrication Process(if any)

Describe how the project was physically made.

Include:

- cutting,
- 3D printing,
- assembly,
- fastening,
- wiring,
- finishing,
- revisions.

**Response:**  
`The fabrication process involved designing, manufacturing, assembling, and refining both the physical structure and electronic integration of the system.`

`Design (CAD Modeling):
The initial model was created using CAD software, where components were designed based on the actual dimensions of the electronic parts. This ensured accurate fitting and minimized errors during assembly.
Cutting (Laser Cutting):
The designed parts were fabricated using laser cutting techniques. Sheets were cut precisely according to the CAD model to create the structural base and mounts for components.`

`Components were fixed using adhesives and mechanical supports. Certain parts were intentionally kept modular (not permanently fixed) to allow easy replacement and modification of electronics.
Surface Finishing:
Some parts were sanded to smooth rough edges after cutting. Sawdust mixed with adhesive was used to fill gaps and uneven edges, improving structural finish. The final structure was then painted for better aesthetics and durability.`

`Environment Setup (Dark Room Fabrication):
To enhance projection visibility, a controlled dark environment was created using Z-boards, paper sheets, and bedsheets. This minimized external light interference and improved projection clarity.
Revisions and Iterations:
Multiple adjustments were made throughout the process, including refining alignment, improving structural stability, repositioning components, and optimizing the interaction between the physical car and projected environment.`

## 16 Build Photos

Add photos throughout the project.

Suggested images:

- early sketch,
- prototype,
- electronics testing,
- mechanism test,
- app screenshot,
- final build.
- <img width="960" height="1280" alt="WhatsApp Image 2026-04-24 at 9 46 02 AM (1)" src="https://github.com/user-attachments/assets/74baa570-5770-483e-be6d-d2f03386e37c" />





# 17. Final Outcome

## 17.1 Final Description

Describe the final version of your project.

**Response:**  


## 17.2 What Works Well



## 17.3 What Still Needs Improvement


## 17.4 What Changed From the Original Plan

How did the project change from the initial idea?

**Response:**  


---

# 18. Reflection

## 18.1 Team Reflection

What did your team do well?  
What slowed you down?  
How well did you manage time, tasks, and responsibilities?

**Response:**  


## 18.2 Technical Reflection

What did you learn about:

- electronics,
- coding,
- mechanisms,
- fabrication,
- integration?

**Response:**  


## 18.3 Design Reflection

What did you learn about:

- designing ,
- delight,
- clarity,
- physical interaction,
- understanding,
- iteration?

**Response:**  


## 18.4 If You Had One More hour

What would you improve next?

**Response:**  

` `

---

# 19. Final Submission Checklist

Before submission, confirm that:

- [x] Team details are complete
- [x] Project description is complete
- [x] Inspiration sources are included
- [x] Sketches are added
- [x] BOM is complete
- [x] Purchase list is complete
- [x] Budget summary is complete
- [x] Mechanical planning is documented if applicable
- [ ] App planning is documented if applicable
- [x] Code flowchart is added
- [x] Task breakdown is complete
- [x] Weekly logs are updated
- [x] Risk register is complete
- [x] Testing log is updated
- [x] Playtesting notes are included
- [x] Build photos are included
- [x] Final reflection is written
<img width="1131" height="1600" alt="image" src="" />

---


---


