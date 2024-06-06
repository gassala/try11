import streamlit as st
from streamlit_option_menu import option_menu
# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Main Menu", ["Circumference", 'Area', 'Volume'], 
        icons=['round', 'square', 'box'], menu_icon="cast", default_index=1)
    selected


st.title('Area Calculator')

s=st.number_input ("Input the side",0)
count=st.button ("Calculate")
if count:
  area=s*s
  st.write("The square area= ", area)
  st.success(f"The square area= {area}")
  st.success('This is a success message!', icon="✅")

