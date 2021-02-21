import json
import requests
import time

# with open('working_with_seats/ticket_data.json') as f:
#     data = json.load(f)
#     f.close()
train = ['DABB', 'NRC', 'BCI', 'KJB', 'BTPX', 'SCD', 'KFJ']

for i in train:
    print(i)
    print("*"*50)
    response0 = requests.post("https://www.esheba.cnsbd.com/v1/seat-availability", json={
        "train_no": "737.", "stn_from": "DA", "stn_to": i, "journey_date": "2021-02-27"})
    js1 = response0.json()
    time.sleep(1)
    data1 = json.dumps(js1, indent=4)
    data2 = json.loads(data1)

    try:
        le = len(data2['DATA'])
        # print(le)
        print()
        print("*"*50)
        for i in range(le):
            print()
            avail_seat0 = data2['DATA'][i]
            class0 = avail_seat0['CLASS']
            counter_Seat = avail_seat0['COUNTER_SEAT']
            online_seat = avail_seat0['MOBILE_SEAT']
            print(f"Class : {class0}")
            print(f"Online-Seat-Remaining : {online_seat}")
            print(f"Counter-Seat-Remaining : {counter_Seat}")
            print()
    except:
        pass
