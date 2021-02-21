import requests
import json


response0 = requests.post("https://www.esheba.cnsbd.com/v1/seat-availability", json={
                          "train_no": "737.", "stn_from": "DA", "stn_to": "DABB", "journey_date": "2021-02-27"})
js1 = response0.json()
data1 = json.dumps(js1, indent=4)
data2 = json.loads(data1)

stats = data2['STATUS']['CODE']
if stats != 1:
    print(data2['STATUS']['msg'])
