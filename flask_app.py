import json
from flask import Flask, Response, request, jsonify
from iconMapping import getIconUrl
from database import DBConnection
from models import Wordpress_profile

from iconMapping import getIconUrl
from dotenv import load_dotenv
from mysql.connector import pooling
import pathlib
import requests
from flask import Flask, session, abort, redirect, request
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol
import google.auth.transport.requests
import logging

load_dotenv()

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(error):
    return "invalid request", 404

def format_profiles(profiles):
    formatted_profiles = []

    # Define field mappings
    field_mappings = {
        "uniqueId": "uniqueId",
        "firstName": "firstName",
        "middleName": "middleName",
        "lastName": "lastName",
        "orderNumber": "orderNumber",
        "emailUsed": "emailUsed",
        "birthDate": "birthDate",
        "bannerPhoto": "bannerPhoto",
        "usOrCanadianOrInternationalSchool": "usOrCanadianOrInternationalSchool",
        "cannotFindSchoolPleaseProvideIt": "cannotFindSchoolPleaseProvideIt",
        "Degree": "Degree",
        "graduationYear": "graduationYear",
        "usUndergradSchool":"usUndergradSchool",
        "aboutMe": "aboutMe",
        "myAcademics": "myAcademics",
        "myExtracurricularActivities":"myExtracurricularActivities",
        "myAthletics": "myAthletics",
        "myPlansForFuture": "myPlansForFuture",
        "myJobsInternships": "myJobsInternships",
        "mySkills": "mySkills",
        "myLanguages": "myLanguages",
        "myHonorsAwards": "myHonorsAwards",
        "favoriteBook": "favoriteBook",
        "favoriteQuote": "favoriteQuote",
        "favoriteCharitableCauses": "favoriteCharitableCauses",
        "regionsAndCharitableNeedsICareAbout": "regionsAndCharitableNeedsICareAbout",
        "metropolitanAreasWhoseCharitableNeedsICareAbout": "metropolitanAreasWhoseCharitableNeedsICareAbout",
        "ethnicGroupsWhoseCharitableNeedsICareAbout": "ethnicGroupsWhoseCharitableNeedsICareAbout",
        "religiousGroupsWhoseCharitableNeedsICareAbout":"religiousGroupsWhoseCharitableNeedsICareAbout",
        "howMyLifestyleIsMakingtheWorldBetterPlace": "howMyLifestyleIsMakingtheWorldBetterPlace",
        "favoriteNonprofitOrganizations.": "favoriteNonprofitOrganizations.",
        "volunteeringCommunityService": "volunteeringCommunityService",
        "myFundraisingActivities": "myFundraisingActivities",
        "charitableWishlists": "charitableWishlists",
        "myThoughtsOnMakingaDifference": "myThoughtsOnMakingaDifference",
        "placesIHaveLived": "placesIHaveLived",
        "placesIHaveTraveled": "placesIHaveTraveled",
        "myFavoritePodcasts": "myFavoritePodcasts",
    }

    for profile in profiles:
        formatted_profile = {key: profile.get(value, None) for key, value in field_mappings.items()}

        organization = []
        organization_fields = [
            "doYouBelongToGreek",
            "shareYourNationalSocialFraternityMembership",
            "nameYourNationalSocialFraternityIfNotInList",
            "yourNationalSocialSororityMembership",
            "nameYourNationalSocialSororityIfNotInList",
            "yourNationalFraternityAssociations",
            "yourNationalFraternityAssociationIfNotInList",
            "yourNationalOrganizationsMembership",
            "YourOtherNationalOrganizationWhichYouCannotFind",
            "menSportsTeam",
            "womenSportsTeam",
            "yourMenSportsTeamIfNotInList",
            "yourWomenSportsTeamIfNotInList"
        ]

        for field in organization_fields:
            if profile.get(field):
                organizations = profile[field].split("\n")
                for org in organizations:
                    organization.append({
                        "name": org,
                        "iconURL": "Organization icon URL",
                        "accountURL": "Organization account URL"
                    })

        formatted_profile["organisation"] = organization

        local_organization = []
        if profile.get("includeTwelveStudentclubsToWhichYouBelong"):
            student_clubs = profile["includeTwelveStudentclubsToWhichYouBelong"].split("\n")
            for club in student_clubs:
                parts = club.split("Position (if any):")
                if len(parts) == 2:
                    local_organization.append({
                        "name": parts[0].strip(),
                        "role": parts[1].strip()
                    })

        formatted_profile["localOrganisation"] = local_organization

        social_media_icons = []

        social_media_fields = [
            "yourOwnWebsite",
            "yourBlog",
            "LinkedIn",
            "Instagram",
            "Twitter",
            "Facebook",
            "GooglePlus",
            "Pinterest",
            "Youtube",
            "Flickr",
            "Behance",
            "Tumblr",
            "Etsy",
            "WayUp",
            "academiaEdu",
            "Researchgate",
            "Digication",
            "Issuu",
            "VSCO",
            "500px",
            "helperHelper",
            "Github",
            "projectsThatMatterorg",
            "Quora",
            "TikTok",
            "Strava",
            "sportsRecruits",
            "mileSplit",
            "prestoSports",
            "Harri",
            "eliteProspects",
            "Hudl",
            "maxPreps",
            "NCSA",
            "athleticNet",
            "medium",
            "twitch",
            "soundCloud",
            "artStation",
            "firstRobotics",
            "Patreon",
            "soundClick",
            "bandcamp",
            "vexRobotics",
            "Rivals",
            "swimCloud"
        ]

        for field in social_media_fields:
            if profile.get(field):
                social_media_icons.append({
                    "platform": field,
                    "iconUrl": getIconUrl(field),
                    "url": profile[field]
                })

        formatted_profile["socialMediaIcons"] = social_media_icons

        formatted_profiles.append(formatted_profile)

    return formatted_profiles   

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

        with DBConnection() as db_connection:
            cursor = db_connection.cursor(dictionary=True)

            # Check if the profile with the given uniqueId exists
            check_query = "SELECT * FROM Wordpress_profile WHERE uniqueId = %s"
            cursor.execute(check_query, (uniqueId,))
            existing_profile = cursor.fetchone()

            if not existing_profile:
                return "Profile not found", 404

            # Prepare the UPDATE query dynamically
            update_query = "UPDATE Wordpress_profile SET "
            update_values = []

            for key, value in data.items():
                if key != "uniqueId":
                    update_query += f"`{key}` = %s, "  # Use backticks to handle special characters
                    update_values.append(value)

            # Remove the trailing comma and space from the query
            update_query = update_query.rstrip(', ')

            update_query += " WHERE uniqueId = %s"
            update_values.append(uniqueId)

            cursor.execute(update_query, update_values)
            db_connection.commit()

        return "Profile updated successfully", 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/profile', methods=['POST'])
