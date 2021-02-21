# # working with station code
stn_code = ''


# def stn_code_generator(name):
#     station_code = [['AUP', 'ABDULPUR'], ['ACP', 'ACCALPUR'], ['AHG', 'AHASANGANG'], ['AKA', 'AKHAURA'], ['ADG', 'ALAMDANGA'], ['ASZ', 'ASHUGANJ'], ['AZPR', 'AZAMPUR'], ['BMSM', 'B SIRAJUL ISLAM'], ['BTPX', 'BAJITPUR'], ['BNNI', 'BANANI'], ['BBE', 'BBSETU_E'], ['BEN', 'BENAPOLE'], ['BCI', 'BHAIRAB_BAZAR'], ['BYM', 'BHAIRAMARA'], ['BXX', 'BHANUGACH'], ['DABB', 'BIMAN_BANDAR'], ['BARP', 'BIRAMPUR'], ['BNRP', 'BONAR_PARA'], ['BRBE', 'BORAL_BRIDGE'], ['BRSI', 'BORASHI'], ['BHRA', 'BRAHMAN_BARIA'], ['CDR', 'CHANDPUR'], ['CNBJ', 'CHAPAINABABGANJ'], ['CHPT', 'CHAPTA'], ['CMO', 'CHATMOHAR'], ['CLH', 'CHILAHATI'], ['CTG', 'CHITTAGONG'], ['CO', 'CHUADANGA'], ['CML', 'COMILLA'], ['KCPR', 'COURT CHANDPUR'], ['DSNH', 'DARSANA_HALT'], ['DACT', 'DA_CANTONMENT'], ['DWB', 'DEWANGANJ_BAZAR'], ['DA', 'DHAKA'], ['DGP', 'DINAJPUR'], ['FNI', 'FENI'], ['GFN', 'GAFARGAON'], ['GBH', 'GAIBANDHA'], ['GOBR', 'GOBRA'], ['GPLJ', 'GOPALGANJ'], ['GRPM', 'GOURIPUR_MYN'], ['GBI', 'GUNABOTI'], ['ISD', 'ISHURDI'], ['IPB', 'ISLAMPUR_BAZAR'], ['JLX', 'JAMALPUR_TOWN'], ['JYR', 'JAYDEBPUR'], ['JS', 'JESSORE'], ['JCG', 'JHIKARGACHA'], ['JY', 'JOYPURHAT'], ['KSNI', 'KASHIANI'], ['KLN', 'KHULNA'], ['KFJ', 'KISHOREGANJ'], ['KRF', 'KULAURA'], ['KJB', 'KULIARCHAR'], ['KRM', 'KURIGRAM'], ['LKM', 'LAKSAM'],
#                     ['LMH', 'LALMONIR_HAT'], ['MIZ', 'MAIZGAON'], ['MNN', 'MANIK_KHALI'], ['MLDB', 'MELANDAH_BAZAR'], ['MGJN', 'MOHONGANJ'], ['MYN', 'MYMENSINGH'], ['NRC', 'NARSINGDI'], ['NTE', 'NATORE'], ['NOP', 'NAYAPARA'], ['NPA', 'NEELFAMARI'], ['NRQ', 'NETROKONA'], ['NKA', 'NOAKHALI'], ['PBT', 'PARBATIPUR'], ['PLB', 'PHULBARI'], ['PDB', 'PORADAHA'], ['QSBA', 'QOSBA'], ['RJHI', 'RAJSHAHI'], ['RJHC', 'RAJSHAHI COURT'], ['RNP', 'RANGPUR'], ['SDP', 'SAIDPUR'], ['STU', 'SANTAHER'], ['SCD', 'SARARCHAR'], ['SSI', 'SARISHA_BARI'], ['SMA', 'SH M MONSUR ALI'], ['SSJ', 'SHAISTAGONJ'], ['SJR', 'SHAMSHERNAGAR'], ['SRG', 'SRIMANGAL'], ['SYT', 'SYLHET'], ['TAGL', 'TANGAIL'], ['THRD', 'THAKURGAON_ROAD'], ['ULP', 'ULLAPARA']]
#     valid_name_index = -1
#     for i in station_code:
#         valid_name_index += 1
#         for j in i:
#             print(j)
#             if j == name:
#                 global stn_code
#                 stn_code = station_code[valid_name_index][0]


# train_route = ['DHAKA', 'BIMAN_BANDAR', 'NARSINGDI', 'BHAIRAB_BAZAR', 'KULIARCHAR',
#                'BAJITPUR', 'SARARCHAR', 'MANIK_KHALI', 'GACHIHATA', 'KISHOREGANJ']


