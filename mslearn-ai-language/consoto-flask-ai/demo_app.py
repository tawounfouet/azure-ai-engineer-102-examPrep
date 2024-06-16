from flask import Flask, render_template, request
import requests
import uuid
import json

app = Flask(__name__)

my_words = {"hello": "Привет"}


@app.route('/', methods=['GET', 'POST'])
def dict_page():
    if request.method == 'POST':
        word = request.form["word"].lower()
        return render_template('result.html', word=my_words[word])

    return render_template('dict.html')


@app.route('/dict', methods=['GET', 'POST'])
def result():
    return render_template('result.html')


@app.route('/translate', methods=['GET', 'POST'])
def index_post():
    if request.method == 'POST':

        original_text = request.form['word']
        target_language = "ru"
        print(original_text)
        key = "your_translator_key"
        endpoint = "https://api.cognitive.microsofttranslator.com/"
        location = "eastus"

        path = '/translate?api-version=3.0&'

        target_language_parameter = 'from=en&to=' + target_language

        constructed_url = endpoint + path + target_language_parameter

        headers = {
            'Ocp-Apim-Subscription-Key': key,
            'Ocp-Apim-Subscription-Region': location,
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
        }


        body = [{'text': original_text}]

        translator_request = requests.post(constructed_url, headers=headers, json=body)

        translator_response = translator_request.json()
        print(translator_response)
        translated_text = translator_response[0]['translations'][0]['text']

        return render_template('result.html', word=translated_text)
    else:
        return render_template('dict.html')




if __name__ == '__main__':
    app.run()