def create_profile():
    try:
        data = request.get_json()

        if not data:
            return jsonify({"error": "Invalid JSON data"}), 400

        with DBConnection() as db_connection:
            cursor = db_connection.cursor(dictionary=True)

            # Insert the new profile data into the database
            insert_query = """
                INSERT INTO Wordpress_profile (
                    uniqueId, firstName, middleName, lastName, orderNumber, emailUsed, birthDate, bannerPhoto, 
                    usOrCanadianOrInternationalSchool, cannotFindSchoolPleaseProvideIt, Degree, graduationYear,
                    usUndergradSchool, aboutMe, myAcademics, myExtracurricularActivities, myAthletics, myPlansForFuture,
                    myJobsInternships, mySkills, myLanguages, myHonorsAwards, favoriteBook, favoriteQuote, 
                    favoriteCharitableCauses, regionsAndCharitableNeedsICareAbout, metropolitanAreasWhoseCharitableNeedsICareAbout,
                    ethnicGroupsWhoseCharitableNeedsICareAbout, religiousGroupsWhoseCharitableNeedsICareAbout,
                    howMyLifestyleIsMakingtheWorldBetterPlace, `favoriteNonprofitOrganizations.`, volunteeringCommunityService,
                    myFundraisingActivities, charitableWishlists, doYouBelongToGreek, shareYourNationalSocialFraternityMembership,
                    nameYourNationalSocialFraternityIfNotInList, yourNationalSocialSororityMembership,
                    nameYourNationalSocialSororityIfNotInList, yourNationalFraternityAssociations,
                    yourNationalFraternityAssociationIfNotInList, yourNationalOrganizationsMembership,
                    YourOtherNationalOrganizationWhichYouCannotFind, menSportsTeam, womenSportsTeam,
                    yourMenSportsTeamIfNotInList, yourWomenSportsTeamIfNotInList, includeTwelveStudentclubsToWhichYouBelong,
                    yourOwnWebsite, yourBlog, LinkedIn, Instagram, Twitter, Facebook, GooglePlus, Pinterest, Youtube, Flickr, Behance,
                    Tumblr, Etsy, WayUp, academiaEdu, Researchgate, Digication, Issuu, VSCO, 500px, helperHelper, Github,
                    projectsThatMatterorg, Quora, TikTok, Strava, sportsRecruits, mileSplit, prestoSports, Harri,
                    eliteProspects, Hudl, maxPreps, NCSA, athleticNet, medium, twitch, soundCloud, artStation, firstRobotics,
                    Patreon, soundClick, bandcamp, vexRobotics, Rivals, myThoughtsOnMakingaDifference, swimCloud, placesIHaveLived,
                    placesIHaveTraveled, myFavoritePodcasts, newUniqueId, id
                ) VALUES (
                    %(uniqueId)s, %(firstName)s, %(middleName)s, %(lastName)s, %(orderNumber)s, %(emailUsed)s, %(birthDate)s,
                    %(bannerPhoto)s, %(usOrCanadianOrInternationalSchool)s, %(cannotFindSchoolPleaseProvideIt)s, %(Degree)s,
                    %(graduationYear)s, %(usUndergradSchool)s, %(aboutMe)s, %(myAcademics)s, %(myExtracurricularActivities)s,
                    %(myAthletics)s, %(myPlansForFuture)s, %(myJobsInternships)s, %(mySkills)s, %(myLanguages)s,
                    %(myHonorsAwards)s, %(favoriteBook)s, %(favoriteQuote)s, %(favoriteCharitableCauses)s,
                    %(regionsAndCharitableNeedsICareAbout)s, %(metropolitanAreasWhoseCharitableNeedsICareAbout)s,
                    %(ethnicGroupsWhoseCharitableNeedsICareAbout)s, %(religiousGroupsWhoseCharitableNeedsICareAbout)s,
                    %(howMyLifestyleIsMakingtheWorldBetterPlace)s, %(favoriteNonprofitOrganizations.)s, %(volunteeringCommunityService)s,
                    %(myFundraisingActivities)s, %(charitableWishlists)s, %(doYouBelongToGreek)s, %(shareYourNationalSocialFraternityMembership)s,
                    %(nameYourNationalSocialFraternityIfNotInList)s, %(yourNationalSocialSororityMembership)s,
                    %(nameYourNationalSocialSororityIfNotInList)s, %(yourNationalFraternityAssociations)s,
                    %(yourNationalFraternityAssociationIfNotInList)s, %(yourNationalOrganizationsMembership)s,
                    %(YourOtherNationalOrganizationWhichYouCannotFind)s, %(menSportsTeam)s, %(womenSportsTeam)s,
                    %(yourMenSportsTeamIfNotInList)s, %(yourWomenSportsTeamIfNotInList)s,
                    %(includeTwelveStudentclubsToWhichYouBelong)s, %(yourOwnWebsite)s, %(yourBlog)s, %(LinkedIn)s, %(Instagram)s,
                    %(Twitter)s, %(Facebook)s, %(GooglePlus)s, %(Pinterest)s, %(Youtube)s, %(Flickr)s, %(Behance)s, %(Tumblr)s,
                    %(Etsy)s, %(WayUp)s, %(academiaEdu)s, %(Researchgate)s, %(Digication)s, %(Issuu)s, %(VSCO)s, %(500px)s, %(helperHelper)s,
                    %(Github)s, %(projectsThatMatterorg)s, %(Quora)s, %(TikTok)s, %(Strava)s, %(sportsRecruits)s, %(mileSplit)s,
                    %(prestoSports)s, %(Harri)s, %(eliteProspects)s, %(Hudl)s, %(maxPreps)s, %(NCSA)s, %(athleticNet)s, %(medium)s,
                    %(twitch)s, %(soundCloud)s, %(artStation)s, %(firstRobotics)s, %(Patreon)s, %(soundClick)s, %(bandcamp)s,
                    %(vexRobotics)s, %(Rivals)s, %(myThoughtsOnMakingaDifference)s, %(swimCloud)s, %(placesIHaveLived)s,
                    %(placesIHaveTraveled)s, %(myFavoritePodcasts)s, %(newUniqueId)s, %(id)s
                )
            """

            cursor.execute(insert_query, data)
            db_connection.commit()

        return "Profile created successfully", 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/profile/<uniqueId>', methods=['DELETE'])
def delete_profile(uniqueId):
    try:
        with DBConnection() as db_connection:
            cursor = db_connection.cursor()
            query = "DELETE FROM Wordpress_profile WHERE uniqueId = %s"
            cursor.execute(query, (uniqueId,))
            db_connection.commit()

        return "Profile deleted successfully", 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Google OAUTH Configuration 
logging.basicConfig(level=logging.DEBUG)  
logger = logging.getLogger(__name__)

app.secret_key = "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"  

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  

GOOGLE_CLIENT_ID = "701134778327-hlh7dm5iuphaq85h13gu3e3hppgodgqo.apps.googleusercontent.com"
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
    app.run(host='0.0.0.0', port=80, debug=True)