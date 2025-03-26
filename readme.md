# **🧠 EEG-Based Wireless Car Control 🚗**

## **📌 Project Overview**
This project implements a **wireless, real-time EEG-controlled car** using the **BioAmp EXG Pill, ESP32, and Arduino Mega**. It processes **brain signals** to classify user attention states and transmits control signals to move or stop the car with **low latency** using **ESP-NOW**.

## **🎯 Features**
✅ **EEG-based control**: Uses brain activity to control movement.
✅ **Wireless communication**: ESP32s use **ESP-NOW** for low-latency data transfer.
✅ **Real-time processing**: Machine learning-based EEG classification.
✅ **Motor control**: Arduino Mega and L298N drive the car.
✅ **Cybersecurity**: Encryption and authentication prevent spoofing.

---

## **🛠 Hardware Requirements**
- **2x ESP32 DevKit V1** (for EEG processing & wireless communication)
- **1x Maker UNO** (for EEG ADC conversion)
- **1x Arduino Mega** (for motor control)
- **1x L298N Motor Driver** (for DC motors)
- **4x DC Motors** (parallel connection for car movement)
- **BioAmp EXG Pill** (for EEG data acquisition)
- **Electrodes, EEG Gel, Headband**

---

## **📜 System Architecture**
1️⃣ **Laptop (`prediction.py`)**:
   - Captures EEG signals via **Maker UNO (ADC)**.
   - Processes data & classifies states (Focus = `1`, Relax = `0`).
   - Sends commands to **ESP32 Master** via Serial.

2️⃣ **ESP32 Master**:
   - Reads classification (`0` or `1`) from Serial.
   - Sends "FORWARD" or "STOP" via **ESP-NOW** to **ESP32 Car Controller**.

3️⃣ **ESP32 Car Controller**:
   - Receives movement commands.
   - Sends them to **Arduino Mega via Serial2 (UART)**.

4️⃣ **Arduino Mega**:
   - Controls **L298N Motor Driver**.
   - Moves or stops the car based on received commands.

---

## **📂 Code Setup**
### **🔹 1. Clone the Repository**
```sh
git clone https://github.com/yourusername/EEG-Car-Control.git
cd EEG-Car-Control
```

### **🔹 2. Upload the Code**
- **ESP32 Master** → `esp32_master.ino`
- **ESP32 Car Controller** → `esp32_car.ino`
- **Arduino Mega** → `arduino_mega.ino`
- **Laptop (EEG Processing)** → `prediction.py`

### **🔹 3. Install Dependencies** (For `prediction.py`)
```sh
pip install numpy pandas scipy pyserial pickle
```

### **🔹 4. Find Your ESP32 Car Controller MAC Address**
Upload the following to your ESP32 Car Controller:
```cpp
#include <WiFi.h>
void setup() {
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);
    Serial.print("ESP32 MAC Address: ");
    Serial.println(WiFi.macAddress());
}
void loop() {}
```
📌 **Update the MAC Address** in `esp32_master.ino` before flashing!

---

## **🔐 Cybersecurity Features**
✅ **ESP-NOW Encryption** – Ensures secure communication.
✅ **AES-256 Encryption** – Secures EEG data before transmission.
✅ **HMAC-SHA256 Authentication** – Prevents signal spoofing.
✅ **Secure Boot & Flash Encryption** – Protects firmware integrity.
✅ **No Debug Serial Logs in Production** – Prevents data leakage.

---

## **📌 Future Improvements**
- 🎯 **Enhancing ML Model** for better EEG classification.
- 📶 **Expanding Wireless Range** with LoRa.
- 🔄 **Integrating More Control Commands** (e.g., Turn Left/Right).

---

## **📜 License**
This project is **open-source** under the **MIT License**.

🚀 **Happy Hacking!** Let me know if you need any improvements! 😊

