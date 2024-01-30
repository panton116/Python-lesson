initiate .venv folder
    py -m venv .venv

activate .venv
    .venv\Scripts\activate

Install packages from requirements file
    py -m pip install -r requirements.txt

run the app with streamlit
    streamlit run app.py