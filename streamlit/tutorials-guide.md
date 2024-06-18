


## Create and activate environment using venv

```sh

python3.10 -m venv .venv


# Windows command prompt
.venv\Scripts\activate.bat

# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS and Linux
source .venv/bin/activate
```

## Install Streamlit in your environment
```sh

# In the terminal with your environment activated, type:
pip install streamlit


# Test that the installation worked by launching the Streamlit Hello example app:
streamlit hello

#If this doesn't work, use the long-form command:
python -m streamlit hello
```

## Basic concepts

You can also pass a URL to streamlit run! This is great when combined with GitHub Gists. For example
```sh
streamlit run https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py

# 
streamlit run 1_app.py