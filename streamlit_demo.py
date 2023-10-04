import streamlit as st

st.title("Welcome to streamlit")

if st.checkbox("Display_widget"):
  # display the text if the checkbox returns True value
  st.text("Showing the widget")

status = st.radio("Select Gender: ", ('Male', 'Female'))

if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")
