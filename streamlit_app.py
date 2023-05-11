import streamlit 
import pandas 
import requests

streamlit.title('My Parents New Healthy Diner') 

streamlit.header('Breakfast Menu') 
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") 
my_fruit_list.set_index('Fruit', inplace = True)
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
streamlit.text('Dietary information...')
fruits_to_show = my_fruit_list.loc[fruits_selected, ['Serving_Size','Serving_Gram_Weight','Calories', 'Total_Fat_G','Total_Carbs_G)','Sugars_G','Protein_G']]
streamlit.dataframe(fruits_to_show)

for x in fruits_selected:
  fruityvice_response = requests.get(f"https://fruityvice.com/api/fruit/{x}")
  streamlit.dataframe(pandas.jason_normalize(fruityvice_response.json()))


