# pages/vis_gdp_life.py
import streamlit as st
import plotly.express as px
from data_loader import load_data, get_year_range, get_country_list

def show():
    st.title("💰 GDP vs 平均寿命")

    df = load_data()
    min_year, max_year = get_year_range(df)
    countries = get_country_list(df)

    year = st.slider("选择年份", min_year, max_year, 2015)
    selected_countries = st.multiselect("选择国家（可多选，默认显示全部）", countries, default=countries)

    df_filtered = df[(df['Year'] == year) & (df['Country'].isin(selected_countries))]

    fig = px.scatter(
        df_filtered,
        x='GDP',
        y='Life expectancy',
        size='Population',
        color='Country',
        hover_name='Country',
        size_max=60,
        title=f"{year} 年各国 GDP 与平均寿命关系图"
    )
    fig.update_layout(height=600)
    st.plotly_chart(fig, use_container_width=True)
