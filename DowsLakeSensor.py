import time
import random
import json
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=snowsensors.azure-devices.net;DeviceId=DowsLake;*****************"

def get_telemetry():
    return {
        "location":"DownsLake",
        "ice_thickness_cm": random.uniform(20.0, 150.0),
        "surface_temperature_c": random.uniform(-35.0, 5.0),
        "snow_accumulation_cm": random.uniform(0.0, 150.0),
        "external_temperature_c": random.uniform(-45.0, 10.0)
    }

def main():
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    print("Sending telemetry to IoT Hub...")
    
    try:
        while True:
            telemetry = get_telemetry()

            message = Message(json.dumps(telemetry))
            client.send_message(message)

            print(f"Sent message: {telemetry}")

            time.sleep(10)

    except KeyboardInterrupt:
        print("Stopped sending messages.")

    finally:
        client.disconnect()

if __name__ == "__main__":
    main()
