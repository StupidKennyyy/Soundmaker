from time import sleep
from datetime import datetime
import json
from queue import Queue

def CheckTime(msg_queue: Queue):
    while True:
        try:
            current_date = datetime.now()
            current_time = current_date.strftime("%H:%M")
            current_day = current_date.strftime("%A")

            with open("graafik.json", "r") as f:
                graafik = json.load(f)
            
            found_match = False
            for action in graafik:
                if action["time"] == current_time and current_day in action["days"]:
                    print(f"Found action {action["action"]}")
                    msg_queue.put(action["action"])
                    found_match = True
                    break
            if found_match:
                sleep(61)
            else:
                sleep(10)

        except FileNotFoundError:
            print("Viga: graafik.json faili ei leitud!")
            sleep(30) # Oota enne uut proovimist
        except json.JSONDecodeError:
            print("Viga: JSON fail on vigane (võib-olla tühi või pooleli salvestamine).")
            sleep(5)
        except Exception as e:
            print(f"Ootamatu viga: {e}")
            sleep(10)

            
