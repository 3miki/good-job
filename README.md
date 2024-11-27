# good-job

### Overview
This app analyses job seeker skills against job descriptions, providing a match percentage and AI-driven encouragement to boost confidence. You can upload a CV file(PDF) or text using an uploader, then add a job description on to a dashboard page. Now, you will get a response with analysis!


### Technology
The main framework and tools used in this project are followings:
- Google generative AI model `Gemini 1.5 Flash`
- Streamlit


### How to set up

Step 1: Install dependancies
1. Download Package and Dependency Manager [(uv)](https://docs.astral.sh/uv/getting-started/installation/) package to organise package and versions.

The commands below are some of options you can use for installation in terminal. (Check more options on UV website)

mac: `curl -LsSf https://astral.sh/uv/install.sh | sh`

1. Run this command to install all dependancies in terminal.

`uv sync`

3. [Option] How to add packages or dependancies (add one by one)

`uv add <package name>`


Step 2: Set environment variables
You will need to mofidy .env example file according to your environment.

1. Set your Google API key.
Create your own API key [Google AI studio](https://aistudio.google.com/app/apikey) to use `gemini-flash-1.5`.

GOOGLE_API_KEY="<example-API-KEY>"

2. Rename the file name to .env
Remove 'example' from the file name.

Step 3: Run program files
To run the python from terminal using PDM and streamlit, use the following command:

`uv run streamlit run dashboard.py`


## TO DO
- Deloy a webpage and allow user to enter their API key.
- Use session state to store PDF data for the session.