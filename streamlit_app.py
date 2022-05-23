
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError


streamlit.title('the new job')

streamlit.header('🥣Breakfast Menu')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🐔Kale, Spinach & Rocket Smoothie')
streamlit.text('🍌Hard-Boiled Free-Range Egg')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

fruit_selected=streamlit.multiselect("pick some fruits : ", list(my_fruit_list.index),['Avocado','Apple'])

my_fruit_select = my_fruit_list.loc[fruit_selected]

streamlit.dataframe(my_fruit_select)

streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choise =streamlit.text_input('what fruit would you like information about ?)
  if not fruit_choise:
    streamlit.error(Please select a fruit to get information.")
  else:
    fruityvice_reponse=requests.get("https://fruityvice.com/api/fruit/"+fruit_choise)
    fruityvice_normalized = pandas.json_normalize(fruityvice_reponse.json())
    streamlit.dataframe(fruityvice_normalized)                
except URLError as e:
        streamlit.error()                    
                
#streamlit.write('The user entered', fruit_choise)


streamlit.stop()


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("*** from snowflake *** ")
streamlit.header("The fruit load list contains :")
streamlit.dataframe(my_data_rows)


add_my_fruit =streamlit.text_input('what fruit would you like to add ? ','kiwi')
streamlit.write('Thank you for adding ', add_my_fruit)

my_cur.execute("insert into fruit_load_list values ('from streamlit')")
