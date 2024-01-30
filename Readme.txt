initiate .venv folder
    py -m venv .venv

activate .venv
    .venv\Scripts\activate

Install packages from requirements file
    py -m pip install -r requirements.txt

Prepare api keys
    - copy apikey.py.example and rename to apikey.py
    - fill in the api keys
    - do the same with .env.example

run the app with streamlit
    streamlit run app.py

