
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

#create the repetable code block (caled function)
def get_fruityvice_data(this_fruit_choise):
    fruityvice_reponse=requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choise)
    fruityvice_normalized = pandas.json_normalize(fruityvice_reponse.json())
    return fruityvice_normalized

#new section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
try:
  fruit_choise = streamlit.text_input('what fruit would you like information about ?')
  if not fruit_choise:
    streamlit.error("Please select a fruit to get information.")
  else:
   back_from_function = get_fruityvice_data(fruit_choise)
   streamlit.dataframe(back_from_function)                
except URLError as e:
        streamlit.error()                    
                
#streamlit.write('The user entered', fruit_choise)




streamlit.header("The fruit load list contains :")
#snowflake-related functions
def get_fruit_load_list():
       with my_cnx.cursor() as my_cur:
            my_cur.execute("select * from fruit_load_list")
            return my_cur.fetchall()
        
#add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows = get_fruit_load_list()
    streamlit.dataframe(my_data_rows)   



#streamlit.stop()

#Allow the end user to add a fruit to the list
def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values ('from streamlit')")
        return "Thank you for adding "+new_fruit


add_my_fruit =streamlit.text_input('what fruit would you like to add ?' )
if streamlit.button('Add a Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake(add_my_fruit)
    streamlit.text(back_from_function)
    

