# vis_wordcloud.py
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from data_loader import load_data


def show():
    st.title("☁️ 国家名称词云图（静态图像）")

    # 加载数据
    df = load_data()

    # 数据预览
    st.markdown("### 📊 数据预览")
    st.write("列名列表：", list(df.columns))
    st.write("数据样本：", df.head())

    if 'Country' not in df.columns:
        st.error("❌ 数据中没有 'Country' 列，请检查数据格式。")
        return

    country_freq = df['Country'].value_counts().to_dict()
    if not country_freq:
        st.warning("⚠️ 没有可用的国家数据生成词云。")
        return

    # 生成词云对象
    wc = WordCloud(
        width=800,
        height=400,
        background_color='white',
        font_path=None,  # 可指定中文字体路径，如 'simhei.ttf'
    ).generate_from_frequencies(country_freq)

    # 使用 Matplotlib 绘图
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wc, interpolation='bilinear')
    ax.axis('off')

    st.markdown("### 🧾 国家词云图")
    st.pyplot(fig)
