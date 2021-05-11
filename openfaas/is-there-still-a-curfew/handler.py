import requests
import sys

def handle(req):
    r = requests.get("https://api.corona-zahlen.org/states/BE/history/incidence/5")
    if r.status_code != 200:
        sys.exit("Sorry, there was an error with your request. Expected: %d, got: %d\n" %(200, r.status_code))
    
    res = r.json()
    history = res['data']['BE']['history']
    curfew = any(day["weekIncidence"] >= 100 for day in history)

    if curfew:
        return "Yes we are still on curfew"
    else:
        return "No you can stay out late tonight"