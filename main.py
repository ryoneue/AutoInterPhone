import network
import json
import utime
import urequests
# from ulab import numpy as np

def json_extract(json_path):
    with open(json_path, "r") as file:
        json_data = json.load(file)
    ssid = json_data["wifi"]["ssid"]
    password = json_data["wifi"]["password"]
    gas_url = json_data["GAS"]["url"]
    return ssid, password, gas_url

def wifi_connect(ssid, password):
    

    
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while wlan.isconnected() == False:
        print('Connection status:', wlan.status())
        utime.sleep(1)

    print('Connection successful')
    print(wlan.ifconfig())
    return wlan

def pico2gas(wlan, gas_url, sound_data=None):
    if not wlan.isconnected:
        return "ERR"
    data = {'sensor_values': list(range(1,1024))}
    response = urequests.post(gas_url, json=data)
    print(response.text)

if __name__ == '__main__':
    json_path = "./setting.json"
    ssid, password, gas_url = json_extract(json_path)
    wlan = wifi_connect(ssid, password)
    pico2gas(wlan,gas_url)