import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

html =  requests.get("https://www.moneydj.com/Z/ZB/ZBH/CZKC0_EB09999_D.djbcd")

# split the data
data_1 = html.text.split()
#the first paragraph of data is the dates
date_1 = data_1.pop(0)
#split all the data individually into 2d list
data_1 = [[float(a) for a in i.split(",")] for i in data_1]
#create a dataframe of the datas and indexes with the dates
frame=pd.DataFrame({"open":data_1[0], "high":data_1[1], "low":data_1[2], "close":data_1[3], "vol":data_1[4]}, index=[datetime(int(i.split("/")[0]), int(i.split("/")[1]), int(i.split("/")[2])) for i in date_1.split(",")])
print("hi")
#create a moving average chart
pd.DataFrame({"p1":frame.rolling(window=60).mean()["close"].values, "close":frame["close"].values, "p2":frame.rolling(window=30).mean()["close"].values}, index=frame.index).plot()
plt.show()