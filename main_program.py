import time
import requests
import json


def stn_code_generator(name):
    station_code = [['AUP', 'ABDULPUR'], ['ACP', 'ACCALPUR'], ['AHG', 'AHASANGANG'], ['AKA', 'AKHAURA'], ['ADG', 'ALAMDANGA'], ['ASZ', 'ASHUGANJ'], ['AZPR', 'AZAMPUR'], ['BMSM', 'B SIRAJUL ISLAM'], ['BTPX', 'BAJITPUR'], ['BNNI', 'BANANI'], ['BBE', 'BBSETU_E'], ['BEN', 'BENAPOLE'], ['BCI', 'BHAIRAB_BAZAR'], ['BYM', 'BHAIRAMARA'], ['BXX', 'BHANUGACH'], ['DABB', 'BIMAN_BANDAR'], ['BARP', 'BIRAMPUR'], ['BNRP', 'BONAR_PARA'], ['BRBE', 'BORAL_BRIDGE'], ['BRSI', 'BORASHI'], ['BHRA', 'BRAHMAN_BARIA'], ['CDR', 'CHANDPUR'], ['CNBJ', 'CHAPAINABABGANJ'], ['CHPT', 'CHAPTA'], ['CMO', 'CHATMOHAR'], ['CLH', 'CHILAHATI'], ['CTG', 'CHITTAGONG'], ['CO', 'CHUADANGA'], ['CML', 'COMILLA'], ['KCPR', 'COURT CHANDPUR'], ['DSNH', 'DARSANA_HALT'], ['DACT', 'DA_CANTONMENT'], ['DWB', 'DEWANGANJ_BAZAR'], ['DA', 'DHAKA'], ['DGP', 'DINAJPUR'], ['FNI', 'FENI'], ['GFN', 'GAFARGAON'], ['GBH', 'GAIBANDHA'], ['GOBR', 'GOBRA'], ['GPLJ', 'GOPALGANJ'], ['GRPM', 'GOURIPUR_MYN'], ['GBI', 'GUNABOTI'], ['ISD', 'ISHURDI'], ['IPB', 'ISLAMPUR_BAZAR'], ['JLX', 'JAMALPUR_TOWN'], ['JYR', 'JAYDEBPUR'], ['JS', 'JESSORE'], ['JCG', 'JHIKARGACHA'], ['JY', 'JOYPURHAT'], ['KSNI', 'KASHIANI'], ['KLN', 'KHULNA'], ['KFJ', 'KISHOREGANJ'], ['KRF', 'KULAURA'], ['KJB', 'KULIARCHAR'], ['KRM', 'KURIGRAM'], ['LKM', 'LAKSAM'],
                    ['LMH', 'LALMONIR_HAT'], ['MIZ', 'MAIZGAON'], ['MNN', 'MANIK_KHALI'], ['MLDB', 'MELANDAH_BAZAR'], ['MGJN', 'MOHONGANJ'], ['MYN', 'MYMENSINGH'], ['NRC', 'NARSINGDI'], ['NTE', 'NATORE'], ['NOP', 'NAYAPARA'], ['NPA', 'NEELFAMARI'], ['NRQ', 'NETROKONA'], ['NKA', 'NOAKHALI'], ['PBT', 'PARBATIPUR'], ['PLB', 'PHULBARI'], ['PDB', 'PORADAHA'], ['QSBA', 'QOSBA'], ['RJHI', 'RAJSHAHI'], ['RJHC', 'RAJSHAHI COURT'], ['RNP', 'RANGPUR'], ['SDP', 'SAIDPUR'], ['STU', 'SANTAHER'], ['SCD', 'SARARCHAR'], ['SSI', 'SARISHA_BARI'], ['SMA', 'SH M MONSUR ALI'], ['SSJ', 'SHAISTAGONJ'], ['SJR', 'SHAMSHERNAGAR'], ['SRG', 'SRIMANGAL'], ['SYT', 'SYLHET'], ['TAGL', 'TANGAIL'], ['THRD', 'THAKURGAON_ROAD'], ['ULP', 'ULLAPARA']]
    valid_name_index = -1
    for i in station_code:
        valid_name_index += 1
        for j in i:
            if j == name:
                global stn_code
                stn_code = station_code[valid_name_index][0]
# ******************************************************************************


