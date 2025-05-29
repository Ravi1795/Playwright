import numpy as np
import pandas as pd
# arr = np.array([1,2,3,4,5,6,7,8,9,10])
#
# print(arr)
# print(np.mean(arr))
# print(np.std(arr))
# print(np.median(arr))
# print(np.var(arr))

df = pd.read_csv("C:/Users/ravi.yadav_infobeans/Downloads/people_data.csv")
df.head(3)
# print("==============")
# print(df.iloc[0,0])
# df["Salary"]=[50000.30,60000.32,70000.3224,800000.4332,900000.234]
# print("==============")
# print(df.at[2,"Salary"])
# print("==============")
# print(df.iat[2,2])
# print("==============")
# print(df.head(5))
# print("==============")
# print(df.describe())
# print("==============")
# df["Salary_Mean"]=df["Salary"].fillna(df["Salary"].mean())
# print("==============")
# print(df.head(5))
# df = df.rename(columns={"Salary":"Money"})
# print(df.head())
# print("====================")
# df["Salary_Mean"]=df["Salary_Mean"].astype(int)
# print(df.head())
#
# grouped = df.groupby(["Job Title"])["Money"].sum()
# print(grouped)

#
# x = [3,4,5,6,8,4,3,1,7]
# y = [1,2,3,4,5,6,7,8,9]
#
# plt.plot(x,y)
# plt.show()