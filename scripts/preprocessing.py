# preprocessing.py
# author: Fiona Chang
# date: 2024-03-14

#import libraries & packages
import click
import os
import requests
import zipfile
import pandas as pd
import shutil

#options
@click.command()
@click.option('--raw-data', type = str)
@click.option('--data-to', type = str)

#main

def main(raw_data, data_to):
    '''
    Reads in data and preprocesses it to be used in EDA (mainly drops null values).
    Saves the preprocessor to be used in next script.
    
    Parameters:
    --------
    raw_data: data downloaded from previous script

    Returns:
    --------
    None
    '''
    # Read the CSV file
    df = pd.read_csv(raw_data)

    #See data details

    df.head()
    df.info()

    # Clean data from null values

    df_clean = df.dropna()  
    df_clean.info()

if __name__ == '__main__':
    main()