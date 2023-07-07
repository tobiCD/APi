import streamlit as st
import plotly.express as px

st.header("Wearther Forecast for the Next Days")
place=st.text_input(label="Place :")
days=st.slider(label="Forecast Days" ,min_value=1,max_value=5,help="Select the number of the Forecast Days")
option=st.selectbox("Select data to view ",options=("Temperature"
                    ,"Sky"))
st.subheader(f"{option} for the next 2 days in {days}")
def get_data(days):
    Date=["2022-25-10","2022-26-10","2022-07-10"]
    Temperature=[10,11,15]
    Temperature=[days* i for i in Temperature]
    return Date,Temperature
t,x=get_data(days)
figure=px.line(x=t,y=x,render_mode="SVG",labels={"x":"Date","y":"Temperature (C)"})
st.plotly_chart(figure)