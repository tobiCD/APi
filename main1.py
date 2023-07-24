import streamlit as st
import plotly .express as px
from backend import get_data
st.title("Weather forecast for the next few days ")
place=st.text_input("Place")
days=st.slider("Forecast",max_value=5 , min_value=1 ,help="Select the Number of Forecast Days")
option=st.selectbox("Select Data to view ",options=("Temperature","Sky"))
st.subheader(f"{option}for the next {days} days in {place}")
if place:
    try:
        filtered_data = get_data(place, days)
        if option=="Temperature":
            data_tem = [dict['main']['temp'] for dict in filtered_data]
            data_tem=[x/10 for x in data_tem]
            finish=[round(number ,2 ) for number in data_tem]
            Date =[dict['dt_txt']for dict in filtered_data]
            config=px.line(x=Date,y=finish , labels={"X": "Date" , "y":"Temperature"})
            st.plotly_chart(config)
        if option=="Sky":
            images={"Clear":"static/clear.png" , "Clouds":"static/cloud.png","Rain":"static/rain.png","Snow":"static/snow.png"}
            data_sky=[dict['weather'][0]['main'] for dict in filtered_data]
            x=[images[condition] for condition in data_sky]
            print(data_sky)
            st.image(x ,width=115)

    except KeyError:
        st.write("That place is not exist")