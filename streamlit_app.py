
import streamlit
import pandas


streamlit.title('the new job')

streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔Kale, Spinach & Rocket Smoothie')
streamlit.text('🍌Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruit_selected=streamlit.multiselect("pick some fruits : ", list(my_fruit_list.index),['Avocado','Apple'])

my_fruit_select = my_fruit_list.loc[fruit_selected]

streamlit.dataframe(my_fruit_select)

streamlit.header('Fruityvice Fruit Advice!')

import requests
fruityvice_reponse=requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_reponse.json())
