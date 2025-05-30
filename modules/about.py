# modules/about.py

def show():
    import streamlit as st

    st.title("📚 作者信息")
    
    st.markdown("""
    ## 🌍 全球健康与社会数据可视化项目

    这是一个基于 Streamlit 的交互式数据可视化 Web 应用，用于探索全球各国的健康、经济和社会发展指标。

    ### 👤 作者简介

    - **姓名**：陈昊
    - **学校**：岭南师范学院 数据科学与大数据技术专业
    - **邮箱**：Chan7728@outlook.com
    - **GitHub**：[github.com/Ahao728](https://github.com/Ahao728) 
    - **项目时间**：2025年4月

    ### 💡 使用的技术栈
    - Python
    - Streamlit
    - Pandas / Plotly / Matplotlib / Pyecharts / Seaborn
    - 数据集来源：https://www.kaggle.com/datasets/mexwell/global-suicide-rates/data

    感谢使用本项目，欢迎提出建议和反馈！📩
    """)

    