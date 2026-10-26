tesla_bot_config = {
     "bot_name": "Tesla-Naitik-V2",
     "is_online": True,
     "battery_percent": 35.5,
     "danger_senser_packet": b"overheat",
     "motors_speed": [40, 50, 60]
} 

# 1. Yahan humne dictionary ke andar se values ko sahi se check kiya hai
if tesla_bot_config["is_online"] is True and tesla_bot_config["danger_senser_packet"] == b"overheat":
     
     # 2. Print se pehle 'f' lagaya aur dictionary ki keys ko {} ke andar dala
     print(f"Warning ! {tesla_bot_config['bot_name']} is overheating! reducing speed to {tesla_bot_config['motors_speed']}")

else:
     print('Robot running perfectly')


 

    