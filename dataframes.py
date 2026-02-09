import pandas as pd
from datetime import date

dic = {"product":["honey", "flour","wine"],
       "quantity":[100,55,1800],
       "expiring":[date(2025,8,10), date(2024,9,25),date(2023,10,15)],
       "cost":[2,3,10]}

df=pd.DataFrame(data=dic)

print(df)
print(df.head(1))
print(df.tail(1))
print(df.shape)