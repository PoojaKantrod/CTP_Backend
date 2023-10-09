import os
import json
import pathlib
import logging
import requests
from pip._vendor import cachecontrol
from google.oauth2 import id_token
import google.auth.transport.requests
from google_auth_oauthlib.flow import Flow
from flask import Flask, Response, request, jsonify, session, abort, redirect

from config import Config
from database import DBConnection
from models.Wordpress_profile import Wordpress_profile
from helper.format_profile_data import format_profiles


app = Flask(__name__)


@app.errorhandler(404)
def page_not_found(error):
    return "invalid request", 404


@app.route('/api/profiles', methods=['GET'])
def get_profiles():
    try:
        profiles = Wordpress_profile().get_all_profiles()
        formatted_profiles = format_profiles(profiles)
        response_data = json.dumps(formatted_profiles, indent=2)
        return Response(response_data, content_type='application/json')

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/profile/<uniqueId>', methods=['GET'])
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
def delete_profile(uniqueId):
    try:
        result = Wordpress_profile.delete_by_id(uniqueId)
        return result["message"], result["status_code"]
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Google OAUTH Configuration
logging.basicConfig(level=logging.DEBUG)  
logger = logging.getLogger(__name__)

app.secret_key = Config.GOOGLE_AUTH_SECRET_KEY

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  

GOOGLE_CLIENT_ID = Config.GOOGLE_CLIENT_ID
client_secrets_file = os.path.join(pathlib.Path(__file__).parent, "client_secret.json")

flow = Flow.from_client_secrets_file(
    client_secrets_file=client_secrets_file,
    scopes=["https://www.googleapis.com/auth/userinfo.profile", "https://www.googleapis.com/auth/userinfo.email", "openid"],
    redirect_uri="http://localhost/callback"
)

def login_is_required(function):
    def wrapper(*args, **kwargs):
        if "google_id" not in session:
            return abort(401)  
        else:
            return function()
    return wrapper

@app.route("/login-button")
def login():
    authorization_url, state = flow.authorization_url()
    session["state"] = state  
    return redirect(authorization_url)

@app.route("/callback")
def callback():
    try:
        flow.fetch_token(authorization_response=request.url)
        logger.debug("Fetched token successfully: %s", flow.credentials.token)  # Log the token

        request_session = requests.session()
        cached_session = cachecontrol.CacheControl(request_session)
        token_request = google.auth.transport.requests.Request(session=cached_session)

        id_info = id_token.verify_oauth2_token(
            id_token=flow.credentials._id_token,
            request=token_request,
            audience=GOOGLE_CLIENT_ID
        )

        logger.debug("ID Token details: %s", id_info)  

        session["google_id"] = id_info.get("sub")
        session["name"] = id_info.get("name")

    except google.auth.exceptions.InvalidValue as e:
        logger.error("Token validation failed: %s", e)  
        return "Token has expired. Please <a href='/login'>login again</a>."
    except Exception as e:  
        logger.error("An error occurred: %s", e)
        return "An error occurred. Please try again."

    return redirect("/protected_area")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")

@app.route("/login")
def index():
    return "Hello World <a href='/login-button'><button>Login</button></a>"

@app.route("/protected_area")
@login_is_required
def protected_area():
    return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"

if __name__ == '__main__':
    app.run(host=Config.FLASK_HOST, port=Config.FLASK_PORT, debug=True)