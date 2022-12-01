from flask import Flask, jsonify, request
from utils import is_valid_credit_card


app = Flask(__name__)

# isValid = is_valid_credit_card("49927398717")
# print(isValid)


@app.route('/')
def home():
    return "CreditCard Validator"


@app.route('/api_v1/validate/')
def validate_credit_card():
    payload = request.get_json("creditCard")

    creditCard = payload['creditCard']
    if creditCard.isdigit():
        if is_valid_credit_card(creditCard):
            print("The Credit card issued is valid ")
            return jsonify({"isValid": True}), 200
        else:
            print("The Credit card issued is invalid ")
            return jsonify({"isValid": False}), 200
    else:
        return (jsonify({"error": "Credit card number must be numeric"}), 400)

@app.route('/api_v2/validate/<string:creditCard>')
def validate_credit_card(creditCard):
    if creditCard.isdigit():
        if is_valid_credit_card(creditCard):
            print("The Credit card issued is valid ")
            return jsonify({"isValid": True}), 200
        else:
            print("The Credit card issued is invalid ")
            return jsonify({"isValid": False}), 200
    else:
        return (jsonify({"error": "Credit card number must be numeric"}), 400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
