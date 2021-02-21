'''
Train Number : 737.
Train Name : EGARO_SINDUR PROVATI
**************************************************
SCD

**************************************************

Train Number : 737.
Train Name : EGARO_SINDUR PROVATI
**************************************************
MNN

**************************************************

response0 = requests.post("https://www.esheba.cnsbd.com/v1/seat-availability", json={
            "train_no": '737.', "stn_from": 'BTPX', "stn_to": 'SCD, "journey_date": '2021-02-28'})
        js1 = response0.json()
        time.sleep(1)
        data1 = json.dumps(js1, indent=4)
        data2 = json.loads(data1)


'''
import requests
import json
import time
date = '2021-02-28'
from_station = 'BTPX'
to_station = 'BCI'

# response = requests.get(
#     "https://www.esheba.cnsbd.com/v1/trains?journey_date="+date+"&from_station="+from_station+"+&to_station="+to_station+"&class=S_CHAIR&adult=1&child=0")
# js = response.json()
# data0 = json.dumps(js, indent=4)
# data = json.loads(data0)
# train_no = data[0]['trn_no']
# # name of a train
# train_name = data[0]["trn_name"]
# routes = data[0]['routes']
# last_route_number = int(routes[-1]['sn']) - int(routes[0]['sn'])
# # printing station
# station_name = []
# for i in range(1, last_route_number+1):
#     station_name.append(routes[i]['int_stn'])
# print(train_name, train_no)
# print(station_name)

l = ['KJB', 'BCI', 'NRC', 'DABB', 'DA']
for i in l:
    response0 = requests.post("https://www.esheba.cnsbd.com/v1/seat-availability", json={
        "train_no": '782.', "stn_from": 'BTPX', "stn_to": i, "journey_date": date})
    js1 = response0.json()
    time.sleep(1)
    data1 = json.dumps(js1, indent=4)
    data2 = json.loads(data1)
    try:
        le = len(data2['DATA'])
        if le == 0:
            continue
        print(i)
        print()
        print("*"*50)
        for j in range(le):
            print()
            avail_seat0 = data2['DATA'][j]
            class0 = avail_seat0['CLASS']
            counter_Seat = avail_seat0['COUNTER_SEAT']
            online_seat = avail_seat0['MOBILE_SEAT']
            print(f"Class : {class0}")
            print(f"Online-Seat-Remaining : {online_seat}")
            print(f"Counter-Seat-Remaining : {counter_Seat}")
            print()
    except:
        pass
