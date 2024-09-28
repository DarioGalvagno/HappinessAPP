import streamlit as st
import plotly.express as px
import pandas as pd

st.title("MapInsight")
option_x = st.selectbox("Select the data for the X-axis",("GDP","Happiness","Generosity","Corruption","Social Support")
                        , index=1)
option_y = st.selectbox("Select the data for the Y-axis",("GDP","Happiness","Generosity","Corruption","Social Support"))
st.subheader(f"This is the correlation between {option_x} and {option_y}")



df = pd.read_csv("happy.csv")
if option_x == "Happiness":
    x_array = df["happiness"]
if option_x =="GDP":
    x_array = df["gdp"]
if option_x =="Generosity":
     x_array = df["generosity"]
if option_x == "Corruption":
    x_array = df["corruption"]
if option_x == "Social Support":
    x_array = df["social_support"]
if option_x == "Freedom to make life choices":
    x_array = df["freedom_to_make_life_choices"]
if option_x == "Life Expectancy":
    x_array = df["life_expectancy"]

if option_y == "Happiness":
    y_array = df["happiness"]
if option_y =="GDP":
    y_array = df["gdp"]
if option_y =="Generosity":
    y_array = df["generosity"]
if option_y == "Corruption":
    y_array = df["corruption"]
if option_y == "Social Support":
    y_array = df["social_support"]
if option_y == "Freedom to make life choices":
    y_array = df["freedom_to_make_life_choices"]
if option_y == "Life Expectancy":
    y_array = df["life_expectancy"]

figure = px.scatter(x=x_array,y=y_array,labels = {"x": option_x, "y": option_y})
st.plotly_chart(figure)



st.title(f"A Map of Global {option_x} By Country")

figure_map = px.choropleth(df,
                        locations="country",  # Assuming you have a "country" column
                        locationmode="country names",
                        color=option_x.lower(),  # Use the lowercase column names from your dataset
                        hover_name="country",  # Display country name on hover
                        color_continuous_scale=px.colors.sequential.Inferno)
figure_map.update_layout(
    width=1000,  # Adjust the width
    height=700   # Adjust the height
)
st.plotly_chart(figure_map)

st.markdown('This app is created by **<span style="color:darkblue;">Dario Galvagno</span>**', unsafe_allow_html=True)