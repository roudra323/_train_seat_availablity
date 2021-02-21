import json
import requests
response2 = requests.get("https://www.esheba.cnsbd.com/v1/from-stations")
js = response2.json()
dic2 = json.dumps(js, indent=4)
print(dic2)
