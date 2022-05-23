
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

fruit_choise =streamlit.text_input('what fruit would you like information about ? ','kiwi')
streamlit.write('The user entered', fruit_choise)

import requests
fruityvice_reponse=requests.get("https://fruityvice.com/api/fruit/"+fruit_choise)


#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_reponse.json())
#output it the screen as a table
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select current_user(), current_account(), current_region()")
my_data_row = my_cur.fetchone()
streamlit.text("hello from snowflake")
streamlit.text(my_data_row)