def stn_code_ge_reverse(name):
    station_code = [['AUP', 'ABDULPUR'], ['ACP', 'ACCALPUR'], ['AHG', 'AHASANGANG'], ['AKA', 'AKHAURA'], ['ADG', 'ALAMDANGA'], ['ASZ', 'ASHUGANJ'], ['AZPR', 'AZAMPUR'], ['BMSM', 'B SIRAJUL ISLAM'], ['BTPX', 'BAJITPUR'], ['BNNI', 'BANANI'], ['BBE', 'BBSETU_E'], ['BEN', 'BENAPOLE'], ['BCI', 'BHAIRAB_BAZAR'], ['BYM', 'BHAIRAMARA'], ['BXX', 'BHANUGACH'], ['DABB', 'BIMAN_BANDAR'], ['BARP', 'BIRAMPUR'], ['BNRP', 'BONAR_PARA'], ['BRBE', 'BORAL_BRIDGE'], ['BRSI', 'BORASHI'], ['BHRA', 'BRAHMAN_BARIA'], ['CDR', 'CHANDPUR'], ['CNBJ', 'CHAPAINABABGANJ'], ['CHPT', 'CHAPTA'], ['CMO', 'CHATMOHAR'], ['CLH', 'CHILAHATI'], ['CTG', 'CHITTAGONG'], ['CO', 'CHUADANGA'], ['CML', 'COMILLA'], ['KCPR', 'COURT CHANDPUR'], ['DSNH', 'DARSANA_HALT'], ['DACT', 'DA_CANTONMENT'], ['DWB', 'DEWANGANJ_BAZAR'], ['DA', 'DHAKA'], ['DGP', 'DINAJPUR'], ['FNI', 'FENI'], ['GFN', 'GAFARGAON'], ['GBH', 'GAIBANDHA'], ['GOBR', 'GOBRA'], ['GPLJ', 'GOPALGANJ'], ['GRPM', 'GOURIPUR_MYN'], ['GBI', 'GUNABOTI'], ['ISD', 'ISHURDI'], ['IPB', 'ISLAMPUR_BAZAR'], ['JLX', 'JAMALPUR_TOWN'], ['JYR', 'JAYDEBPUR'], ['JS', 'JESSORE'], ['JCG', 'JHIKARGACHA'], ['JY', 'JOYPURHAT'], ['KSNI', 'KASHIANI'], ['KLN', 'KHULNA'], ['KFJ', 'KISHOREGANJ'], ['KRF', 'KULAURA'], ['KJB', 'KULIARCHAR'], ['KRM', 'KURIGRAM'], ['LKM', 'LAKSAM'],
                    ['LMH', 'LALMONIR_HAT'], ['MIZ', 'MAIZGAON'], ['MNN', 'MANIK_KHALI'], ['MLDB', 'MELANDAH_BAZAR'], ['MGJN', 'MOHONGANJ'], ['MYN', 'MYMENSINGH'], ['NRC', 'NARSINGDI'], ['NTE', 'NATORE'], ['NOP', 'NAYAPARA'], ['NPA', 'NEELFAMARI'], ['NRQ', 'NETROKONA'], ['NKA', 'NOAKHALI'], ['PBT', 'PARBATIPUR'], ['PLB', 'PHULBARI'], ['PDB', 'PORADAHA'], ['QSBA', 'QOSBA'], ['RJHI', 'RAJSHAHI'], ['RJHC', 'RAJSHAHI COURT'], ['RNP', 'RANGPUR'], ['SDP', 'SAIDPUR'], ['STU', 'SANTAHER'], ['SCD', 'SARARCHAR'], ['SSI', 'SARISHA_BARI'], ['SMA', 'SH M MONSUR ALI'], ['SSJ', 'SHAISTAGONJ'], ['SJR', 'SHAMSHERNAGAR'], ['SRG', 'SRIMANGAL'], ['SYT', 'SYLHET'], ['TAGL', 'TANGAIL'], ['THRD', 'THAKURGAON_ROAD'], ['ULP', 'ULLAPARA']]
    valid_name_index = -1
    for i in station_code:
        valid_name_index += 1
        for j in i:
            if j == name:
                global stn_code_rev
                stn_code_rev = station_code[valid_name_index][1]
# useful link
# https://www.esheba.cnsbd.com/v1/trains?journey_date=2021-02-27&from_station=DA&to_station=BTPX&class=S_CHAIR&adult=1&child=0
# https://www.esheba.cnsbd.com/v1/seat-availability


try:# ---------------------------------------------------------------------------------------------------------------------------------------------
    # taking input
    from_station = input("From station: ").upper()
    fs = from_station
    to_station = input("To station: ").upper()

    date = input("Enter date in YYYY-MM-DD formate: ")
    stn_code_generator(from_station)
    from_station = stn_code
    stn_code_generator(to_station)
    to_station = stn_code
    stn_code = ''

    # ----------------------------------------------------------------------------------------------------------------------------------------------

    # making a requeset to load json
    response = requests.get(
        "https://www.esheba.cnsbd.com/v1/trains?journey_date="+date+"&from_station="+from_station+"+&to_station="+to_station+"&class=S_CHAIR&adult=1&child=0")
    js = response.json()
    data0 = json.dumps(js, indent=4)
    data = json.loads(data0)


    # received the request and processing data
    for i in range(len(data)):
        # train NO
        train_no = data[i]['trn_no']
        # name of a train
        train_name = data[i]["trn_name"]
        # Egaro Sindur Provati
        routes = data[i]['routes']
        print()

        # how many time the loop will occur
        last_route_number = int(routes[-1]['sn']) - int(routes[0]['sn'])
        # printing station
        station_name = []
        for i in range(last_route_number):
            station_name.append(routes[i]['int_stn'])
        # generating station code
        stn_code = ''
        stn_code_list = []
        s_e = ''
        for i in station_name:
            stn_code_generator(i)
            if stn_code != s_e:
                stn_code_list.append(stn_code)
                s_e = stn_code
        stn_code_list.append(to_station)
        s_C = stn_code_list[1:]

        # sending requests for seats
        # ***************************************************************************************************************
        for i in s_C:
            response0 = requests.post("https://www.esheba.cnsbd.com/v1/seat-availability", json={
                "train_no": train_no, "stn_from": from_station, "stn_to": i, "journey_date": date})
            js1 = response0.json()
            data1 = json.dumps(js1, indent=4)
            data2 = json.loads(data1)
            try:
                le = len(data2['DATA'])
                if le == 0:
                    continue
                stn_code_ge_reverse(i)
                k = stn_code_rev
                print(
                    f"- ----------------------------------From {fs} to {k} Available Tickets are-------------------------------------------")

                print(train_no, train_name)
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
        # ***************************************************************************************************************
 except:
    print("*"*50)
    print("Check Spellings/Date formate and try again..")
    print("*"*50)
