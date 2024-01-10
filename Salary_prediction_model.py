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



#define display_and_select_csv function


def display_and_select_csv(csv_files):
    i=0
    for file_name in csv_files:
        print(i,'....',file_name)
        i+=1
    return csv_files[int(input("select csv file to create model"))]











# define main function
def main():
    welcome()
    try:
        csv_files=checkcsv()
        if csv_files=="No csv files in the directory":
            raise FileNotFoundError("No csv files in the directory")
        csv_file=display_and_select_csv(csv_files)
        print(csv_file,'is selected')
        print('Reading csv file')
        print('Creating dataset')
    # create dataset by reading csv file
        dataset=pd.read_csv(csv_file)
        print('dataset is created')

     # obtaining x and y
        
        x=dataset.iloc[:,:-1]                        
        y=dataset.iloc[:,-1]




    except FileNotFoundError:
        print("No csv files in the directory")
        








#flow of program
if __name__=="__Salary_prediction_model__" :
    main()
    input()
