import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Experience Level', layout = 'wide', page_icon=':bar_chart')

st.title(':red[Average Salary] :blue[Based On Experience Level]')

left_col, center_col, right_col = st.columns([1, 2, 1])

df = st.session_state['df']

st.sidebar.header('Experience Level Visualizations')


def experience_level_avg_salary_per_year():
    experience_filter = st.sidebar.multiselect('Experience Levels', df.experience_level.unique())
    year_filter = st.sidebar.selectbox('Choose Year', df.work_year.unique())

    button_clicked = st.sidebar.button('Display_chart')

    if button_clicked:
        filtered_experience = df[
            (df['experience_level'].isin(experience_filter)) &
            (df['work_year'] == year_filter)
        ]

        fig1 = px.bar(filtered_experience.groupby('experience_level', as_index = False)['salary_in_usd'].mean(), x = 'experience_level', y = 'salary_in_usd')

        fig1.update_layout(
            title = f'Average Salary Per Job Title for Year {year_filter}'
        )
    
        with center_col:
            fig1


def experience_level_distribution_per_year():
    experience_filter = st.multiselect('Experience Level', df.experience_level.unique())
    year_filter = st.slider('Work Yr', min_value=int(df['work_year'].unique().min()), max_value=int(df['work_year'].unique().max()))

    button_clicked = st.button('Plot Chart')

    if button_clicked:
        filtered_experience = df[
            (df['experience_level'].isin(experience_filter)) & 
            (df['work_year'] == year_filter)
        ]

        experience_level_by_year = filtered_experience.groupby('work_year', as_index = False)['experience_level'].value_counts()
        fig2 = px.pie(data_frame = experience_level_by_year, names='experience_level', values = 'count')

        fig2.update_layout(
            title = f'Experience Level Count in {year_filter}'
        )       

        with center_col:
            fig2

if st.sidebar.checkbox('Get Experience Level Avg Salary Per Year'):
    experience_level_avg_salary_per_year()

experience_level_distribution_per_year() 