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
| Dhriti Mohata     | [Electronics / Fabrication]   | [Coding]       | Material Handling, Hardware      |
| Sairaj Indulkar   | [Electronics / Fabrication]   | [Coding]       | Material Handling, Hardware      |
| Vivek Thakare     | [Electronics / Fabrication]   | [Coding]       | Material Handling, Hardware      |
| Werda Wasey       | [Electronics / Fabrication]   | [Coding]       | Material Handling, Hardware      |

## 1.3 Project Title

`Smart Parking System`

<img width="1600" height="1131" alt="image" src="https://github.com/user-attachments/assets/c64bfbd4-b3b7-43d9-83ad-c203a5aa11bc" />

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
`[Upload image and link here]`

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
`[Upload image and link here]`
<img width="1600" height="1200" alt="image" src="https://github.com/user-attachments/assets/95637f31-b4e7-4427-a9e1-4b63fbeb0ac5" />

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
| `[Raspi/FPGA]`                 | `1`      | `[Main controller]`                   |
| `[L298N Motor Driver]`    | `1`      | `[Control Motors]`                    |
| `[BO Motors]`             | `2`      | `[Rotate wheels]`                     |
| `[Buck Converter]`        | `1`      | `[Power ESP32]`                       |
| `[Li Ion Battery Pack]`   | `2`      | `[Power]`                             |
| `[Projector]`             | `1`      | `[Display obstacles]`                 |
| `Camera (Webcam / Phone)` | `1`      | `[Tracks car position using markers]` |

## 7.2 Wiring Plan

Describe the main electrical connections.

**sample Response:**  
`The RASPI is connected to the motor driver (L298N) using four GPIO pins (18,19; 22,23) to control motor direction (IN1, IN2, IN3, IN4). Two PWM-capable pins (ENA and ENB; 25 and 26) are connected to control the speed of each motor.

The motors are connected to the output terminals of the motor driver. The motor driver is powered directly by the battery pack (higher voltage), while the ESP32 receives regulated 5V from the buck converter.

All components share a common ground to ensure stable operation. The projector and camera are connected to the laptop, which handles tracking and game logic separately.`

## 7.3 Circuit Diagram/architecture diagram

Insert a hand-drawn or software-made circuit diagram.

**Insert image below:**  
`[Upload image and link here]`
<img width="867" height="1156" alt="" src="" />


# 7.4. Power Plan

| Question         | Response                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Power source     | `Battery (Li-ion pack)`                                                                                                                           |
| Voltage required | `~6–8.4V for motors (via driver), stepped down to 5V for ESP32 (buck converter)`                                                                  |
| Current concerns | `Motors can draw high current under load, which may cause voltage drops affecting ESP32 and WiFi stability`                                       |
| Safety concerns  | `Avoid over-discharging Li-ion batteries, ensure proper voltage regulation, prevent short circuits, and secure wiring to avoid loose connections` |

---

# 8. Software Planning/

## 8.1 Software Tools

| Tool / Platform                | Purpose                                        |
| ------------------------------ | ---------------------------------------------- |
| `[MicroPython]`                | `Control ESP32`                                |
| `[Python/PyGame/OpenCV]`       | `Track markers, game logic, create projection` |
| `[Fusion/Blender/Illustrator]` | `[Prototyping structure]`                      |
|                                |                                                |

## 8.2 Software Logic/Algorithm

Describe what the code must do.

Include:

- startup behavior,
- input handling,
- sensor reading,
- decision logic,
- output behavior,
- communication logic,
- reset behavior.

**Response:**  
`

- **Sample Startup behavior:**  
  The Raspi/FPGA initializes motor pins, PWM control, and starts a WiFi access point with a web server. The laptop initializes camera input, tracking system, and projection mapping.
- **Input handling:**  
  Movement commands are received from the laptop (pygame sends http requests)
- **Sensor reading:**  
  The camera continuously captures frames, and OpenCV detects ArUco markers to determine the car’s position and orientation.
- **Decision logic:**  
  The system maps the car’s position into a virtual coordinate system and checks for nearby obstacles or collisions. If movement is valid, the command is allowed; if not, it is blocked or replaced with a feedback action (like a slight shake).
- **Output behavior:**  
  The ESP32 drives the motors using PWM signals to control speed and direction. The projector displays the updated game environment, including obstacles, targets, and feedback visuals.
- **Communication logic:**  
  The laptop sends HTTP requests (e.g., `/forward`, `/left`) to the ESP32 over WiFi. The ESP32 parses these commands and executes motor actions.
- **Reset behavior:**  
  If no command is received within a short timeout, the ESP32 stops the motors. The game resets when a level is completed or restarted.`

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

| Item                             | Quantity | In Kit? | Need to Buy? | Estimated Cost | Material / Spec               | Why This Choice?          |
| -------------------------------- | --------:| ------- | ------------ | --------------:| ----------------------------- | ------------------------- |
| `[RASPI]`                        | `1`      | `Yes`   | `No`         | `0`            | `38 Pin ESP32`                | `[To control components]` |
| `[Motor Driver]`                 | `[1]`    | `[Yes]` | `[No]`       | `0`            | `[LN296]`                     | `[To drive both motors]`  |
| `[DC Motors and wheel]`          | `[2]`    | `[No]`  | `[Yes]`      | `[150]`        | `[BO Motors and 6 cm wheels]` | `[high torque motors]`    |
| `[Buck Converter]`               | `[1]`    | `[No]`  | `[Yes]`      | `[75]`         |                               |                           |
| `[Li-ion batteries with holder]` | `[1]`    | `[No]`  | `[Yes]`      | `[200]`        |                               |                           |

## 9.2 Material Justification

Explain why you selected your main materials and components.

**Response:**  
`DC motors (BO motors) were chosen instead of servos or steppers because the system requires continuous rotation for movement rather than precise angular control (Previously, we were considering using steppers as we were planning on tracking movement on the ESP using its relative position from an origin, but since we're using a camera now, this is not required). A motor driver (L298N) was used to allow bidirectional control and speed variation using PWM.`


## 9.3 Items You chose

| Item                 | Why Needed               | Purchase Link | Latest Safe Date to Procure | Status       |
| -------------------- | ------------------------ | ------------- | --------------------------- | ------------ |
| `BO Motors + Wheels` | `Drive system for car`   | `robu.in`     | `15th April`                | `[Received]` |
| `Buck Converter`     | `Stable power for ESP32` | `local store` | `before testing`            | `[Received]` |
| `Li-ion Batteries`   | `Portable power`         | `local store` | `before testing`            | `Recieved`   |

## 9.4 Budget Summary

| Budget Item           | Estimated Cost              |
| --------------------- | ---------------------------:|
| Electronics           | `[400]`                     |
| Mechanical parts      | `[200]`                     |
| Fabrication materials | `[0 (Available on campus)]` |
| Purchased extras      | `[0]`                       |
| Contingency           | `[300]`                     |
| **Total**             | `[900]`                     |

## 9.5 Budget Reflection

If your cost is too high, what can be simplified, removed, substituted, or shared?

**Response:**  

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


