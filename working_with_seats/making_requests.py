# import requests
import json
# train_no = ["737.", "781.", "749."]

# for i in train_no:
#     print("*" * 50)
#     response = requests.post("https://www.esheba.cnsbd.com/v1/seat-availability", json={
#         "train_no": i, "stn_from": "DA", "stn_to": "KFJ", "journey_date": "2021-02-27"})
#     dik = json.dumps(response.json(), indent=4)

#     print(dik)
#     print("*" * 50)
#     print()

with open('working_with_seats/ticket_data.json') as f:
    data = json.load(f)
    f.close()

print(data)
