from flask import Flask, request, jsonify, make_repsonse
from flask_sqlalchemy import SQLAlcehmy
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_has, check_password_hash
import jwt
import datetime

app = FlasK(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'our_database_uri'
# This is used for JWT encryption
app.config['SECRET_KEY'] = 'your_secret_key'
# This is used for token expiration time
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(hours=1)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

@app.route('/login', methods=['POST'])
def login():
    # Get user inputs from the request
    username = request.json.get('username')
    password = request.json.get('password')

    # Find the user by username or email
    user = User.query.filter((User.username == username) | (User.email == username)).first()

    # Verify the user's credentials
    if user and check_password_hash(user.password, password):
        # Generate JWT token
        token = jwt.encode(
            {'user_id': user.id, 'exp': datetime.datetime.utcnow() + app.config['JWT_EXPIRATION_DELTA']},
            app.config['SECRET_KEY'],
            algorithm='HS256'
        )
        return jsonify({'token': token.decode('utf-8')})  # Return the token
    else:
        return jsonify({'error': 'Invalid username/email or password'}), 401

@app.route('/protected', methods=['GET'])
def protected():
    # Get the token from the Authorization header
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        return jsonify({'error': 'Missing authorization header'}), 401

    try:
        # Decode and verify the token
        payload = jwt.decode(auth_token, app.config['SECRET_KEY'], algorithms=['HS256'])

        # Retrieve the user from the database based on the user ID in the token payload
        user = User.query.get(payload['user_id'])
        if not user:
            return jsonify({'error': 'User not found'}), 404

        # User is authenticated, return protected data or perform authorized actions
        return jsonify({'message': 'Access granted for user: {}'.format(user.username)})
    except jwt.ExpiredSignatureError:
        return jsonify({'error': 'Token has expired'}), 401
    except jwt.InvalidTokenError:
        return jsonify({'error': 'Invalid token'}), 401

if __name__ == '__main__':
    app.run()

# When a user successfully logs in, a JWT token is generated, including the
# user's ID and an expiration time (1 hour in this case). The token is returned to the client

# For protected routes, such as '/protected' in this example, the client includes the token in
# the 'Authorization' headers as 'Bearer <token>'. The server decodes and verifies