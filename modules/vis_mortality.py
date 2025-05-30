# pages/vis_mortality.py
import streamlit as st
import plotly.graph_objects as go
from data_loader import load_data, get_country_list

def show():
    st.title("📉 婴儿 & 成人死亡率趋势")

    df = load_data()
    countries = get_country_list(df)

    # 默认值改为数据中真实存在的国家
    default_countries = ["United States of America", "Brazil", "Norway"]
    valid_defaults = [c for c in default_countries if c in countries]

    selected_countries = st.multiselect("选择国家", countries, default=valid_defaults)

    df_filtered = df[df['Country'].isin(selected_countries)]
    df_grouped = df_filtered.groupby(['Year', 'Country'])[['Infant deaths', 'Adult Mortality']].mean().reset_index()

    fig = go.Figure()

    for country in selected_countries:
        country_data = df_grouped[df_grouped['Country'] == country]
        fig.add_trace(go.Scatter(
            x=country_data['Year'],
            y=country_data['Infant deaths'],
            mode='lines+markers',
            name=f"{country} - 婴儿死亡数"
        ))
        fig.add_trace(go.Scatter(
            x=country_data['Year'],
            y=country_data['Adult Mortality'],
            mode='lines+markers',
            name=f"{country} - 成人死亡率"
        ))

    fig.update_layout(
        title="各国 婴儿死亡数 与 成人死亡率 趋势图",
        xaxis_title="年份",
        yaxis_title="人数",
        height=600
    )

    st.plotly_chart(fig, use_container_width=True)
