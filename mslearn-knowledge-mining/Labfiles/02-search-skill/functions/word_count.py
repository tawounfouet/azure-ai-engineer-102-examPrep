import re
from collections import Counter
from typing import List, Dict

def main(req):
    context_log('Python HTTP trigger function processed a request.')

    if req.get_json() and 'values' in req.get_json():
        vals = req.get_json()['values']

        # Array of stop words to be ignored
        stopwords = ['', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 
        "youre", "youve", "youll", "youd", 'your', 'yours', 'yourself', 
        'yourselves', 'he', 'him', 'his', 'himself', 'she', "shes", 'her', 
        'hers', 'herself', 'it', "its", 'itself', 'they', 'them', 
        'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 
        'this', 'that', "thatll", 'these', 'those', 'am', 'is', 'are', 'was',
        'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 
        'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 
        'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 
        'about', 'against', 'between', 'into', 'through', 'during', 'before', 
        'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 
        'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 
        'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 
        'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 
        'only', 'own', 'same', 'so', 'than', 'too', 'very', 'can', 'will',
        'just', "dont", 'should', "shouldve", 'now', "arent", "couldnt", 
        "didnt", "doesnt", "hadnt", "hasnt", "havent", "isnt", "mightnt", "mustnt",
        "neednt", "shant", "shouldnt", "wasnt", "werent", "wont", "wouldnt"]

        res = {"values": []}

        for rec in vals:
            # Get the record ID and text for this input
            resVal = {"recordId": rec['recordId'], "data": {}}
            txt = rec['data']['text']

            # remove punctuation and numerals
            txt = re.sub(r'[^ A-Za-z_]', '', txt).lower()

            # Get an array of words
            words = txt.split()

            # count instances of non-stopwords
            wordCounts = Counter(word for word in words if word not in stopwords)

            # Convert wordcounts to an array
            topWords = sorted(wordCounts.items(), key=lambda item: item[1], reverse=True)

            # Get the first ten words from the first array dimension
            resVal['data']['text'] = [word for word, count in topWords[:10]]

            res["values"].append(resVal)

        context_res = {
            "body": res,
            "headers": {
                'Content-Type': 'application/json'
            }
        }

    else:
        context_res = {
            "status": 400,
            "body": {"errors": [{"message": "Invalid input"}]},
            "headers": {
                'Content-Type': 'application/json'
            }
        }
    
    return context_res

# Helper function to simulate context log
def context_log(message):
    print(message)

# Example usage
if __name__ == "__main__":
    import json
    from flask import Flask, request, jsonify

    app = Flask(__name__)

    @app.route('/', methods=['POST'])
    def handle_request():
        response = main(request)
        return jsonify(response['body']), response.get('status', 200), response['headers']

    # Start the Flask server
    app.run(debug=True)
