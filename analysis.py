import streamlit as st
import pandas as pd
from streamlit import columns

df = pd.read_csv("Automobile.csv")
st.dataframe(df)


st.bar_chart(data=df,x="company",y="mileage")
st.line_chart(df["length"])