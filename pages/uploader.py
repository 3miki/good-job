"""
# to uplodad file
"""

import streamlit as st
import os

st.markdown("# Uploader 📤")
st.sidebar.markdown("# Uploader 📤")

# upload by pdf file
st.write("Upload your CV (PDF or text) to get started!")
st.write("Please note that this app uses Gemini model so consider not to upload your personal data to keep your privacy. Check Google’s AI and privacy policy for more information. You can also enter texts from your CV.")
uploaded_file = st.file_uploader("Choose a file (PDF only)", type=["pdf"])

# check if pdf file has been uploaded
if uploaded_file:
    file_name = "CV_file.pdf"
    dir_file_name = "uploads/" + file_name

    if st.button("Save File") and dir_file_name:
        file_path = os.path.join(os.getcwd(), dir_file_name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("File saved successfully as " + file_name + "!")
        
        # delete text file if pdf file is uploaded
        text_file_path = os.path.join(os.getcwd(), "uploads/Text_file.txt")
        if os.path.exists(text_file_path):
            os.remove(text_file_path)
            st.warning("Text file deleted as PDF file is uploaded.")

# upload by text
uploaded_text = st.text_area("Or add your CV texts here:", height=300)
file_name = "Text_file.txt"
dir_file_name = "uploads/" + file_name

if st.button("Save Text"):
    if uploaded_text:
        file_path = os.path.join(os.getcwd(), dir_file_name)
        with open(file_path, "wb") as f:
            f.write(uploaded_text.encode("utf-8"))
        st.success("File saved successfully as " + file_name + "!")
        
        # delete pdf file if text file is uploaded
        pdf_file_path = os.path.join(os.getcwd(), "uploads/CV_file.pdf")
        if os.path.exists(pdf_file_path):
            os.remove(pdf_file_path)
            st.warning("PDF file deleted as text file is uploaded.")