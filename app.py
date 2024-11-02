from flask import Flask, render_template, request, jsonify
from model import predict_spam  

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/predict', methods=['POST'])
def predict():
    urls = request.json['urls']  
    predictions = {url: predict_spam(url) for url in urls}
    return jsonify(predictions)

if __name__ == '__main__':
    app.run(debug=True)