import streamlit as st

st.title('Area Calculator')

s=st.number_input ("Input the side",0)
count=st.button ("Calculate")
if count:
  area=s*s
  st.write("The square area= ", area)
  st.success(f("The square area= {area}"))

