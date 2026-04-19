# 📘 Rideau Canal Sensor Simulation

## Overview
This repository contains the **IoT sensor simulation** component of the *Rideau Canal Real‑time Monitoring System* for the CST8916 – Remote Data and Real‑time Applications course.

The simulator generates synthetic environmental telemetry for three monitoring locations along the Rideau Canal:

- **Dows Lake**
- **Fifth Avenue**
- **NAC**

Each simulated device sends JSON messages every **10 seconds** to **Azure IoT Hub**, where the data is later processed by Azure Stream Analytics, stored in Cosmos DB, archived in Blob Storage, and visualized in the dashboard application.

This repository is one of the three required project components.

---

## Features
- Simulates **three independent IoT devices**
- Sends telemetry every **10 seconds**
- Generates realistic values for:
  - Ice thickness (cm)
  - Surface temperature (°C)
  - Snow accumulation (cm)
  - External temperature (°C)
- Includes location of each device
- Sends messages to Azure IoT Hub using the Azure IoT Device SDK
- Fully configurable through environment variables

---

## Technologies Used
- **Python
- **Azure IoT Device SDK 
- **JSON** for message formatting

---

## Repository Structure
