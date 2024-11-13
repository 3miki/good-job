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

# set up generative model
generation_config = {
  "temperature": 0.8, # small values for more deterministic output, range from 0.0 to 2.0
  "max_output_tokens": 1500, # maximum number of tokens to generate, max 128,000 tokens
  "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

# get file path for uploaded file
uploads_dir = os.path.join(os.getcwd(), "uploads/")
file_name = next((f for f in os.listdir(uploads_dir) if f), None)

if file_name is None:
    st.write("Please upload your CV from uploader.")
    st.stop() # stop the script

file_path = os.path.join(uploads_dir, file_name) if file_name else None
file_exists = os.path.exists(file_path)

if file_exists:
    try:
        with open(file_path, "rb") as f:
            # read pdf content
            if file_path.endswith(".pdf"):
                pdf_reader = PdfReader(f)
                cv_content = ""
                for page_num in range(len(pdf_reader.pages)):
                    page = pdf_reader.pages[page_num]
                    cv_content += page.extract_text()
        
            # read txt content
            elif file_path.endswith(".txt"):
                cv_content = f.read().decode("utf-8")

        # get job description
        job_description = st.text_area("Enter a job description here:", height=200)

        if len(job_description) == 0:
            st.write("Please enter a job description for analysis.")

        else:
            prompt = """
            Can you analyse my CV and this job description and give me a percentage how my skill match with the role? 
            Show the matching percentage in number at the beggining such as "Matching result: xx%", and explain why you reach the answer in 2-3 sentences. You should encourage me even if my skill is not adequate for the role, suggesting skill I might want to develop. My CV is
            """ + cv_content + "The job description is " + job_description

            # call the model to generate the answer
            with st.spinner('Generating answer...'):
                response = model.generate_content(prompt)
                st.write(response.text)

    except FileNotFoundError:
        st.write("Please upload your CV from uploader.")