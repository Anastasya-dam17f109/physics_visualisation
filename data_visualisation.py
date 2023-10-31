import matplotlib.pyplot as plt
import numpy as np
import datetime




class data_visualiser:
    def __init__(self, file_meta, file_data, work_dir):
        self.filename = file_data
        self.meta_data = file_meta
        self.data_mass = []
        self.time_mass = []
        self.value_mass = []
        self.work_dir = work_dir
        self.date = "it does not matter"
        self.char_amount = 0
    def print_window_data(self, split_num, window,start,char_num):
        self.data_mass = []
        self.time_mass = []
        self.value_mass = []
        left_bound = datetime.datetime(100, 1, 1, 0, 0, 0)
        for i in range(24*60*60):
            self.time_mass.append(str(left_bound.time()) + ".197")
            self.time_mass.append(str(left_bound.time()) + ".696")
            left_bound = left_bound + datetime.timedelta(0, 1)
        self.data_mass = [None for i in range(24*60*60*2)]
        with open(self.filename, "r") as data_file:
            for line in data_file:

                ch_list = list(filter(None, line.split(" ")))
                ch_list = [line1.rstrip() for line1 in ch_list]
                ch_list = list(filter(None, ch_list))

                self.char_amount = len(ch_list) - 3
                self.date = ch_list[1]
                if ch_list[2] in self.time_mass:
                    ch_list_num = float(ch_list[3 + char_num])#float(ch_list[i]) for i in range(3, len(ch_list))]
                    self.data_mass[self.time_mass.index(ch_list[2])] = ch_list_num




                # заменяем значения  пропусков на none
                #ch_list_num = ch_list_num + [float(ch_list[i]) for i in range(4, len(ch_list))]

                #self.data_mass.append(ch_list_num)
            data_file.close()
            print("data was read")

           # собираем значения временного ряда для выбраннойхарактеристики в один массив

            self.value_mass = self.data_mass[start: start + window]
            self.plot_time_mass = self.time_mass[start: start + window]


            #print("collected")
            fig, axs = [], []
            len_fragm = len(self.plot_time_mass) // split_num
            for i in range(split_num):
                figb, axsb = plt.subplots(nrows=1, ncols=1)
                fig.append(figb)
                axs.append(axsb)
                axs[i].plot(self.plot_time_mass[i*len_fragm : (i+1)*len_fragm], self.value_mass[i*len_fragm : (i+1)*len_fragm], color="blue")
                axs[i].set_title(self.date)
                for index, label in enumerate(axs[i].xaxis.get_ticklabels()):
                    if index % 12000 != 0:
                        label.set_visible(False)
            plt.show()

    def print_window_data_by_mounth(self, split_num, window,start,char_num):
        self.data_mass = []
        self.time_mass = []
        self.value_mass = []
        ch = np.loadtxt("C:/Users/ADostovalova/Desktop/work/data_phys/202304_measurements.txt", dtype= "float32")
        print("measures load")
        dict_idx = {}
        left_bound = datetime.datetime(2023, 4, 1, 0, 0, 0)
        counter = 0
        for i in range(24*60*60*30):
            self.time_mass.append(str(left_bound) + ".197")
            self.time_mass.append(str(left_bound) + ".696")
            dict_idx.update({str(left_bound).replace(" ",":") + ".197": counter})
            dict_idx.update({str(left_bound).replace(" ",":") + ".696": counter+1})
            left_bound = left_bound + datetime.timedelta(0, 1)
            counter += 1
        print("time set")
        print(dict_idx)
        counter = 0
        self.data_mass = [None for i in range(24 * 60 * 60 * 2 * 30)]
        with open("C:/Users/ADostovalova/Desktop/work/data_phys/202304_dates.txt", "r") as date_file:
            for line in date_file:
                line = line.rstrip()
                print(line)
                self.data_mass[dict_idx.get(line)] = ch[counter,char_num]
                dict_idx.update({line:counter})
                counter +=1
        print("time load")


        print(self.data_mass)

        '''
        for i in range(24 * 60 * 60 * 30 * 2):
        self.data_mass = [None for i in range(24*60*60*2*30)]
        with open(self.filename, "r") as data_file:
            for line in data_file:

                ch_list = list(filter(None, line.split(" ")))
                ch_list = [line1.rstrip() for line1 in ch_list]
                ch_list = list(filter(None, ch_list))

                self.char_amount = len(ch_list) - 3
                self.date = ch_list[1]
                if ch_list[2] in self.time_mass:
                    ch_list_num = float(ch_list[3 + char_num])#float(ch_list[i]) for i in range(3, len(ch_list))]
                    self.data_mass[self.time_mass.index(ch_list[2])] = ch_list_num




                # заменяем значения  пропусков на none
                #ch_list_num = ch_list_num + [float(ch_list[i]) for i in range(4, len(ch_list))]

                #self.data_mass.append(ch_list_num)
            data_file.close()
            print("data was read")

           # собираем значения временного ряда для выбраннойхарактеристики в один массив

            self.value_mass = self.data_mass[start: start + window]
            self.plot_time_mass = self.time_mass[start: start + window]


            #print("collected")
            fig, axs = [], []
            len_fragm = len(self.plot_time_mass) // split_num
            for i in range(split_num):
                figb, axsb = plt.subplots(nrows=1, ncols=1)
                fig.append(figb)
                axs.append(axsb)
                axs[i].plot(self.plot_time_mass[i*len_fragm : (i+1)*len_fragm], self.value_mass[i*len_fragm : (i+1)*len_fragm], color="blue")
                axs[i].set_title(self.date)
                for index, label in enumerate(axs[i].xaxis.get_ticklabels()):
                    if index % 12000 != 0:
                        label.set_visible(False)
            plt.show()
            '''


    def print_hist_holes(self):
        fig, axs = plt.subplots(nrows=1, ncols=1)
        holes = []
        count = 0
        if self.value_mass[0] == None:
            count += 1
        for i in range(1, len(self.value_mass)):
            if self.value_mass[i] == None:
                count += 1
            else:
                if self.value_mass[i - 1] == None:
                    holes.append(count)
                    count = 0
        # убираем хвост гистограммы, если мешает
        new_holes = []
        for i in holes:
            if i < 30:
                new_holes.append(i)

        a = list(set(holes))
        res = np.zeros(len(a), dtype=int)
        for i in holes:
            res[a.index(i)] += 1
        d = {}
        for i in range(len(a)):
            d.update({a[i]: res[i]})

        with open(self.work_dir + "/labels.txt", "w") as write_file:
            for k, v in d.items():
                write_file.write(str(k) + ":" + str(v) + "\n")

        axs.hist(new_holes)
        plt.show()


#число dht в окне
window = 24*60*60

start = 24*60*60-1
char_num = 8

dv = data_visualiser("C:/Users/ADostovalova/Downloads/Telegram Desktop/omni_min_2023.fmt",
                     "C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230401T000000_20230401T235959_0101.txt",
                     "C:/Users/ADostovalova/Desktop/work/data_phys")
dv.print_window_data_by_mounth(3, window,start,char_num)

dv.print_hist_holes()



