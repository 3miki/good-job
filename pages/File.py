"""
# to manage uploaded file
"""

import streamlit as st
import os

st.markdown("# File 📤")
st.sidebar.markdown("# File 📤")

uploads_dir = os.path.join(os.getcwd(), "uploads/")
file_name = next((f for f in os.listdir(uploads_dir) if f), None)

if file_name is None:
  st.write("Please upload your CV from uploader.")
  st.stop() # stop the script

file_path = os.path.join(uploads_dir, file_name) if file_name else None
file_exists = os.path.exists(file_path)

if file_exists:
  st.write("Saved file:", file_name)

  # to delete the file
  if st.button("Delete File"):
    try:
      os.remove(file_path)
      st.write("File deleted successfully.")
    except FileNotFoundError:
      st.write("No file uploaded yet.")

    file_exists = False

  if not file_exists:
    st.write("No file uploaded yet.")

else:
  st.write("No file uploaded yet.")

