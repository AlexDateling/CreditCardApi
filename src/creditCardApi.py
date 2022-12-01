from flask import Flask, jsonify, request
from utils import isAValidCreditCard

app = Flask(__name__)

# isValid = isAValidCreditCard("49927398717")
# print(isValid)

@app.route('/')
def home():
    return "CreditCard Validator"

@app.route('/api/validate/')
def validate_credit_card():
    payload = request.get_json("creditCard")
    
    creditCard = payload['creditCard']
    if creditCard.isdigit():
        if isAValidCreditCard(creditCard):
            print("The Credit card issued is valid ")
            return jsonify({"isValid": True}), 200
        else:
            print("The Credit card issued is invalid ")
            return jsonify({"isValid": False}), 200
    else:
        return "Invalid Input", 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)