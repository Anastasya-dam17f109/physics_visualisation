import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime



files_list = [
"C:/Users/ADostovalova/Desktop/work/data_phys/data_16_11_2033/2023_TS/omni_min_def_20230401_20230630_fix.lst",

"C:/Users/ADostovalova/Desktop/work/data_phys/data_16_11_2033/2023_TS/omni_min_def_20231001_20231010.lst",
"C:/Users/ADostovalova/Desktop/work/data_phys/data_16_11_2033/2023_TS/omni_min_def_20230101_20230331.lst",

"C:/Users/ADostovalova/Desktop/work/data_phys/data_16_11_2033/2023_TS/omni_min_def_20230701_20230930.lst",
]

fix = False
if fix:
    with open("C:/Users/ADostovalova/Desktop/work/data_phys/data_16_11_2033/2023_TS/omni_min_def_20230401_20230630_fix.lst", "w") as fix_file:
        with open(
            "C:/Users/ADostovalova/Desktop/work/data_phys/data_16_11_2033/2023_TS/omni_min_def_20230401_20230630.lst",
            "r") as source_file:
            for line in source_file:
                ch_list = list(filter(None, line.split(" ")))

                ch_list = [line1.rstrip() for line1 in ch_list]
                ch_list = list(filter(None, ch_list))
                ch_list[1] = str(int(ch_list[1]) + 90)
                fix_file.write(" ".join(ch_list)+ "\n")

csv_head = "Timestamp;BX;BY;BZ;Vx;Vy;Vz;SYM_D;SYM_H;ASY_D;ASY_H\n"
#csv version
with open("C:/Users/ADostovalova/Desktop/work/data_phys/2023_data.csv", "w") as data_full:
    data_full.write(csv_head)
    for _file in files_list:

        with open(_file, "r") as data_file:
            for line in data_file:

                ch_list = list(filter(None, line.split(" ")))

                ch_list = [line1.rstrip() for line1 in ch_list]
                ch_list = list(filter(None, ch_list))
                #ch_list_num = [int(ch_list[i]) for i in range(4)]
                # заменяем значения  пропусков на none
                ch_list_num =[float(ch_list[i]) for i in range(4, len(ch_list))]
                for i in range(len(ch_list_num)):
                    if ch_list_num[i] == 99999.9 or ch_list_num[i] == 9999.99 or ch_list_num[i] == 999.99 or \
                            ch_list_num[i] == 99.99:
                        ch_list_num[i] = ""
                    else:
                        ch_list_num[i] = str(ch_list_num[i])
                #print(ch_list_num)
                time_meas = datetime.strptime(ch_list[0] + ':' + ch_list[1] + ":" + ch_list[2] +":"+ch_list[3], "%Y:%j:%H:%M")
                data_full.write(time_meas.strftime("%Y-%m-%d:%H:%M:%S:%f") + ";" + ";".join(ch_list_num) + "\n")
