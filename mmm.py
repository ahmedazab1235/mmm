import streamlit as st
import pandas as pd 


# Title
st.title("Hello World")

name = st.text_input("Enter your name", "Type Here...")

st.write(f"Hello {name}!")

upload = st.file_uploader("Upload a CSV file", type=["csv"])
if upload:
    df = pd.read_csv(upload)
    st.write("DataFrame:")
    st.dataframe(df.head())

    st.download_button(
        label="Download CSV",
        data=df.to_csv(index=False).encode('utf-8'),
        file_name='downloaded_data.csv',
        mime='text/csv'
    )