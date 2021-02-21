import json
import requests
response = requests.get(
    "https://www.esheba.cnsbd.com/v1/trains?journey_date=2021-02-27&from_station=DA&to_station=KFJ&class=S_CHAIR&adult=1&child=0")
js = response.json()
dic = json.dumps(js, indent=4)
print(dic)
