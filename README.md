# good-job

### Overview
- add


### Technology
The main framework and tools used in this project are followings:
- Google generative AI model `Gemini 1.5 Flash`
- Streamlit


### How to set up

Step 1: Install dependancies
1. Download Package and Dependency Manager [(PDM)](https://pdm-project.org/en/latest/) package to organise package and versions.

The commands below are some of options you can use for installation in terminal. (Check more options on PDM website)

`brew install pdm` or 
`pip install --user pdm`

2. Run this command to install all dependancies in terminal.

`pdm install`

3. [Option] How to add packages or dependancies (add one by one)

`pdm add <package name>`


Step 2: Set environment variables
You will need to mofidy .env example file according to your environment.

1. Set your Google API key.
Create your own API key [Google AI studio](https://aistudio.google.com/app/apikey) to use `gemini-flash-1.5`.

GOOGLE_API_KEY="<example-API-KEY>"

2. Rename the file name to .env
Remove 'example' from the file name.

Step 3: Run program files
To run the python from terminal using PDM and streamlit, use the following command:

`pdm run streamlit run dashboard.py`