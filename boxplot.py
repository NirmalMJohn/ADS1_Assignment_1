import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def bxplot():
#Data frames required for plotting
    df= pd.read_excel('bedfordshire_2021_bp.xlsx')
    df1=pd.read_excel('heathrow_2021_bp.xlsx')

    data=[df['max_air_temp'],df1['max_air_temp']]

    fig = plt.figure(figsize =(10, 7))
 
# Creating axes instance
    ax = fig.add_axes([0, 0, 1, 1])
 
# Creating plot
    labels=('Bedforshire','Heathrow')
    bp = ax.boxplot(data,labels=labels)
    ax.set_title('Maximum Air Temperature of Bedfordhsire & Heathrow')
    ax.set_ylabel('Temperature')
    plt.savefig('Avg_Max_Box.png', dpi=300)
# show plot
    plt.show()