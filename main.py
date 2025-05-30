import streamlit as st
from modules import (
    home,
    vis_gdp_life,
    vis_mortality,
    vis_heatmap,
    vis_slider_plot,
    vis_wordcloud,
    vis_suicide_analysis,
    vis_education_gdp,
    about,
)

# 设置页面配置
st.set_page_config(
    page_title="🌍 全球健康与社会数据可视化",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS美化界面
st.markdown("""
<style>
    body {
        background-color: #f8f9fa;
        font-family: "Segoe UI", sans-serif;
    }
    .sidebar .sidebar-content {
        width: 100%;
    }
    .css-145kmo2 {
        color: #007BFF;
        font-weight: bold;
    }
    .stSelectbox label {
        font-size: 16px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 侧边栏标题 + 图标
st.sidebar.markdown("### 📊 数据可视化导航")
st.sidebar.markdown("---")

# 页面字典
all_pages = {
    "🏠 首页": home,
    "📈 GDP vs 寿命": vis_gdp_life,
    "📉 死亡率趋势": vis_mortality,
    "🌡️ 寿命热力图": vis_heatmap,
    "⏳ 年份滑块图": vis_slider_plot,
    "🧠 自杀率分析": vis_suicide_analysis,
    "🏫 教育与GDP关系": vis_education_gdp,
    "🌍 国家词云图": vis_wordcloud,
    "📚 作者信息": about,   
}

# 页面选择器
selected_page = st.sidebar.selectbox("🔍 请选择一个可视化页面", list(all_pages.keys()))

# 显示当前页面
st.sidebar.markdown("---")
st.sidebar.markdown("📌 当前页面：**{}**".format(selected_page))

# 调用对应模块的 show() 方法
all_pages[selected_page].show()