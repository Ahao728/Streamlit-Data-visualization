import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Bar
from data_loader import load_data, get_country_list

def show():
    st.title("🏫 教育资源 vs GDP 对比（柱形图）")

    df = load_data()
    countries = get_country_list(df)

    selected_countries = st.multiselect(
        "选择国家",
        countries,
        default=["Norway", "Brazil", "South Africa", "United States of America"]
    )

    year = st.slider("选择年份", int(df['Year'].min()), int(df['Year'].max()), 2015)

    df_filtered = df[(df['Country'].isin(selected_countries)) & (df['Year'] == year)]

    # 按国家顺序准备数据
    gdp_data = [df_filtered[df_filtered['Country'] == c]['GDP'].values[0] if c in df_filtered['Country'].values else 0 for c in selected_countries]
    schooling_data = [df_filtered[df_filtered['Country'] == c]['Schooling'].values[0] if c in df_filtered['Country'].values else 0 for c in selected_countries]

    bar = (
        Bar(init_opts=opts.InitOpts(width="1000px", height="600px"))
        .add_xaxis(selected_countries)
        .add_yaxis("GDP", gdp_data, yaxis_index=0)
        .add_yaxis("教育年限", schooling_data, yaxis_index=1)
        .extend_axis(
            yaxis=opts.AxisOpts(
                name="教育年限",
                type_="value",
                position="right",
                offset=0,
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color="#675bba")
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} 年"),
            )
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title=f"{year} 年各国 GDP 与 教育年限对比柱状图"),
            yaxis_opts=opts.AxisOpts(
                name="GDP",
                axislabel_opts=opts.LabelOpts(formatter="{value}"),
            ),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="shadow"),
            datazoom_opts=opts.DataZoomOpts(),
            legend_opts=opts.LegendOpts(pos_top="10%"),
        )
    )

    html_content = bar.render_embed()
    st.components.v1.html(html_content, height=650, scrolling=True)
