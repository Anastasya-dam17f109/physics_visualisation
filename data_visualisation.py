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
    def print_window_data(self, split_num, window,start,char_num):
        self.data_mass = []
        self.time_mass = []
        self.value_mass = []
        with open(self.filename, "r") as data_file:
            for line in data_file:
                ch_list = list(filter(None, line.split(" ")))
                ch_list = [line1.rstrip() for line1 in ch_list]
                ch_list_num = [int(ch_list[i]) for i in range(4)]
                # заменяем значения  пропусков на none
                ch_list_num = ch_list_num + [float(ch_list[i]) for i in range(4, len(ch_list))]
                for i in range(len(ch_list_num)):
                    if ch_list_num[i] == 99999.9 or ch_list_num[i] == 9999.99 or ch_list_num[i] == 999.99 or \
                            ch_list_num[i] == 99.99:
                        ch_list_num[i] = None
                self.data_mass.append(ch_list_num)
            data_file.close()
            #print("read")
           # собираем значения временного ряда для выбраннойхарактеристики в один массив
            for l_mass in self.data_mass:

                if l_mass[1] >= start and l_mass[1] < start + window:
                    self.time_mass.append(str(l_mass[1]) + ": " + str(datetime.time(l_mass[2], l_mass[3], 0)))
                    self.value_mass.append(l_mass[4 + char_num])
            #print("collected")
            fig, axs = [], []
            len_fragm = len(self.time_mass) // split_num
            for i in range(split_num):
                figb, axsb = plt.subplots(nrows=1, ncols=1)
                fig.append(figb)
                axs.append(axsb)
                axs[i].plot(self.time_mass[i*len_fragm : (i+1)*len_fragm], self.value_mass[i*len_fragm : (i+1)*len_fragm], color="blue")
                axs[i].set_title("test")
                for index, label in enumerate(axs[i].xaxis.get_ticklabels()):
                    if index % 12000 != 0:
                        label.set_visible(False)
            plt.show()
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


#число дней в окне
window = 210

start = 1
char_num = 8

dv = data_visualiser("C:/Users/ADostovalova/Downloads/Telegram Desktop/omni_min_2023.fmt", "C:/Users/ADostovalova/Downloads/Telegram Desktop/omni_min_2023.lst", "C:/Users/ADostovalova/Downloads/Telegram Desktop/")
dv.print_window_data(3, window,start,char_num)
dv.print_hist_holes()



