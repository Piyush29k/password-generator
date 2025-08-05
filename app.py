from flask import Flask, render_template, request, jsonify
import secrets
import string

app = Flask(__name__)

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "❌ Please select at least one character type."

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    length = int(data['length'])
    upper = data['upper']
    lower = data['lower']
    digits = data['digits']
    symbols = data['symbols']

    password = generate_password(length, upper, lower, digits, symbols)
    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)
