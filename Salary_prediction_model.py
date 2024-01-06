# import neessary module

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#define welcome function


def welcome():
    print("Welcome to salary prediction system")
    print("Press ENTER key to proceed")
    input()




# define checkcsv function

def checkcsv():
    csv_files=[]
    cur_dir=os.getcwd()
    content_list=os.lisdir(cur_dir)
    for x in content_list:
        if x.split('.')[-1]=='csv':
            csv_files.append(x)
    if len(csv_files)==0:
        return "No csv files in the directory"
    else:
        return csv_files






# define main function
def main():
    welcome()
    try:
        csv_files=checkcsv()




    except
        








#flow of program
if __name__=="Salary_prediction_model__" :
    main()
    input()
