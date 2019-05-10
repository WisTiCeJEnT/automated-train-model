from practicum import find_mcu_boards, McuBoard, PeriBoard
from time import sleep
import requests
import json

LTH = 800
URL = "http://127.0.0.1:5000/station"

def is_here(ldr_status):
    if (ldr_status > LTH):
        return '0'
    return '1'

def position(ldr_light):
    return is_here(ldr_light[0])+is_here(ldr_light[1])+is_here(ldr_light[2])+is_here(ldr_light[3])

def poster(payload):
    try:
        headers = {'content-type': 'application/json'}
        response = requests.post(URL, data=json.dumps(payload), headers=headers)
        print(response.json())
        return(response.json())
        
    except:
        print("fail to connect to server")

devs = find_mcu_boards()

if len(devs) == 0:
    print("*** No practicum board found.")
    exit(1)

mcu = McuBoard(devs[0])
print("*** Practicum board found")
print("*** Manufacturer: %s" % \
        mcu.handle.getString(mcu.device.iManufacturer, 256))
print("*** Product: %s" % \
        mcu.handle.getString(mcu.device.iProduct, 256))
peri = PeriBoard(mcu)

count = 0
while True:
    #peri.set_led_value(count)
    light = peri.get_light()

    print(light)
    res = poster({"train_position": position(light)})
    payload = 0
    if res["traffic_signal"][0]:
        payload += 1
    if res["traffic_signal"][1]:
        payload += 2
    if res["traffic_signal"][2]:
        payload += 4
    peri.set_signal_light(value = int(payload))
    sleep(0.25)
