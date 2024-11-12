import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from pypdf import PdfReader

load_dotenv()

st.title('Good Job 🎈')

# set up API key
google_api_key = os.environ.get("GOOGLE_API_KEY")
genai.configure(api_key=google_api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# get file path for uploaded file
file_path = os.path.join(os.getcwd(), "uploads/file-1.pdf")

# uploads_dir = os.path.join(os.getcwd(), "uploads")
# file_name = next((f for f in os.listdir(uploads_dir) if f.startswith('file-1')), None)
# file_path = os.path.join(uploads_dir, file_name) if file_name else None
# print(file_path)

# file_exists = os.path.exists(file_path)

# if file_exists:

try:
    with open(file_path, "rb") as f:
        # read pdf content
        if file_path.endswith(".pdf"):
            pdf_reader = PdfReader(f)
            cv_content = ""
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                cv_content += page.extract_text()
            # to test: print extracted pdf content
            print(cv_content)
        
        # # read txt content
        # elif file_path.endswith(".txt"):
        #     cv_content = f.read().decode("utf-8")
        #     # to test: print extracted txt content
        #     print(cv_content)

    # get job description from user
    job_description = st.text_input("Enter a job description: ")

    if len(job_description) == 0:
        st.write("Please enter a job description for analysis.")

    else:
        prompt = """
        Can you analyse my cv and this job description and give me a percentage how my skill match with the role? 
        Show the matching percentage in number at the beggining such as "Matching result: , and explain why you reach the answer in 2-3 sentences. You should encourage me even if my skill is not adequate for the role, suggesting skill I might want to develop. My cv is
        """ + cv_content + "The job description is " + job_description

        # call the model to generate the answer
        with st.spinner('Generating answer...'):
            response = model.generate_content(prompt)
            st.write(response.text)

except FileNotFoundError:
# else:
    st.write("Please upload your CV from uploader.")