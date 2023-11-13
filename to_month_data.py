import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime



files_list = [
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230422T000000_20230422T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230423T000000_20230423T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230424T000000_20230424T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230425T000000_20230425T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230426T000000_20230426T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230427T000000_20230427T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230428T000000_20230428T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230429T000000_20230429T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230430T000000_20230430T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230401T000000_20230401T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230402T000000_20230402T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230403T000000_20230403T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230404T000000_20230404T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230405T000000_20230405T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230406T000000_20230406T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230407T000000_20230407T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230408T000000_20230408T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230409T000000_20230409T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230410T000000_20230410T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230411T000000_20230411T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230412T000000_20230412T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230413T000000_20230413T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230414T000000_20230414T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230415T000000_20230415T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230416T000000_20230416T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230417T000000_20230417T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230418T000000_20230418T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230419T000000_20230419T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230420T000000_20230420T235959_0101.txt",
"C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230421T000000_20230421T235959_0101.txt"
]

'''
with open("C:/Users/ADostovalova/Desktop/work/data_phys/202304_dates.txt", "w") as date_file , open("C:/Users/ADostovalova/Desktop/work/data_phys/202304_measurements.txt", "w") as measurements_file:
    for _file in files_list :
        counter = 0
        with open( _file, "r") as data_file:
            for line in data_file:
                if counter>3:
                    ch_list = list(filter(None, line.split(" ")))
                    ch_list = [line1.rstrip() for line1 in ch_list]
                    ch_list = list(filter(None, ch_list))
                    #print(ch_list)


                    date_file.write(ch_list[1] + ':' + ch_list[2] + "\n")
                    measurements_file.write(" ".join(ch_list[3:]) + "\n")
                counter+=1
#число dht в окне

'''
csv_head = "Timestamp;Latitude;Longitude;Height;Radius;SZA;SAz;ST;Diplat;Diplon;MLat;MLT;AACGMLat;AACGMLon;n;Te_hgn;Te_lgn;T_elec;Vs_hgn;Vs_lgn;U_SC\n"
#csv version
with open("C:/Users/ADostovalova/Desktop/work/data_phys/202304_data.csv", "w") as data_full:
    data_full.write(csv_head)
    for _file in files_list:
        counter = 0
        with open(_file, "r") as data_file:
            for line in data_file:
                if counter > 3:
                    ch_list = list(filter(None, line.split(" ")))

                    ch_list = [line1.rstrip() for line1 in ch_list]
                    ch_list = list(filter(None, ch_list))
                    ch_list[1] = ch_list[1].replace("-23", "-2023")
                    full_t, ms_t = ch_list[2].split(".")
                    ms_t = int(ms_t) * 1000
                    # print(ch_list)
                    time_meas = datetime.strptime(ch_list[1] + ':' + full_t + ":" + str(ms_t),"%d-%m-%Y:%H:%M:%S:%f" )
                    #print(time_meas)


                    #data_full.write(ch_list[1] + ':' + ch_list[2] + "\n")
                    data_full.write( time_meas.strftime("%Y-%m-%d:%H:%M:%S:%f")+";"+ ";".join(ch_list[3:]) + "\n")
                counter += 1


count =0

with open("C:/Users/ADostovalova/Desktop/work/data_phys/202304_data.csv", "r") as data_full:
    for l in data_full:
        if  count < 10:
            print(l)
            count +=1