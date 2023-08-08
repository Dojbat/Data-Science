from matplotlib import *
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("April Action.csv")
rf = pd.read_csv("Target.csv")
vf = pd.read_csv("March Action.csv")
af = pd.read_csv("March Target.csv")

qe = []
eq = []
plt.figure(figsize=(20,40))
for t in rf['New user']:
    qe.append(t)
for r in rf['date']:
    eq.append(r)
plt.title("March Action data")
plt.plot(eq,qe)
plt.show()