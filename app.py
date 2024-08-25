from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample user information
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        # Get data from the request
        data = request.json.get('data', [])
        
        # Separate numbers and alphabets
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        
        # Find the highest lowercase alphabet
        lowercase_alphabets = [ch for ch in alphabets if ch.islower()]
        highest_lowercase = max(lowercase_alphabets) if lowercase_alphabets else None
        
        # Build the response
        response = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": [highest_lowercase] if highest_lowercase else []
        }
        return jsonify(response), 200
    
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 500

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
