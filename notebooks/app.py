from typing import List, Tuple

import pandas as pd
import plotly.express as px
import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="Consumer Price Index by division levels",
        page_icon=":random:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown("<style> footer {visibility: hidden;} </style>", unsafe_allow_html=True)
    

@st.cache_data
def load_data() -> pd.DataFrame:
    data = pd.read_csv("../data/processed/merged_df_long.csv")
    data['Date'] = pd.to_datetime(data['Date'])
    return data

def filter_data(data: pd.DataFrame, column: str, values: List[str]) -> pd.DataFrame:
    return data[data[column].isin(values)] if values else data

def display_sidebar(data: pd.DataFrame) -> Tuple[List[str], List[str], List[str]]:
    st.sidebar.header("Filters")
    start_date = pd.Timestamp(st.sidebar.date_input("Start date", data['Date'].min().date()))
    end_date = pd.Timestamp(st.sidebar.date_input("End date", data['Date'].max().date()))


    CPI_divisions = sorted(data['variable'].unique())
    selected_cpi_divisions = st.sidebar.multiselect("CPI Divisions", CPI_divisions)


    #product_lines = sorted(data['PRODUCTLINE'].unique())
    #selected_product_lines = st.sidebar.multiselect("Product lines", product_lines, product_lines)

    #selected_countries = st.sidebar.multiselect("Select Countries", data['COUNTRY'].unique())

    #selected_statuses = st.sidebar.multiselect("Select Order Statuses", data['STATUS'].unique())

    return selected_cpi_divisions # selected_product_lines, selected_countries, selected_statuses


def display_charts(data: pd.DataFrame):
    combine_product_lines = st.checkbox("Combine CPI Division Lines", value=True)

    if combine_product_lines:
        fig = px.area(data, x='Date', y='value',
                      title="Customer Price Index Over Time", width=900, height=500)
    else:
        fig = px.area(data, x='Date', y='value', color='variable',
                      title="Customer Price Index Over Time", width=900, height=500)

    fig.update_layout(margin=dict(l=20, r=20, t=50, b=20))
    fig.update_xaxes(rangemode='tozero', showgrid=False)
    fig.update_yaxes(rangemode='tozero', showgrid=True)
    st.plotly_chart(fig, use_container_width=True)

    #col1, col2, col3 = st.columns(3)

    #with col1:
    #    st.subheader("Top 10 Divisions")
    #    top_customers = data.groupby('CUSTOMERNAME')['SALES'].sum().reset_index().sort_values('SALES',
    #                                                                                          ascending=False).head(10)
    #    st.write(top_customers)

    #with col2:
    #    st.subheader("Top 10 Products by Sales")
    #    top_products = data.groupby(['PRODUCTCODE', 'PRODUCTLINE'])['SALES'].sum().reset_index().sort_values('SALES',
    #                                                                                                         ascending=False).head(
    #        10)
    #    st.write(top_products)

    #with col3:
    #    st.subheader("Total Sales by Product Line")
    #    total_sales_by_product_line = data.groupby('PRODUCTLINE')['SALES'].sum().reset_index()
    #    st.write(total_sales_by_product_line)


def main():
    set_page_config()

    data = load_data()

    st.title("Consumer Price Index by division levels")

    selected_cpi_divisions = display_sidebar(data)

    filtered_data = data.copy()
    filtered_data = filter_data(filtered_data, "variable", selected_cpi_divisions)
    #filtered_data = filter_data(filtered_data, 'COUNTRY', selected_countries)
    #filtered_data = filter_data(filtered_data, 'STATUS', selected_statuses)

    #kpis = calculate_kpis(filtered_data)
    #kpi_names = ["Total Sales", "Total Orders", "Average Sales per Order", "Unique Customers"]
    #display_kpi_metrics(kpis, kpi_names)

    display_charts(filtered_data)


if __name__ == '__main__':
    main()



