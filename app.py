import streamlit as st
from model import get_response

st.title("Medi Bot")

user_question = st.text_input("Ask a question:")

if st.button("Submit"):

    response = get_response(user_question)
    
    st.write(f"{response}")
