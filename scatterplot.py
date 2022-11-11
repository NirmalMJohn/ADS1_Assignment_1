


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df= pd.read_excel('bedfordshire_2021_bp.xlsx')

x = df['DD_MM_YYYY']
y = df['min_air_temp']

plt.scatter(x, y)
plt.show()