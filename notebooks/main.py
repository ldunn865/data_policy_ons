from typing import List, Tuple

import pandas as pd
import plotly
import plotly.express as px
import streamlit as st
import datetime
import re
import requests
import os




def get_csv(csv_url):

    # Make a GET request to the CSV file URL
    response = requests.get(csv_url)

    # Check if the request was successful
    if response.status_code == 200:
        # Save the CSV content to a local file
        with open("data/raw/mm23.csv", "wb") as csv_file:
            csv_file.write(response.content)
        print("CSV file downloaded successfully.")
    else:
        print("Failed to fetch the CSV file.")
        
    df_CPI = pd.read_csv(filepath_or_buffer="data/raw/mm23.csv")
        
    
    
    
    return df_CPI


def clean_data(data):
    # getting the right months, issue here is that cells might change better to do it with matching?
    df_months = data[1017:1444].copy()
    df_months["Title"] = pd.to_datetime(df_months["Title"], format="%Y %b")
    
    CPI_division_level = [
    "CPI INDEX 01 : FOOD AND NON-ALCOHOLIC BEVERAGES 2015=100",
    "CPI INDEX 02:ALCOHOLIC BEVERAGES,TOBACCO & NARCOTICS 2015=100",
    "CPI INDEX 03 : CLOTHING AND FOOTWEAR 2015=100",
    "CPI INDEX 04 : HOUSING, WATER AND FUELS 2015=100",
    "CPI INDEX 05 : FURN, HH EQUIP & ROUTINE REPAIR OF HOUSE 2015=100",
    "CPI INDEX 06 : HEALTH 2015=100",
    "CPI INDEX 07 : TRANSPORT 2015=100",
    "CPI INDEX 08 : COMMUNICATION 2015=100",
    "CPI INDEX 09 : RECREATION & CULTURE 2015=100",
    "CPI INDEX 10 : EDUCATION 2015=100",
    "CPI INDEX 11 : HOTELS, CAFES AND RESTAURANTS 2015=100",
    "CPI INDEX 12 : MISCELLANEOUS GOODS AND SERVICES 2015=100",]

    CPIH_division_level = [
        "CPIH INDEX 01 : FOOD AND NON-ALCOHOLIC BEVERAGES 2015=100",
        "CPIH INDEX 02:ALCOHOLIC BEVERAGES,TOBACCO & NARCOTICS 2015=100",
        "CPIH INDEX 03 : CLOTHING AND FOOTWEAR 2015=100",
        "CPIH INDEX 04: Housing, water, electricity, gas and other fuels 2015=100",  # this is different to above
        "CPIH INDEX 05 : FURN, HH EQUIP & ROUTINE REPAIR OF HOUSE 2015=100",
        "CPIH INDEX 06 : HEALTH 2015=100",
        "CPIH INDEX 07 : TRANSPORT2015=100",
        "CPIH INDEX 08 : COMMUNICATION 2015=100",
        "CPIH INDEX 09 : RECREATION & CULTURE 2015=100",
        "CPIH INDEX 10 : EDUCATION 2015=100",
        "CPIH INDEX 11 : HOTELS, CAFES AND RESTAURANTS 2015=100",
        "CPIH INDEX 12 : MISCELLANEOUS GOODS AND SERVICES 2015=100",]

    CPH_CPIH_list = [CPI_division_level, CPIH_division_level] #length of 2 

    CPH_CPIH_list_df = []

    for division_type in CPH_CPIH_list:
        # Create a list of DataFrames to merge
        dfs_to_merge = [df_months[["Title", x]] for x in division_type]

        # Merge the DataFrames on the "Title" column
        merged_df = dfs_to_merge[0]
        for df in dfs_to_merge[1:]:
            merged_df = pd.merge(merged_df, df, on="Title", how="inner")

        # renaming columns - could create a function for this
        if division_type == CPI_division_level:
            merged_df = merged_df.rename(
                columns={
                    "CPI INDEX 02:ALCOHOLIC BEVERAGES,TOBACCO & NARCOTICS 2015=100": "CPI INDEX 02 : ALCOHOLIC BEVERAGES,TOBACCO & NARCOTICS 2015=100",
                    "Title": "Date",
                }
            )
            clean_column_names = []
            pattern = r"CPI INDEX \d+ : (.*?) \d+=\d+"
            clean_column_names.extend(
                [re.sub(pattern, r"\1", text) for text in merged_df.columns]
            )

            merged_df.columns = clean_column_names

        else: #it doesnt run this for some reason
          
            merged_df = merged_df.rename(
                columns={
                    "CPIH INDEX 02:ALCOHOLIC BEVERAGES,TOBACCO & NARCOTICS 2015=100": "CPIH INDEX 02 : ALCOHOLIC BEVERAGES,TOBACCO & NARCOTICS 2015=100",
                    "Title": "Date",
                    "CPIH INDEX 07 : TRANSPORT2015=100": "CPIH INDEX 07 : TRANSPORT 2015=100",
                    "CPIH INDEX 04: Housing, water, electricity, gas and other fuels 2015=100": "CPIH INDEX 04 : Housing, water, electricity, gas and other fuels 2015=100",
                }
            )
        
            clean_column_names = []
            pattern = r"CPIH INDEX \d+ : (.+?) 2015=100"
            clean_column_names.extend(
                [re.sub(pattern, r"\1", text) for text in merged_df.columns]
            )

            merged_df.columns = clean_column_names
        

        CPH_CPIH_list_df.append(merged_df)
    
        long_df_list = []

    for x in CPH_CPIH_list_df:
        merged_df_long = x.copy()
        merged_df_long = (
            merged_df_long.set_index("Date").melt(ignore_index=False).reset_index()
            )
        long_df_list.append(merged_df_long)
         
        
    return long_df_list
    
    
def combine_dataframe(data):
    long_CPI = data[1].copy() #out of range
    long_CPI.columns = ["Date", "Index Name", "Value"]
    long_CPI["Name"] = "CPI"
    
    long_CPIH = data[0].copy()
    long_CPIH.columns = ["Date", "Index Name", "Value"]
    long_CPIH["Name"] = "CPIH"
    
    combined_df = pd.concat([long_CPIH, long_CPI], ignore_index=True)
    combined_df = combined_df.sort_values(by=["Date"])
    
    combined_df.to_csv("data/processed/CPIH_and_CPI_df.csv")
    
    return combined_df


def run():
    
    df_CPI = get_csv(csv_url = "https://www.ons.gov.uk/file?uri=/economy/inflationandpriceindices/datasets/consumerpriceindices/current/mm23.csv")
    long_df_list = clean_data(data = df_CPI)
    combined_df = combine_dataframe(data = long_df_list)
    
    return combined_df
    
    
    
    
    
    
    
    
    
  
