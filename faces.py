import streamlit as st
import pandas as pd

st.title("Attendance Tracker")

df = pd.read_csv("Attendance.csv")
st.table(df)