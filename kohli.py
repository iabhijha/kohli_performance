import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv("Virat_Kohli.csv")

# print(df.head(10))

# print(df.tail(10))

# df.info()
# print(df.shape)
# print(df["Opposition"].describe())

# print(df["Opposition"] == "v Australia")

# vs_aussies = df[df["Opposition"] == "v Australia"]
# print(vs_aussies)

#Find all the matches where Virat Scored a Century
# print(df[df["Runs"]>=100])

#Find all the matches where Virat's Strike Rate was > 100
# print(df[df["SR"]>100.0])

##Find all the matches where Virat played with Srilanka and scored a century
# print(df[(df["Runs"]>=100) & (df["Opposition"] == "v Sri Lanka")])


def find_centuries(x):
    if x>=50:
        return "OG"
    else:
        return "NOOB"
    
df["Centuries"] = df["Runs"].apply(find_centuries)
print(df.tail(10))

# print(df["Runs"])

# y=np.array(df["Runs"])
# x=np.arange(0,132)

# plt.plot(x,y)
# plt.show()
