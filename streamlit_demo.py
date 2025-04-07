import os
from langchain_openai import ChatOpenAI
import streamlit as st


st.title("Ask me anything!")

with st.sidebar:
    st.title("Provide Your API Key")
    OPENAI_API_KEY = st.text_input("OpenAI API Key", type="password")

if not OPENAI_API_KEY:
    st.info("Please provide your OpenAI API key to continue.")
    st.stop()

llm = ChatOpenAI(model='gpt-4o', api_key=OPENAI_API_KEY)

question = st.text_input("Enter your question: ")

if question:
    response = llm.invoke(question)
    st.write(response.content)


