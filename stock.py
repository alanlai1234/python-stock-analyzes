import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
plt.style.use("fivethirtyeight")
class analysis_1:
    def __init__(self, c, end, start):
        html=requests.get("http://www.moneydj.com/funddj/bcd/tBCDNavList.djbcd?a="+c+"&&b="+start+"&c="+end)
        date=html.text.split(" ")[0].split(",")
        self.dates=[datetime(int(date[i][:4]), int(date[i][4:6]), int(date[i][6:])) for i in range(len(date))]
        self.data=html.text.split(" ")[1].split(",")
        self.data=[float(i) for i in self.data]
        self.stock_return=[i/self.data[0] for i in self.data]
        self.code=c
    def getplot(self, choice):
        if (choice=="volunm"):
            return pd.DataFrame({self.code:self.data}, index=self.dates).plot()
        elif (choice=="return"):
            return pd.DataFrame({self.code:self.stock_return}, index=self.dates).plot()
#start
ACCY98=analysis_1("ACCY98", "2017-08-15", "2018-8-15")
AC0057=analysis_1("AC0057", "2017-08-15", "2018-8-15")
ACFP87=analysis_1("ACFP87", "2017-08-15", "2018-8-15")
#ACFP87.getplot("return")
pd.DataFrame({"ACCY98":ACCY98.stock_return, "AC0057":AC0057.stock_return, "ACFP87":ACFP87.stock_return}, index=ACFP87.dates).plot()
#pd.DataFrame({"factor":[i-k for i, k in zip(ACCY98.stock_return, ACFP87.stock_return)]}, index=ACCY98.dates).plot()
plt.show()
