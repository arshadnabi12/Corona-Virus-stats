import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_csv("corona_stat.csv")
fig, ax = plt.subplots()
years = df['country name']
x = np.arange(len(years))
width = 0.15
ax.bar(x - 3*width/2, df['total cases recovered'], width, label='Total cases recovered', color='#0000FF')
ax.bar(x - width/2, df['total cases confirmed'], width, label='total cases confirmed', color='#E10600')
ax.set_ylabel('CASES')
ax.set_xlabel('COUNTRIES')
ax.set_title('CORONA VIRUS STATISTICS')
ax.set_xticks(x)   
ax.set_xticklabels(years.astype(str).values, rotation='vertical')
ax.legend()
plt.show()
