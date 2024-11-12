"""
# to uplodad file
"""

import streamlit as st
import os

st.markdown("# Uploader 🎈")
st.sidebar.markdown("# Uploader 🎈")

# st.text_input("Your name", key="name")
# st.session_state.name

uploaded_file = st.file_uploader("Choose a file", type=["txt", "pdf"])

# check if file has been uploaded
if uploaded_file is not None:
    # st.write("Filename:", uploaded_file.name)
    # st.write("File size:", uploaded_file.size, "bytes")
    # st.write("File type:", uploaded_file.type)

    # if it's pdf
    if uploaded_file.type in ["pdf"]:
        file_name = "uploads/file-1.pdf"
        st.image(uploaded_file, caption="Uploaded PDF", use_column_width=True)

    # # if it's text file
    # elif uploaded_file.type == "text/plain":
    #     file_name = "uploads/file-1.txt"
    #     content = uploaded_file.read().decode("utf-8")
    #     st.text(content)

    if st.button("Save File"):
        file_path = os.path.join(os.getcwd(), "uploads/file-1.pdf")
        # file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success("File saved successfully as 'file-1'!")