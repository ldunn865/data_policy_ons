from typing import List, Tuple

import pandas as pd
import plotly
import plotly.express as px
import streamlit as st
import datetime
import re
import requests
import os

def set_page_config():
    st.set_page_config(
        page_title="The Consumer Prices Index including owner occupiers' housing costs by division levels",
        page_icon=":random:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)


@st.cache_data
def run_main():
    
    with open("notebooks/main.py") as f:
        code = f.read()
    # Create a dictionary to hold the global variables
    global_vars = {}
    # Execute the code with the global variables dictionary
    exec(code, global_vars)
    # Call the generate_dataframe function from main.py
    df = global_vars.get('run')()
    return df



@st.cache_data
def load_data(data_from_main) -> pd.DataFrame:
    data = data_from_main
    data["Date"] = pd.to_datetime(data["Date"])
    return data


def filter_data(data: pd.DataFrame, column: str, values: List[str]) -> pd.DataFrame:
    return data[data[column].isin(values)] if values else data


def display_sidebar(
    data: pd.DataFrame,
) -> Tuple[List[str], List[str], List[str], Tuple[datetime.date, datetime.date]]:
    st.sidebar.header("Filters")

    # Get the minimum and maximum dates from the dataset
    min_start_date = data["Date"].min().date()
    max_end_date = data["Date"].max().date()

    start_date = pd.Timestamp(
        st.sidebar.date_input(
            "Start date",
            min_start_date,
            min_value=min_start_date,
            max_value=max_end_date,
        )
    )
    end_date = pd.Timestamp(
        st.sidebar.date_input(
            "End date", max_end_date, min_value=min_start_date, max_value=max_end_date
        )
    )

    CPI_divisions = sorted(data["Index Name"].unique())
    selected_cpi_divisions = st.sidebar.multiselect("CPIH/CPI Divisions", CPI_divisions)

    return selected_cpi_divisions, (start_date, end_date)


def display_charts(data: pd.DataFrame):
    CPIH_dataset = st.checkbox("CPIH Dataset", value=True)
    CPI_dataset = st.checkbox("CPI Dataset", value=True)
    combine_CPIH_lines = st.checkbox("Combine CPIH Division Lines", value=True)
    combine_CPI_lines = st.checkbox("Combine CPI Division Lines", value=True)
    CPIH_CPI_separate = st.checkbox("Separate lines for CPIH and CPI", value=True)

    if CPIH_CPI_separate:
        grouped_df = data.groupby(["Date", "Name"])["Value"].mean().reset_index()
        fig = px.line(
            grouped_df,
            x="Date",
            y="Value",
            color="Name",
            title="Customer Price Index Over Time",
            width=900,
            height=500,
        )

    elif CPIH_dataset:
        CPIH_data = data[data["Name"] == "CPIH"].copy()
        if combine_CPIH_lines:
            grouped_data = CPIH_data.groupby("Date")["Value"].mean().reset_index()
            fig = px.area(
                grouped_data,
                x="Date",
                y="Value",
                title="Customer Price Index Over Time",
                width=900,
                height=500,
            )
        else:
            fig = px.area(
                CPIH_data,
                x="Date",
                y="Value",
                color="Index Name",
                title="Customer Price Index Over Time",
                width=900,
                height=500,
            )

    elif CPI_dataset:
        CPI_data = data[data["Name"] == "CPI"].copy()
        if combine_CPI_lines:
            grouped_data_CPI = CPI_data.groupby("Date")["Value"].mean().reset_index()
            fig = px.area(
                grouped_data_CPI,
                x="Date",
                y="Value",
                title="Customer Price Index Over Time",
                width=900,
                height=500,
            )
        else:
            fig = px.area(
                CPI_data,
                x="Date",
                y="Value",
                color="Index Name",
                title="Customer Price Index Over Time",
                width=900,
                height=500,
            )

    fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
    fig.update_xaxes(rangemode="tozero", showgrid=False)
    fig.update_yaxes(rangemode="tozero", showgrid=True)
    st.plotly_chart(fig, use_container_width=True)


def main():
    set_page_config()
    
    
    #if __name__ == '__main__':
     #   result_df = run_main()
      #  st.dataframe(result_df)
        
    result_df = run_main()


    data = load_data(result_df)

    st.title(
        "The Consumer Prices Index including owner occupiers' housing costs by division levels"
    )

    st.markdown(
        "The Consumer Price Index measures the overall change in consumer prices based on a representative basket of goods and services over time."
    )

    selected_cpi_divisions, date_range = display_sidebar(data)

    filtered_data = data.copy()
    filtered_data = filter_data(filtered_data, "Index Name", selected_cpi_divisions)

    # Unpack the date range tuple
    start_date, end_date = date_range

    # Apply date filtering here
    filtered_data = filtered_data[
        (filtered_data["Date"] >= start_date) & (filtered_data["Date"] <= end_date)
    ]

    display_charts(filtered_data)


if __name__ == "__main__":
    main()
