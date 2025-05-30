# vis_suicide_analysis.py
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from data_loader import load_data, get_country_list


def show():
    st.title("🧠 自杀率与相关社会变量分析")

    # 设置中文字体和解决负号显示问题
    sns.set_theme(style="whitegrid")
    sns.set_theme(rc={'font.sans-serif': ['Microsoft YaHei', 'SimHei'], 'axes.unicode_minus': False})

    df = load_data()
    countries = get_country_list(df)

    st.markdown("选择要分析的国家和对比变量，查看自杀数与其他变量的关系。")

    # 默认国家列表（确保是数据中存在的）
    default_countries = ["Japan", "United States of America", "Brazil"]
    valid_defaults = [c for c in default_countries if c in countries]

    selected_countries = st.multiselect("选择国家", countries, default=valid_defaults)
    x_var = st.selectbox("选择 X 轴变量",
                         ["Alcohol", "HIV/AIDS", "Schooling", "Income composition of resources", "GDP"])

    df_filtered = df[df["Country"].isin(selected_countries)]

    # 创建折线图画布（缩小尺寸）
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.lineplot(
        data=df_filtered,
        x=x_var,
        y="Suicides number",
        hue="Country",
        marker="o",
        ax=ax
    )

    ax.set_title(f"各国自杀人数 vs {x_var}（Seaborn 折线图）", fontsize=14)
    ax.set_xlabel(x_var, fontsize=12)
    ax.set_ylabel("自杀人数", fontsize=12)

    # 可选：创建散点图画布（缩小尺寸）
    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.scatterplot(
        data=df_filtered,
        x=x_var,
        y="Suicides number",
        hue="Country",
        ax=ax2
    )

    ax2.set_title(f"各国自杀人数 vs {x_var}（Seaborn 散点图）", fontsize=14)
    ax2.set_xlabel(x_var, fontsize=12)
    ax2.set_ylabel("自杀人数", fontsize=12)

    # 使用 st.columns 并排显示两个图表
    col1, col2 = st.columns(2)
    with col1:
        st.pyplot(fig)
    with col2:
        st.pyplot(fig2)