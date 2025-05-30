# pages/home.py
import streamlit as st
from data_loader import load_data

def show():
    st.title("🌍 全球健康与社会发展可视化平台")
    st.markdown("""
    本平台基于世界范围内多个国家的人口健康与社会经济指标构建，涵盖：
    
    - 人均寿命、死亡率、自杀率等健康指标
    - GDP、教育资源、HIV/AIDS、酒精使用等社会经济变量
    - 支持交互式图表、年度滑动、国家选择等操作

    📈 快通过左侧菜单探索可视化模块吧！
    """)

    df = load_data()
    st.subheader("📄 数据样例预览")
    st.dataframe(df.head(20), use_container_width=True)

    st.info(f"数据共包含 **{df.shape[0]} 行**, **{df.shape[1]} 列**, 来自 **{df['Country'].nunique()} 个国家**，时间范围 **{df['Year'].min()} - {df['Year'].max()}**")
