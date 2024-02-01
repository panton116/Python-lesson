import os
from apikey import OpenAIapikey,Googleapikey

import streamlit as st
from langchain.llms import OpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# os.environ['OPENAI_API_KEY']=OpenAIapikey
os.environ['GOOGLE_API_KEY']=Googleapikey

# App framework
st.title('Some LLM Langchain practice')
prompt = st.text_input('Please enter prompt here')

# Prompt templates
title_template = PromptTemplate(
    input_variables=['topic'],
    template='write me a youtube video title about {topic}'
)

# llm
# llm = OpenAI(temperature=0.9)
llm = ChatGoogleGenerativeAI(model="gemini-pro")
# llm.invoke("Sing a ballad of LangChain.")
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True)

# Show stuff to the screen if there's a prompt
if prompt:
    response = title_chain.run(prompt)
    st.write(response)
    