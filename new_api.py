import requests
import time

WLED_IP = "192.168.0.179"  # Replace with the IP address of your WLED node
LED_INDEX = 44  # The index of the LED you want to turn on (0 for the first LED)
WAIT_TIME = 5  # The time to wait before reverting back to previous settings (in seconds)

def get_wled_state(ip):
    url = f"http://{ip}/json"
    response = requests.get(url)
    return response.json()

def set_wled_state(ip, state):
    url = f"http://{ip}/json/state"
    requests.post(url, json=state)

def send_request2(target_ip, start_num, stop_num, color):
    url = f"http://{target_ip}/json/state" # construct URL using the target IP address
    state = {"seg": [{"id": 0, "start": start_num, "stop": stop_num, "col": [color]}]}
    response = requests.post(url, json=state)

def send_request(target_ip, start_num, stop_num, color):
    url = f"http://{target_ip}/json/state" # construct URL using the target IP address
    state = {"seg": [{"id": 1, "start": start_num, "stop": stop_num, "col": [color]}]}
    response = requests.post(url, json=state)


def main():
    # Get the current WLED state
    current_state = get_wled_state(WLED_IP)

    # Turn off all LEDs
    off_state = {"on": False}
    #set_wled_state(WLED_IP, off_state)
    time.sleep(1)

    start_num = int(LED_INDEX) - 1
    send_request2(WLED_IP, 0, 64, [255, 0, 0])
    send_request(WLED_IP, start_num, int(LED_INDEX), [0, 255, 0])
    time.sleep(WAIT_TIME) # Change how long the LED stays on for.
    set_wled_state(WLED_IP, current_state["state"])

if __name__ == "__main__":
    main()
