import streamlit as st
st.title("my first streamlit app")


name=st.text_input("enter your name")
if st.button("Submit"):
  st.write(f"Hello,{name}")


age=st.int_input("Enter ur age")
if st.button("submit"):
  st.write("Eligible to vote")
else:
  st.write("Not eligible to vote")
