

```sh
pip install -U pip setuptools wheel
pip install -U spacy
python -m spacy download en_core_web_sm

```


## spaCy 101: Everything you need to know


## Streamlit Spacy
```sh
# https://github.com/explosion/spacy-streamlit/tree/master

pip install spacy-streamlit
python -m spacy download en_core_web_sm

touch app.py

streamlit run app.py
