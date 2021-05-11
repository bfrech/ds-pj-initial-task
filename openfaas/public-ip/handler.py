import requests
import sys 
import json

def handle(req):
    
    r = requests.get("https://api.ipify.org/?format=json")
    if r.status_code != 200:
        sys.exit("Sorry, there was an error with your request. Expected: %d, got: %d\n" %(200, r.status_code))
    
    res = r.json()
    ip = res["ip"]

    return json.dumps({"IP": ip})
