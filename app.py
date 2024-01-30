import os
from apikey import OpenAIapikey,Googleapikey

import streamlit as st
from langchain.llms import OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

# os.environ['OPENAI_API_KEY']=OpenAIapikey
os.environ['GOOGLE_API_KEY']=Googleapikey

# App framework
st.title('Some LLM Langchain practice')
prompt = st.text_input('Please enter prompt here')

# llm
# llm = OpenAI(temperature=0.9)
llm = ChatGoogleGenerativeAI(model="gemini-pro")
# llm.invoke("Sing a ballad of LangChain.")

# Show stuff to the screen if there's a prompt
if prompt:
    response = llm.invoke(prompt)
    st.write(response.content)
    