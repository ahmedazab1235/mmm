import streamlit as st
from transformers import pipeline


# Load the classification pipeline with the specified model
pipe = pipeline("text-classification", model="tabularisai/multilingual-sentiment-analysis")

st.title("text classification App")

text = st.text_input("Enter your text", "I love this product! It's amazing and works perfectly.")

result = pipe(text)

# Print the result
st.write(result[0]['label'])
st.write(result[0]['score'])

