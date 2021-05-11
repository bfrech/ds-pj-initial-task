import requests
import sys

def handle(req):
    
    r = requests.get("http://" + "gateway.openfaas" + ":8080/function/public-ip")
    if r.status_code != 200:
        sys.exit("Sorry, there was an error with your request. Expected: %d, got: %d\n" %(200, r.status_code))
    
    res = r.json()
    ip = res["IP"]

    r2 = requests.get("http://" + "gateway.openfaas" + ":8080/function/location", data= ip)
    if r2.status_code != 200:
        sys.exit("Sorry, there was an error with your 2nd request. Expected: %d, got: %d\n" %(200, r.status_code))
    
    result = r2.json()

    return result["City"]

