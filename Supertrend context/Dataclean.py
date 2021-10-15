import pandas as pd 
df=pd.read_csv("E:/Backtest project/Supertrend context/Data/BANKNIFTY_F1_5min.csv")
# print(df.head(50))

df["Date_Time"]=pd.to_datetime(df["Date_Time"])
df.set_index(df["Date_Time"],inplace=True)
# print(df.head(100))
# # df1 = pd.DataFrame(df["Date_Time"])
# df1 = pd.DataFrame(df1.Date_Time.str.split(' ',1).tolist(),
#                                  columns = ['Date','Time'])

# print(df1)
# df["Date_Time"] = pd.to_datetime(df["Date_Time"])
# df.set_index("Date_Time",inplace=True)
# df = df.between_time(start_time = "10:00:00",end_time="15:30:00",include_end=False)
df = df.resample("60T").agg({"Open":"first","High":"max","Low":"min","Close":"last"})

df.dropna(inplace=True)

print(df.head(100))
df.to_csv("E:/Backtest project/Supertrend context/Data/BANKNIFTY_F1_60min.csv")