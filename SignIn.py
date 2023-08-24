from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/signin', methods=['POST'])
def sign_in():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Perform sign-in logic and return response
    if username == 'user' and password == 'pass':
        response = {'message': 'Sign-in successful'}
    else:
        response = {'message': 'Sign-in failed'}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
