from flask import Flask, Response, request, jsonify,session, abort, redirect
from config import Config
from database import DBConnection
from models.Wordpress_profile import Wordpress_profile
from helper.format_profile_data import format_profiles
#imports for cognito
from flask_cognito_lib import CognitoAuth
from flask_cognito_lib.decorators import (
    auth_required,
    cognito_login,
    cognito_login_callback,
    cognito_logout,
)
from flask_cors import CORS
import json
import os
from dotenv import load_dotenv
from mysql.connector import pooling
from flask import Flask, session, abort, redirect, request
from pip._vendor import cachecontrol
import secrets
import json
import logging


app = Flask(__name__)
app.secret_key = os.environ.get("secret_key")

 #added for cognito details 
# Configuration required for CognitoAuth
app.config["AWS_REGION"]=os.environ.get("AWS_REGION")
app.config["AWS_COGNITO_USER_POOL_ID"] =os.environ.get("AWS_COGNITO_USER_POOL_ID")
app.config["AWS_COGNITO_DOMAIN"]= os.environ.get("AWS_COGNITO_DOMAIN")
app.config["AWS_COGNITO_USER_POOL_CLIENT_ID"] =os.environ.get("AWS_COGNITO_USER_POOL_CLIENT_ID")
app.config["AWS_COGNITO_USER_POOL_CLIENT_SECRET"] =os.environ.get("AWS_COGNITO_USER_POOL_CLIENT_SECRET")
app.config["AWS_COGNITO_REDIRECT_URL"] = os.environ.get("AWS_COGNITO_REDIRECT_URL")
app.config["AWS_COGNITO_LOGOUT_URL"]= os.environ.get("AWS_COGNITO_LOGOUT_URL")


# app.config["AWS_REGION"] = "us-east-2"
# app.config["AWS_COGNITO_USER_POOL_ID"] = "us-east-2_awNCF5k9A"
# app.config["AWS_COGNITO_DOMAIN"] = "https://ctpbackend.auth.us-east-2.amazoncognito.com"
# app.config["AWS_COGNITO_USER_POOL_CLIENT_ID"] = "53a307pmr0pajipnpjpie0ue72"
# app.config["AWS_COGNITO_USER_POOL_CLIENT_SECRET"] = "1os86h0fl0ir5mvffoi0umted2mqae572cgdh5slboc2g76vjirm"
# app.config["AWS_COGNITO_REDIRECT_URL"] = "http://localhost/callback"
# app.config["AWS_COGNITO_LOGOUT_URL"] = "http://localhost/login"


auth = CognitoAuth(app)
@app.errorhandler(404)
def page_not_found(error):
    return "invalid request", 404

@app.route('/api/profiles', methods=['GET'])
@auth_required()
def get_profiles():
    try:
        
        profiles = Wordpress_profile().get_all_profiles()
        formatted_profiles = format_profiles(profiles)
        response_data = json.dumps(formatted_profiles, indent=2)
        return Response(response_data, content_type='application/json')

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/profile/<uniqueId>', methods=['GET'])
@auth_required()
def get_profile(uniqueId):
    try:
        profile = Wordpress_profile().get_by_id(uniqueId)
        if profile:
            formatted_profile = format_profiles([profile])[0]
            response_data = json.dumps(formatted_profile, indent=2)
            return Response(response_data, content_type='application/json')
        else:
            return "Profile not found", 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/profile/<uniqueId>', methods=['PUT'])
@auth_required()
def update_profile(uniqueId):
    try:
        data = request.get_json()

        if not data:
            return "Invalid JSON data", 400

        returnData = Wordpress_profile.update_profile_by_id(uniqueId=uniqueId, data=data)
        return returnData["message"], returnData["status_code"]

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/profile', methods=['POST'])
@auth_required()
def create_profile():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400

        returnData = Wordpress_profile().create_profile(data=data)
        return returnData["message"], returnData["status_code"]

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/profile/<uniqueId>', methods=['DELETE'])
@auth_required()
def delete_profile(uniqueId):
    try:
        result = Wordpress_profile.delete_by_id(uniqueId)
        return result["message"], result["status_code"]
    except Exception as e:
        return jsonify({"error": str(e)}), 500


app.secret_key = os.environ.get("secret_key")


@app.route("/callback")
@cognito_login_callback
def callback():
    print("Inside callback route")
    return redirect("/protected_area")

@app.route("/logout")
@cognito_logout
def logout():
   # session.clear()
    return redirect("/login")

#@app.route("/login")
#@cognito_login
#def index():
 #   print("Before login redirection")
  #  return "Hello World <a href='/login-button'><button>Login</button></a>"

@app.route("/login")
@cognito_login
def login():
    code_verifier = secrets.token_urlsafe(100)  # Generate a code verifier
    session['code_verifier'] = code_verifier  # Store code verifier in the session

    auth_url, state = auth.authorization_url(
        code_verifier=code_verifier,  # Pass the code verifier
        scope="openid profile email",
    )
    return redirect(auth_url)

@app.route("/protected_area")
@auth_required()
def protected_area():
    # return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"
    return f"Hello! <br/> <a href='/logout'><button>Logout</button></a>"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)