from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    elif request.method == 'POST':
        print("Sending request to Lambda")
        url = "https://11uawj4zrf.execute-api.us-east-1.amazonaws.com/datastream1/reddit-to-kafka"
        response = requests.post(url, json=request.json)
        return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)