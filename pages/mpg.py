import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib
import seaborn as sns
import plotly.express as px


st.set_page_config(
    page_title = "Likelion AI school 자동차 연비 App",
    page_icon = "🚗",
    layout = "wide"
)

st.markdown("# 자동차 연비 🚗")
st.sidebar.markdown("# 자동차 연비 🚗")

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/mpg.csv"

@st.cache
def load_data(url):
    data = pd.read_csv(url)
    return data

data_load_state = st.text('Loading data...')
mpg = load_data(url)
data_load_state.text("Done! (using st.cache)")

st.sidebar.header('User Input Features')
selected_year = st.sidebar.selectbox('Year',
   list(reversed(range(mpg.model_year.min(),mpg.model_year.max()+1)))
   )

# Sidebar - origin
sorted_unique_origin = sorted(mpg.origin.unique())
selected_origin = st.sidebar.multiselect('origin', sorted_unique_origin, sorted_unique_origin)


if selected_year > 0 :
   mpg = mpg[mpg.model_year == selected_year]

if len(selected_origin) > 0:
   mpg = mpg[mpg.origin.isin(selected_origin)]

st.dataframe(mpg)

st.line_chart(mpg["mpg"])

st.bar_chart(mpg["mpg"])

fig, ax = plt.subplots()
sns.barplot(data=mpg, x="origin", y="mpg").set_title("origin 별 자동차 연비")
st.pyplot(fig)

pxh = px.histogram(mpg, x="origin", title="지역별 자동차 연비 데이터 수")
st.plotly_chart(pxh)

pxb = px.box(mpg, x="origin", y="mpg", title="지역별 자동차 연비 boxplot")
st.plotly_chart(pxb)
