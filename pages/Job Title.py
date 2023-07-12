import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Job Title', layout = 'wide', page_icon=':bar_chart')

st.title(':red[Average Salary] :blue[Based On Job Titles]')

left_col, center_col, right_col = st.columns([1, 2, 1])


df = st.session_state['df']

# SideBars
st.sidebar.header('Filter Section')

st.sidebar.markdown('## Salary Of Job Titles Every Year')


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


    job_title_by_year = filtered_job.groupby('work_year', as_index = False)['job_title'].value_counts()
    fig2 = px.pie(data_frame = job_title_by_year, names='job_title', values = 'count')

    fig2.update_layout(
        title = f'Job Title Count in {year_filter}'
    )

    with center_col:
        fig1
        fig2


st.sidebar.markdown('## Remote Ratio For Each Jobs Every Year')

remote_job_filter = st.sidebar.selectbox('Jobs Available', df.job_title.unique())
remote_year_filter = st.sidebar.multiselect('Choose Year', df.work_year.unique())

remote_button_clicked = st.sidebar.button('Display')

if remote_button_clicked:
    remote_filtered_job = df[
        (df['job_title'] == remote_job_filter) &
        (df['work_year'].isin(remote_year_filter))
    ]

    filtered_data = remote_filtered_job[['work_year', 'remote_ratio']]

    grouped_data = filtered_data.groupby(['work_year', 'remote_ratio']).size().reset_index(name='count')

    fig3 = px.bar(grouped_data, x='work_year', y='count', color='remote_ratio', barmode='stack')

    fig3.update_layout(
        xaxis_title='Work Year',
        yaxis_title='Counts',
        title='Bar of Remote Ratio by Work Year'
    )

    with center_col:
        fig3

