import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#Define function to plot the Barplot
def barplt():
    # Dataframes required for ploting
    df= pd.read_excel('bedfordshire_2018.xlsx')
    df1= pd.read_excel('bedfordshire_2019.xlsx')
    df2= pd.read_excel('bedfordshire_2020.xlsx')
    df3= pd.read_excel('bedfordshire_2021.xlsx')
    df4=pd.read_excel('heathrow_2018.xlsx')
    df5=pd.read_excel('heathrow_2019.xlsx')
    df6=pd.read_excel('heathrow_2020.xlsx')
    df7=pd.read_excel('heathrow_2021.xlsx')


#Average of Maximum temperature in each year taken for Bedfordshire
    bed_avg_max2018= np.mean(df['max_air_temp'])
    bed_avg_max2019= np.mean(df1['max_air_temp'])
    bed_avg_max2020= np.mean(df2['max_air_temp'])
    bed_avg_max2021= np.mean(df3['max_air_temp'])

#Average of Maximum temperature in each year taken for Heathrow
    hr_avg_max2018= np.mean(df4['max_air_temp'])
    hr_avg_max2019= np.mean(df5['max_air_temp'])
    hr_avg_max2020= np.mean(df6['max_air_temp'])
    hr_avg_max2021= np.mean(df7['max_air_temp'])
 
#Plotting the Bar plot of Average Maximum temperature between Bedfordshire & Heathrow
    plt.figure(figsize=(10,8),dpi=144)
    max_temp =[]
    max_temp = pd.DataFrame(data = max_temp, columns=["year", "Heathrow_max_temp",
                        "Bedford_max_temp"])
    max_temp['year'] = ['2018', '2019', '2020', '2021']
    max_temp['Heathrow_max_temp'] = [hr_avg_max2018, hr_avg_max2019, 
                                 hr_avg_max2020, hr_avg_max2021]
    max_temp['Bedford_max_temp'] = [bed_avg_max2018, bed_avg_max2019, 
                                bed_avg_max2020, bed_avg_max2021]



    plt.figure(figsize=(10,8))


    x_axis = np.arange(len(max_temp['year'])) 

    plt.bar(x_axis - 0.15, max_temp['Heathrow_max_temp'],width=0.3,label='Heathrow')
    plt.bar(x_axis + 0.15, max_temp['Bedford_max_temp'],width=0.3,label='Bedford')
    plt.title('Average Maximum Temperature of Bedforshire and Heathrow')
    plt.xlabel('Years')
    plt.ylabel('Temperature')
    plt.legend()
    plt.xticks(x_axis,max_temp['year'])
    plt.savefig('Avg_Max_Bar.png', dpi=300)
    plt.show()
    return None
    