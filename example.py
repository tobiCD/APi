import streamlit as st
import pandas as pd
import plotly.express as px

st.title("In Search for Happiness")
x=st.selectbox("Select the data for X - " ,
               ("GDP" ,"Happiness","Generously"))
y=st.selectbox("Select the data for y - " ,
                ("GDP","Happiness","Generously"))
df=pd.read_csv("happy.csv")
match  x:
    case "GDP":
        x_array=df["gdp"]
    case "Happiness":
        x_array=df["happiness"]

    case "Generously":
        x_array=df["generosity"]


match  y:
    case "GDP":
        y_array=df["gdp"]
    case "Happiness":
        y_array=df["happiness"]

    case "Generously":
        y_array=df["generosity"]


st.subheader(f"{x} and {y}")


figure=px.scatter(x=x_array , y=y_array,render_mode="SVG",labels={"x":x,"y":y})

st.plotly_chart(figure)



