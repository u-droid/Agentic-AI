import requests
import traceback
import streamlit as st

def get_groq_response(input_text, language="french"):
    json_body = {
      "input": {
        "language": language,  
        "text": input_text
      }
    }
    response=requests.post("http://127.0.0.1:8000/chain/invoke",json=json_body)
    print(response.json())
    return response.json()

# ## Streamlit app
st.title("LLM Application Using LCEL")
language = st.selectbox("Select the language to translate to", ["french", "spanish", "german", "italian","hindi"])
input_text = st.text_input("Enter the text you want to convert to the selected language")


if input_text:
    st.write(get_groq_response(input_text, language=language))