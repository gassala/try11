import streamlit as st

st.title('Calculate Square Area')

s=st.number_input ("Input the side",0)
count=st.button ("Calculate the area")
if count:
  area=s*s
  st.write("The square area= ", area)

