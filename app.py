import streamlit as st
import pandas as pd
from datetime import datetime
import plotly.express as px

csv_file = 'data/data_science_salary.csv'

st.set_page_config(page_title='Advanced Visualization', layout = 'wide', page_icon=':bar_chart')

st.title(':red[Data Science] :blue[Salary Visualization]🤖', )

left_col, right_col = st.columns([1, 3])

@st.cache_data
def convert_csv_to_df(file_path):
    return pd.read_csv(file_path, index_col = 0)  

df = convert_csv_to_df(csv_file)
st.dataframe(df)

# SideBars
st.sidebar.header('Filter Section')

job_filter = st.sidebar.multiselect('Jobs Available', df.job_title.unique())
year_filter = st.sidebar.selectbox('Choose Year', df.work_year.unique())

button_clicked = st.sidebar.button('Display Chart')

if button_clicked:
    filtered_job = df[
        (df['job_title'].isin(job_filter)) & 
        (df['work_year'] == year_filter)
    ]

    fig1 = px.bar(filtered_job.groupby('job_title', as_index = False)['salary_in_usd'].mean(), x = 'job_title', y = 'salary_in_usd')

    fig1.update_layout(
        title = f'Average Salary Per Job Title for Year {year_filter}'
    )

    left_col.plotly_chart(fig1)