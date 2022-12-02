from flask import Flask, jsonify, request
from utils import is_valid_credit_card


app = Flask(__name__)


def is_credit_card_valid(creditCard):
    if creditCard.isdigit():
        if is_valid_credit_card(creditCard):
            print("The Credit card issued is valid ")
            return jsonify({"isValid": True}), 200
        else:
            print("The Credit card issued is invalid ")
            return jsonify({"isValid": False}), 200
    else:
        return (jsonify({"error": "Credit card number must be numeric"}), 400)

@app.route('/')
def home():
    return "CreditCard Validator"

@app.route('/api/validate/<string:creditCard>')
def validate_credit_card(creditCard):
    return is_credit_card_valid(creditCard)
    

@app.route('/api_v2/validate/')
def validate_credit_card_json():
    payload = request.get_json("creditCard")
    creditCard = payload['creditCard']
    return is_credit_card_valid(creditCard)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
