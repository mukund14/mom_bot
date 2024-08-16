import streamlit as st
from transformers import pipeline, set_seed

# Load the GPT model and set a seed for reproducibility
model = pipeline("text-generation", model="gpt-2")
set_seed(42)

def mom_bot(prompt, max_length=100):
    mom_prompt = (
        "You're doing great, sweetie! Remember to take care of yourself. " 
        "Now, about your question: "
        + prompt
    )
    response = model(mom_prompt, max_length=max_length, num_return_sequences=1)
    return response[0]['generated_text']

# Streamlit app interface
st.title("MOM Bot 🤗")
st.write("Ask MOM anything, and she'll give you some comforting advice!")

user_input = st.text_input("What's on your mind?", "")

if user_input:
    response = mom_bot(user_input)
    st.write(response)
