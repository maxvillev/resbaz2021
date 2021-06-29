#
# hellopanda.py - using pandas to read and plot a csv file
#
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("kungfu.csv", skiprows=3)

print("\n*** Po and the Furious Five ***\n")
print(df)

df.plot(x="Name",kind="bar")
plt.title("Po and the Furious Five")
#plt.savefig("kungfu.png")
plt.show()
