import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def lplot():
#Data Frames required for plotting
    df= pd.read_excel('bedfordshire_2018_lp.xlsx')
    df1= pd.read_excel('bedfordshire_2019_lp.xlsx')
    df2= pd.read_excel('bedfordshire_2020_lp.xlsx')
    df3= pd.read_excel('bedfordshire_2021_lp.xlsx')

#Plotting four years Maximum temperature for Bedfordshire
    plt.figure(figsize=(18,10),dpi=144)

    plt.style.use('ggplot')
    plt.plot(df['DD_MM_YYYY'],df['max_air_temp'],label='2018')
    plt.plot(df1['DD_MM_YYYY'],df1['max_air_temp'],label='2019')
    plt.plot(df2['DD_MM_YYYY'],df2['max_air_temp'],label='2020')
    plt.plot(df3['DD_MM_YYYY'],df3['max_air_temp'],label='2021')
    plt.title('Maximum air temperature of Bedfordshire 2018-2021')
    plt.xlabel('Months')
    plt.ylabel('Temperatures')
    plt.legend()
    plt.savefig('Max_Temp_lp.png', dpi=300)
    plt.show()

#Plotting four years Minimum temperature for Bedfordshire
    plt.figure(figsize=(18,10),dpi=144)

    plt.style.use('ggplot')
    plt.plot(df['DD_MM_YYYY'],df['min_air_temp'],label='2018')
    plt.plot(df1['DD_MM_YYYY'],df1['min_air_temp'],label='2019')
    plt.plot(df2['DD_MM_YYYY'],df2['min_air_temp'],label='2020')
    plt.plot(df3['DD_MM_YYYY'],df3['min_air_temp'],label='2021')
    plt.title('Minimum air temperature of Bedfordshire 2018-2021')
    plt.xlabel('Months')
    plt.ylabel('Temperature')
    plt.legend()
    plt.savefig('Min_Temp_lp.png', dpi=300)
    plt.show()