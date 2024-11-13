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
            Please analyse my CV in relation to this job description and provide a matching percentage score at the beginning (e.g., “Matching result: xx%”). Then, briefly explain (in 3-4 sentences) how you arrived at this percentage, focusing on key matching skills, qualifications, and experiences. Regardless of the matching result, encourage me to apply by explaining that candidates often apply successfully with less than perfect alignment and suggest any relevant transferable skills that could strengthen my application. Finally, recommend a few specific skills I might consider developing to increase my suitability for similar roles. My CV is
            """ + cv_content + "The job description is " + job_description

            # call the model to generate the answer
            with st.spinner('Generating answer...'):
                response = model.generate_content(prompt)
                st.write(response.text)

    except FileNotFoundError:
        st.write("Please upload your CV from uploader.")
