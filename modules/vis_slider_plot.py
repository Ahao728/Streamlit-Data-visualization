# pages/vis_slider_plot.py
import streamlit as st
import plotly.express as px
from data_loader import load_data, get_country_list

def show():
    st.title("📽️ 随时间变化的 GDP 与平均寿命关系图")

    df = load_data()
    countries = get_country_list(df)

    default_countries = ["United States of America", "Brazil", "Norway"]
    valid_defaults = [c for c in default_countries if c in countries]

    selected_countries = st.multiselect("选择国家", countries, default=valid_defaults)

    df_filtered = df[df['Country'].isin(selected_countries)]

    fig = px.scatter(
        df_filtered,
        x="GDP",
        y="Life expectancy",
        animation_frame="Year",
        animation_group="Country",
        size="Population",
        color="Country",
        hover_name="Country",
        size_max=60,
        range_x=[0, df_filtered["GDP"].max() * 1.1],
        range_y=[df_filtered["Life expectancy"].min() - 5, df_filtered["Life expectancy"].max() + 5],
        title="随时间变化的 GDP 与平均寿命"
    )

    fig.update_layout(height=650)
    st.plotly_chart(fig, use_container_width=True)
