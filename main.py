import os
import time
import requests

process_name = 'RobloxPlayerBeta.exe'

place_id = 142823291 # change to your game id 
webhook_url = '' # discord webhook

def is_running(process_name):
    return process_name.lower() in os.popen('tasklist').read().lower()

while True:
    if not is_running(process_name):
        if webhook_url:
            requests.post(webhook_url, json={'content': 'Roblox closed, reopening'})
        print('Roblox closed, reopening')
        os.system(f'start roblox://placeId={place_id}/')
        time.sleep(20)
    time.sleep(5)
