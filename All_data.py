import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("April Action.csv")
rf = pd.read_csv("Target.csv")
vf = pd.read_csv("March Action.csv")
af = pd.read_csv("March Target.csv")
ls = []
sl = []
plt.figure(figsize=(20,40))
for i in df['open page']:
    ls.append(i)
for j in df['Date']:
    sl.append(j)
plt.title("April Action data")
plt.xlabel("Date")
plt.ylabel("Open page")
plt.plot(sl,ls)
plt.grid()
plt.show()
