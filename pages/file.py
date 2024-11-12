"""
# to manage uploaded file
"""

import streamlit as st
import os

st.markdown("# File 🎈")
st.sidebar.markdown("# File 🎈")

file_path = os.path.join(os.getcwd(), "uploads/file-1.pdf")

# uploads_dir = os.path.join(os.getcwd(), "uploads")
# file_name = next((f for f in os.listdir(uploads_dir) if f.startswith('file-1')), None)
# file_path = os.path.join(uploads_dir, file_name) if file_name else None
# file_exists = os.path.exists(file_path)

if file_path:
  st.write("Saved file:", file_path) 
# if file_exists:
  # st.write("Saved file:", file_name)
  # to delete the file
  if st.button("Delete file"):
    try:
      os.remove(file_path)
      st.write("File deleted successfully.")
    except FileNotFoundError:
      st.write("No file uploaded yet.")

  #   file_exists = False

  # if not file_exists:
  #   st.write("No file uploaded yet.")

else:
  st.write("No file uploaded yet.")

