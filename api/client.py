import requests
import streamlit as st

def get_openai_response(input_text):
    try:
        response = requests.post("http://localhost:5000/essayyyy/invoke", json={'input':{'topic':input_text}})
        return response.json()['output']['content']
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")

def get_ollama_response(input_text):
    try:
        response = requests.post("http://localhost:5000/poemmmmm/invoke", json={'input':{'topic':input_text}})
        return response.json()['output']['content']
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")

st.title("Langchain demo with OpenAI and Llama2")
input_text1 = st.text_input("Write an essay on")
input_text2 = st.text_input("Write a poem on")


if input_text1:
    st.write(get_openai_response(input_text1))


if input_text2:
    st.write(get_ollama_response(input_text2))