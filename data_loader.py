# data_loader.py
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """加载原始数据集"""
    df = pd.read_csv("30_merged_dataset_v00_final.csv")  # 请替换为实际 CSV 文件路径
    # 预处理：统一国家名、处理缺失
    df['Country'] = df['Country'].str.strip()
    df = df.dropna(subset=['Life expectancy', 'GDP'])
    return df

@st.cache_data
def get_year_range(df):
    return int(df['Year'].min()), int(df['Year'].max())

@st.cache_data
def get_country_list(df):
    return sorted(df['Country'].unique())
