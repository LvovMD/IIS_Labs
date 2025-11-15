import requests
import time
import random

for i in range(50):
    params = {'item_id': i}
    data = {
        "blue": random.randint(0,1),
        "dual_sim": random.randint(0,1),
        "four_g": random.randint(0,1),
        "three_g": random.randint(0,1),
        "touch_screen": random.randint(0,1),
        "wifi": random.randint(0,1),
        "battery_power": random.randint(500,1998),
        "clock_speed": 0.5*random.randint(1,6.0),
        "fc": random.randint(0,19),
        "int_memory": random.randint(2,64),
        "m_dep": 0.1*random.randint(1,100),
        "mobile_wt": random.randint(80,200),
        "n_cores": random.randint(1,8),
        "pc": random.randint(0,20),
        "px_height": random.randint(0,1960),
        "px_width": random.randint(500,1998),
        "ram": random.randint(256,3998),
        "sc_h": random.randint(5,19),
        "sc_w": random.randint(0,19),
        "talk_time": random.randint(2,20)
        }

    response = requests.post('http://price_predict:8000/api/prediction', params=params, json=data)
    time.sleep(random.randint(1,5))
    print(response.json())