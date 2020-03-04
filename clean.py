import pandas as pd
import os
import csv
import shutil
import sys
import glob
import operator
import time

def removeRowsWith(df,string):
    for col in df.columns:
            indexNames = df[df[col]==string].index
            if not indexNames.empty:
                print('deleting {} rows with {} in column {}'.format(len(indexNames),string, col))
                df.drop(indexNames, inplace=True)
    return df

def loadData(csvFile):

    df = pd.read_csv(csvFile, low_memory=False, na_values='...')
    #Change this to reflect the column names in the csv
    #
    df.columns=['District','Total Defendants','Violent Offenses','Property Offenses','Fraudulent Other','Drug Offenses','Public-Order Offenses','Regulatory Other']
    #
    #
    for col in df.columns:
        df[col]=df[col].str.replace("%",'') #remove percent signs

    df=removeRowsWith(df,'   All districts') #remove rows with useless info
    df=removeRowsWith(df,'District')
    df=removeRowsWith(df,'Total')

    df=df.dropna(subset=['District','Total Defendants']) #Drop NaN values in the two columns where NaN is not valid
    df=df.dropna(how='all') #drop empty rows
    return df

try:
    file=sys.argv[1]
    df1=loadData('{}'.format(file))
    df1.to_csv('clean/clean{}.csv'.format(file),index=False )
except IndexError:
    print('Please provide absolute file path')
    exit(0)
