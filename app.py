from flask import Flask, request, jsonify
from ml_model import train_and_predict

app = Flask(__name__)

@app.route('/predict_level', methods=['POST'])
def predict_level():
    data = request.get_json()

    question = data['question']

    predicted_level = train_and_predict(question)

    response = {'predicted_level': predicted_level}
    return jsonify(response)


@app.route('/k', methods=['GET'])
def predict_level1():

    return "hi this srk"



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
