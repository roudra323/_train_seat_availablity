import json
import requests
# with open('train_list.json') as f:
#     data = json.load(f)
#     f.close()
response = requests.get(
    "https://www.esheba.cnsbd.com/v1/trains?journey_date=2021-02-27&from_station=DA&to_station=KFJ&class=S_CHAIR&adult=1&child=0")
js = response.json()
data0 = json.dumps(js, indent=4)
data = json.loads(data0)
print(data[0]['trn_no'])
# for i in range(len(data)):
#     # train NO
#     train_no = data[i]['trn_no']
#     # name of a train
#     train_name = data[i]["trn_name"]
#     # Egaro Sindur Provati
#     routes = data[i]['routes']
#     # how many time the loop will occur
#     last_route_number = int(routes[-1]['sn'])
#     # printing station
#     station_name = []
#     for i in range(last_route_number):
#         station_name.append(routes[i]['int_stn'])
#     print(train_no, train_name)
#     print(station_name)
#     print("*" * 20)
