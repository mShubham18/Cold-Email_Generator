import streamlit as st
st.title(" 📧 Want to Send a cold email ? Don't worry we gotchu !")
url_input = st.text_input("Enter a URL: ", value = "https://jobs.nike.com/job/R-39039")
submit_button = st.button("Submit")

if submit_button:
    st.code("Hello Hiring Manager, I am from CronAi",language="markdown")