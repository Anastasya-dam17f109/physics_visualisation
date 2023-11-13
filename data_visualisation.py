import matplotlib.pyplot as plt
import numpy as np
import datetime
from datetime import timedelta

from datetime import datetime
import pandas as pd
import pyqtgraph as pg
#from pyqtgraph.Qt import QtGui
from pyqtgraph.Qt import QtCore, QtGui

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

            pg.mkQApp()
            win = pg.GraphicsView()
            win.resize(800, 600)
            plot = win.addPlot(title="Plot with Legend")
            plot.plot(self.plot_time_mass, self.value_mass, pen='r', name='series')

            plot.addLegend()
            #print("collected")
            ''' 
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
            plt.show()'''

    def print_window_data_by_mounth(self, split_num, window,start,char_num):
        self.data_mass = []
        self.time_mass = []
        self.time_mass_raw = []
        self.value_mass = []
        ch = np.loadtxt("C:/Users/ADostovalova/Desktop/work/data_phys/202304_measurements.txt", dtype= "float32")
        print("measures load")
        dict_idx = {}
        left_bound = datetime.datetime(2023, 4, 1, 0, 0, 0)
        counter = 0
        for i in range(24*60*60*30):
            self.time_mass.append(str(left_bound) + ".197")
            self.time_mass.append(str(left_bound) + ".696")
            self.time_mass_raw.append(left_bound)
            self.time_mass_raw.append(left_bound)
            dict_idx.update({left_bound.strftime('%d-%m-23:%H:%M:%S') + ".197": counter})
            dict_idx.update({left_bound.strftime('%d-%m-23:%H:%M:%S') + ".696": counter+1})
            left_bound = left_bound + datetime.timedelta(0, 1)
            counter += 2
        print("time set")

        counter = 0
        self.data_mass = [0 for i in range(24 * 60 * 60 * 2 * 30)]
        with open("C:/Users/ADostovalova/Desktop/work/data_phys/202304_dates.txt", "r") as date_file:
            for line in date_file:
                line = line.rstrip()
                self.data_mass[dict_idx.get(line)] = ch[counter,char_num]
                dict_idx.update({line:counter})
                counter += 1

            print("data was read")

           # собираем значения временного ряда для выбраннойхарактеристики в один массив

            self.value_mass = self.data_mass[start: start + window]
            self.value_mass = [self.value_mass[i]  for i in range(1,len(self.value_mass),300)]
            self.plot_time_mass = self.time_mass_raw[start: start + window]
            self.plot_time_mass = [self.plot_time_mass[i] for i in range(1,len(self.plot_time_mass), 300)]

            '''
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
            '''

            class TimeAxisItem(pg.AxisItem):
                def tickStrings(self, values, scale, spacing):
                    return [datetime.fromtimestamp(value) for value in values]
            pg.mkQApp()
            axis = pg.DateAxisItem()
            date_axis = TimeAxisItem(orientation='bottom')
            graph = pg.PlotWidget(axisItems={'bottom': date_axis})

            graph.plot(x=[x.timestamp() for x in self.plot_time_mass], y=self.value_mass, pen='r')
            graph.show()
            #win = pg.GraphicsView()
            #win.resize(800, 600)
            #plot =pg.plot(title="Plot with Legend")
            #plot.setAxisItems({'bottom': axis})
            #plot.plot(self.plot_time_mass, self.value_mass, pen='r', name='series')

            #plot.addLegend()

    def print_window_data_by_mounth_pandas(self, split_num, window, start, char_num):
        dateparse = lambda x: datetime.strptime(x,  '%Y-%m-%d:%H:%M:%S:%f')
           # datetime.datetime.strptime(x, '%Y-%m-%d:%H:%M:%S:%f'))
        infile = "C:/Users/ADostovalova/Desktop/work/data_phys/202304_data.csv"
        df = pd.read_csv(infile, sep=';', parse_dates=['Timestamp'], date_parser=dateparse)
        print(df.head(4))
        self.data_mass = []
        self.time_mass = []
        self.time_mass_raw = []
        self.value_mass = []
        left_bound0 = datetime(2023, 4, 1, 0, 0, 0,197000)
        left_bound1 = datetime(2023, 4, 1, 0, 0, 0, 696000)
        for i in range(24*60*60*30):
            self.time_mass.append(left_bound0 )
            self.time_mass.append(left_bound1)
            left_bound0 = (left_bound0 + timedelta(0, 1))
            left_bound1 = left_bound1 + timedelta(0, 1)
        #dateparse.
        df_time = pd.DataFrame(self.time_mass,
                          columns=['Timestamp'])
        #len(df_time)
        print(df_time.head(4))
        anime = df_time.merge( df, how="left", on=["Timestamp"])
        print(anime.head(4))
        anime.plot(x="Timestamp", y="Radius")
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


#число dht в окне
window = 24*60*60*30*2

start = 1#24*60*60-1
char_num = 8

dv = data_visualiser("C:/Users/ADostovalova/Downloads/Telegram Desktop/omni_min_2023.fmt",
                     "C:/Users/ADostovalova/Desktop/work/data_phys/SW_EXTD_EFIB_LP_HM_20230401T000000_20230401T235959_0101.txt",
                     "C:/Users/ADostovalova/Desktop/work/data_phys")
dv.print_window_data_by_mounth_pandas(1, window,start,char_num)

#dv.print_hist_holes()
#plt.show()
#QtGui.QGuiApplication.instance().exec_()

(3*inputs - sigma*tetha*(tf.random.normal(shape=(1,inputs.shape[1]))*self.x_i[np.random.randint(0,self.num_grids)]- tf.random.normal(shape=(1,inputs.shape[1]))*self.x_i[np.random.randint(0,self.num_grids)]
                 - tf.random.normal(shape=(1,inputs.shape[1]))*self.x_i[np.random.randint(0,self.num_grids)] ))/3.0
