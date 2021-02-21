def stn_code_generator(name):
    stn_code_list = []
    station_code = [['AUP', 'ABDULPUR'], ['ACP', 'ACCALPUR'], ['AHG', 'AHASANGANG'], ['AKA', 'AKHAURA'], ['ADG', 'ALAMDANGA'], ['ASZ', 'ASHUGANJ'], ['AZPR', 'AZAMPUR'], ['BMSM', 'B SIRAJUL ISLAM'], ['BTPX', 'BAJITPUR'], ['BNNI', 'BANANI'], ['BBE', 'BBSETU_E'], ['BEN', 'BENAPOLE'], ['BCI', 'BHAIRAB_BAZAR'], ['BYM', 'BHAIRAMARA'], ['BXX', 'BHANUGACH'], ['DABB', 'BIMAN_BANDAR'], ['BARP', 'BIRAMPUR'], ['BNRP', 'BONAR_PARA'], ['BRBE', 'BORAL_BRIDGE'], ['BRSI', 'BORASHI'], ['BHRA', 'BRAHMAN_BARIA'], ['CDR', 'CHANDPUR'], ['CNBJ', 'CHAPAINABABGANJ'], ['CHPT', 'CHAPTA'], ['CMO', 'CHATMOHAR'], ['CLH', 'CHILAHATI'], ['CTG', 'CHITTAGONG'], ['CO', 'CHUADANGA'], ['CML', 'COMILLA'], ['KCPR', 'COURT CHANDPUR'], ['DSNH', 'DARSANA_HALT'], ['DACT', 'DA_CANTONMENT'], ['DWB', 'DEWANGANJ_BAZAR'], ['DA', 'DHAKA'], ['DGP', 'DINAJPUR'], ['FNI', 'FENI'], ['GFN', 'GAFARGAON'], ['GBH', 'GAIBANDHA'], ['GOBR', 'GOBRA'], ['GPLJ', 'GOPALGANJ'], ['GRPM', 'GOURIPUR_MYN'], ['GBI', 'GUNABOTI'], ['ISD', 'ISHURDI'], ['IPB', 'ISLAMPUR_BAZAR'], ['JLX', 'JAMALPUR_TOWN'], ['JYR', 'JAYDEBPUR'], ['JS', 'JESSORE'], ['JCG', 'JHIKARGACHA'], ['JY', 'JOYPURHAT'], ['KSNI', 'KASHIANI'], ['KLN', 'KHULNA'], ['KFJ', 'KISHOREGANJ'], ['KRF', 'KULAURA'], ['KJB', 'KULIARCHAR'], ['KRM', 'KURIGRAM'], ['LKM', 'LAKSAM'],
                    ['LMH', 'LALMONIR_HAT'], ['MIZ', 'MAIZGAON'], ['MLDB', 'MELANDAH_BAZAR'], ['MGJN', 'MOHONGANJ'], ['MYN', 'MYMENSINGH'], ['NRC', 'NARSINGDI'], ['NTE', 'NATORE'], ['NOP', 'NAYAPARA'], ['NPA', 'NEELFAMARI'], ['NRQ', 'NETROKONA'], ['NKA', 'NOAKHALI'], ['PBT', 'PARBATIPUR'], ['PLB', 'PHULBARI'], ['PDB', 'PORADAHA'], ['QSBA', 'QOSBA'], ['RJHI', 'RAJSHAHI'], ['RJHC', 'RAJSHAHI COURT'], ['RNP', 'RANGPUR'], ['SDP', 'SAIDPUR'], ['STU', 'SANTAHER'], ['SCD', 'SARARCHAR'], ['SSI', 'SARISHA_BARI'], ['SMA', 'SH M MONSUR ALI'], ['SSJ', 'SHAISTAGONJ'], ['SJR', 'SHAMSHERNAGAR'], ['SRG', 'SRIMANGAL'], ['SYT', 'SYLHET'], ['TAGL', 'TANGAIL'], ['THRD', 'THAKURGAON_ROAD'], ['ULP', 'ULLAPARA']]
    valid_name_index = -1
    for i in station_code:
        valid_name_index += 1
        for j in i:
            if j == name:
                stn_code = station_code[valid_name_index][0]
                stn_code_list.append(stn_code)
    return stn_code_list
