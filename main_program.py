import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import barplot as br
import boxplot as bxp
import lineplot as lp


# User Choice for plotting different graphs
print("1) For Line Plot of Bedfordshire's Maximum & Minimum Temperature spanning from 2018-2021\n")
print("\n 2) For the Box plot between Maximum Temperature of a location inside and outside london i.e.Heathrow & Bedforshire\n")
print("\(n 3) For the Bar Plot of Average Maximum temperature between Heathrow & Bedfordshire for past 4 Years")
print('\n 4) Exit')

choice=" "
'''In accordance to choice each functions are called for respective plotting 
till exit choice is given'''
while choice!='4':
    choice= input('\n What Would you like to choose from entry 1-4 \n')
    if choice =='1':
        print('Please check out the Line Plot')
        lp.lplot()
    elif choice =='2':
        print('\nPlease Check the Boxplot\n')
        bxp.bxplot()        
    elif choice =='3':
        print('\n Please check the Barplot')
        br.barplt()
    else:
        print('\n Thank You')
        break