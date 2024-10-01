import network
import urequests
import utime

# Wi-Fi接続設定
# ssid = 'your_SSID'
# password = 'your_PASSWORD'

ssid = 'Buffalo-G-F5A0'
password = 'mck4wuvu7eypn'


wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, password)

while wlan.isconnected() == False:
    print('Connection status:', wlan.status())
    utime.sleep(1)

print('Connection successful')
print(wlan.ifconfig())

# データ送信
script_id =  "AKfycbyOVPdDRN0W4T8QkRIkMPSUbP0VS0Gzw-GnZhKu5caOE-hy5iWYRjJ-vdmTmN0MByJ9dA"
url = 'https://script.google.com/macros/s/AKfycbxnK12Gg8AhKuAGM8sMsu80XXcnzWo1UuPBtXTrrr9FjdzeSLGzEVF2Ah8o4PEwQIkoUQ/exec'
data = {'sensor_value': 123}

response = urequests.post(url, json=data)
print(response.text)
