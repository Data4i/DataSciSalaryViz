import streamlit as st
import pandas as pd
import plotly.express as px

csv_file = 'data/data_science_salary.csv'

st.set_page_config(page_title='Advanced Visualization', layout = 'wide', page_icon=':bar_chart')

st.title(':red[Data Science] :blue[Salary Visualization]🤖')

left_col, right_col = st.columns([1, 3])


@st.cache_data
def convert_csv_to_df(file_path):
    return pd.read_csv(file_path, index_col = 0)  

df = convert_csv_to_df(csv_file)

# Initialization
if 'df' not in st.session_state:
    st.session_state['df'] = df

st.dataframe(df)

