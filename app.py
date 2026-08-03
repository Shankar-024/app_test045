import streamlit as st
st.title("my first streamlit app")


name=st.text_input("enter your name")
if st.button("Submit"):
  st.write(f"Hello,{name}")

age = st.number_input("Enter your age")
if st.button("Check Eligibility"):
    if age >= 18:
        st.success("Eligible to vote")
    else:
        st.error("Not eligible to vote")
