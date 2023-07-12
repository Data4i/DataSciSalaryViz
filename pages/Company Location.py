import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title='Company Location', layout = 'wide', page_icon=':bar_chart')

st.title(':red[Average Salary] :blue[Based On The Company Locations]')

left_col, center_col, right_col = st.columns([1, 2, 1])