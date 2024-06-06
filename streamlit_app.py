import streamlit as st
from streamlit_option_menu import option_menu

# 1. as sidebar menu
with st.sidebar:
    selected = option_menu("Menu", ["Circumference", 'Area', 'Volume'], 
        icons=['circle', 'square', 'box'], menu_icon="math", default_index=0)
    selected

#circumference
if (selected=='Circumference'):
  st.title('Circumference Calculator')

  s=st.number_input ("Input the side",0)
  count=st.button ("Calculate")
  if count:
    circumference=s*4
    st.write("The square circumference= ", circumference)
    st.success(f"The square circumference= {circumference}")
    st.success('This is a success message!', icon="✅")

#Area
if (selected=='Area'):
  st.title('Area Calculator')

  s=st.number_input ("Input the side",0)
  count=st.button ("Calculate")
  if count:
    area=s*s
    st.write("The square area= ", area)
    st.success(f"The square area= {area}")
    st.success('This is a success message!', icon="✅")
if (selected=='Volume'):
  st.title('Volume Calculator')

  s1=st.slider('Input length',0,100)
  s2=st.slider('Input width',0,100)
  s3=st.slider('Input height',0,100)
  
  count=st.button("Calculate Volume")
  if count:
    volume=s1*s2*s3
    st.write("The Volume is = ",volume)
    st.success(f"The Volume is = {volume}")
