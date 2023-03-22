import whisper
import streamlit as st
import requests
import os

def save_file(file):
    with open(file.name, "wb") as f:
        f.write(file.getbuffer())
    return file.name

st.set_page_config(page_title="Summarizor", page_icon=":fire:")

st.title("Transcript summarizer 🔮")

st.subheader("Upload your audio file and we will summarize it for you!")

with st.form("hi"):
    email = st.text_input("Enter your Email")
    file = st.file_uploader("Upload your audio file .wav", type="wav")

    if st.form_submit_button("Summarize"):
        if file and email:
            with st.spinner("Generating magic..."):
                file_path = save_file(file)
                model = whisper.load_model("base")
                result = model.transcribe(file_path, fp16=False)
                # st.write(result["text"])
                # st.write(result)

                webhook_url = "https://hooks.zapier.com/hooks/catch/14830394/331xres/"
                payload = {"email": email, "result": result["text"]} 
                requests.post(webhook_url, json=payload)
                st.write("Done!")

                os.remove(file_path)
        elif not file:
            st.write("Please upload your file first!")
        else :
            st.write("Please enter your email first!")