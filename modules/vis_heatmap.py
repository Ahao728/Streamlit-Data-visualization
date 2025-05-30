import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import HeatMap
import numpy as np
import pandas as pd
from data_loader import load_data, get_country_list
import streamlit.components.v1 as components

def show():
    st.title("🌡️ 各国平均寿命热力图")

    df = load_data()
    countries_all = get_country_list(df)

    # 默认改成数据集里有的国家
    default_countries = [c for c in ["United States of America", "Brazil", "Norway"] if c in countries_all]

    selected_countries = st.multiselect(
        "选择国家（最多20个）",
        countries_all,
        default=default_countries,
        max_selections=20
    )

    if not selected_countries:
        st.warning("请至少选择一个国家")
        return

    df_filtered = df[df['Country'].isin(selected_countries)]

    # 透视表，国家为行，年份为列，值为平均寿命
    pivot_table = df_filtered.pivot(index="Country", columns="Year", values="Life expectancy")

    years = list(pivot_table.columns)
    countries = list(pivot_table.index)

    # 生成热力图需要的坐标和值三元组格式 [(x轴，y轴，value), ...]
    data = []
    for i, country in enumerate(countries):
        for j, year in enumerate(years):
            val = pivot_table.at[country, year]
            if pd.isna(val):
                val = 0
            data.append([j, i, val])

    heatmap = (
    HeatMap(init_opts=opts.InitOpts(width="1000px", height="600px"))
    .add_xaxis([str(year) for year in years])
    .add_yaxis("平均寿命", countries, data, label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(title="平均寿命热力图"),
        visualmap_opts=opts.VisualMapOpts(
            min_=np.nanmin(pivot_table.values),
            max_=np.nanmax(pivot_table.values),
            orient="vertical",
            pos_left="right",
            pos_top="center",
            range_text=["低", "高"],
            is_calculable=True,
            dimension=2,
            range_color=["#d73027", "#ffffbf", "#4575b4"],
        ),
        xaxis_opts=opts.AxisOpts(name="年份", type_="category"),
        yaxis_opts=opts.AxisOpts(name="国家", type_="category"),
        tooltip_opts=opts.TooltipOpts(
            formatter="{a}<br />{b} - {c}"
        ),
    )
)

    html_content = heatmap.render_embed()
    components.html(html_content, height=650, scrolling=True)