# # for i in train_route:
# #     stn_code_generator(i)
# #     # print(stn_code)
# #     stn_code = ''

def stn_code_ge_reverse(name):
    station_code = [['AUP', 'ABDULPUR'], ['ACP', 'ACCALPUR'], ['AHG', 'AHASANGANG'], ['AKA', 'AKHAURA'], ['ADG', 'ALAMDANGA'], ['ASZ', 'ASHUGANJ'], ['AZPR', 'AZAMPUR'], ['BMSM', 'B SIRAJUL ISLAM'], ['BTPX', 'BAJITPUR'], ['BNNI', 'BANANI'], ['BBE', 'BBSETU_E'], ['BEN', 'BENAPOLE'], ['BCI', 'BHAIRAB_BAZAR'], ['BYM', 'BHAIRAMARA'], ['BXX', 'BHANUGACH'], ['DABB', 'BIMAN_BANDAR'], ['BARP', 'BIRAMPUR'], ['BNRP', 'BONAR_PARA'], ['BRBE', 'BORAL_BRIDGE'], ['BRSI', 'BORASHI'], ['BHRA', 'BRAHMAN_BARIA'], ['CDR', 'CHANDPUR'], ['CNBJ', 'CHAPAINABABGANJ'], ['CHPT', 'CHAPTA'], ['CMO', 'CHATMOHAR'], ['CLH', 'CHILAHATI'], ['CTG', 'CHITTAGONG'], ['CO', 'CHUADANGA'], ['CML', 'COMILLA'], ['KCPR', 'COURT CHANDPUR'], ['DSNH', 'DARSANA_HALT'], ['DACT', 'DA_CANTONMENT'], ['DWB', 'DEWANGANJ_BAZAR'], ['DA', 'DHAKA'], ['DGP', 'DINAJPUR'], ['FNI', 'FENI'], ['GFN', 'GAFARGAON'], ['GBH', 'GAIBANDHA'], ['GOBR', 'GOBRA'], ['GPLJ', 'GOPALGANJ'], ['GRPM', 'GOURIPUR_MYN'], ['GBI', 'GUNABOTI'], ['ISD', 'ISHURDI'], ['IPB', 'ISLAMPUR_BAZAR'], ['JLX', 'JAMALPUR_TOWN'], ['JYR', 'JAYDEBPUR'], ['JS', 'JESSORE'], ['JCG', 'JHIKARGACHA'], ['JY', 'JOYPURHAT'], ['KSNI', 'KASHIANI'], ['KLN', 'KHULNA'], ['KFJ', 'KISHOREGANJ'], ['KRF', 'KULAURA'], ['KJB', 'KULIARCHAR'], ['KRM', 'KURIGRAM'], ['LKM', 'LAKSAM'],
                    ['LMH', 'LALMONIR_HAT'], ['MIZ', 'MAIZGAON'], ['MNN', 'MANIK_KHALI'], ['MLDB', 'MELANDAH_BAZAR'], ['MGJN', 'MOHONGANJ'], ['MYN', 'MYMENSINGH'], ['NRC', 'NARSINGDI'], ['NTE', 'NATORE'], ['NOP', 'NAYAPARA'], ['NPA', 'NEELFAMARI'], ['NRQ', 'NETROKONA'], ['NKA', 'NOAKHALI'], ['PBT', 'PARBATIPUR'], ['PLB', 'PHULBARI'], ['PDB', 'PORADAHA'], ['QSBA', 'QOSBA'], ['RJHI', 'RAJSHAHI'], ['RJHC', 'RAJSHAHI COURT'], ['RNP', 'RANGPUR'], ['SDP', 'SAIDPUR'], ['STU', 'SANTAHER'], ['SCD', 'SARARCHAR'], ['SSI', 'SARISHA_BARI'], ['SMA', 'SH M MONSUR ALI'], ['SSJ', 'SHAISTAGONJ'], ['SJR', 'SHAMSHERNAGAR'], ['SRG', 'SRIMANGAL'], ['SYT', 'SYLHET'], ['TAGL', 'TANGAIL'], ['THRD', 'THAKURGAON_ROAD'], ['ULP', 'ULLAPARA']]
    valid_name_index = -1
    for i in station_code:
        valid_name_index += 1
        for j in i:
            if j == name:
                global stn_code_var
                stn_code_var = station_code[valid_name_index][1]


code = ['LMH', 'AHG', 'BTPX']
stn_code_list = []
s_e = ''
for i in code:
    stn_code_ge_reverse(i)
    if stn_code_var != s_e:
        stn_code_list.append(stn_code_var)
        s_e = stn_code_var
print(stn_code_list)
