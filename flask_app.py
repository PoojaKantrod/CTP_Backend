from flask import Flask, Response, request, jsonify
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
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from pip._vendor import cachecontrol

load_dotenv()

app = Flask(__name__)

db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_database = os.environ.get("DB_DATABASE")

# Create a connection pool
connection_pool = pooling.MySQLConnectionPool(
    pool_name="mypool",
    pool_size=10,
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_database,
    auth_plugin='mysql_native_password'
)
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
                    "iconUrl": f"{field} icon URL",
                    "url": profile[field]
                })

        formatted_profile["socialMediaIcons"] = social_media_icons

        formatted_profiles.append(formatted_profile)

    return formatted_profiles


 # Define a context manager for getting database connections from the pool
class DBConnection:
    def __enter__(self):
        self.db_connection = connection_pool.get_connection()
        return self.db_connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.db_connection:
            self.db_connection.close()      

@app.route('/api/profiles', methods=['GET'])
@auth_required()
def get_profiles():
    try:
        with DBConnection() as db_connection:
            cursor = db_connection.cursor(dictionary=True)
            query = "SELECT * FROM Wordpress_profile"
            cursor.execute(query)
            profiles = cursor.fetchall()

        formatted_profiles = format_profiles(profiles)
        response_data = json.dumps(formatted_profiles, indent=2)
        return Response(response_data, content_type='application/json')

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/profile/<uniqueId>', methods=['GET'])
@auth_required()
def get_profile(uniqueId):
    try:
        with DBConnection() as db_connection:
            cursor = db_connection.cursor(dictionary=True)
            query = "SELECT * FROM Wordpress_profile WHERE uniqueId = %s"
            cursor.execute(query, (uniqueId,))
            profile = cursor.fetchone()

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
@auth_required()
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
@auth_required()
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


app.secret_key = os.environ.get("secret_key")

@app.route("/callback")
@cognito_login_callback
def callback():
    return redirect("/protected_area")

@app.route("/logout")
@cognito_logout
def logout():
   # session.clear()
    return redirect("/login")

@app.route("/login")
@cognito_login
def index():
    return "Hello World <a href='/login-button'><button>Login</button></a>"

@app.route("/protected_area")
@auth_required()
def protected_area():
    # return f"Hello {session['name']}! <br/> <a href='/logout'><button>Logout</button></a>"
    return f"Hello! <br/> <a href='/logout'><button>Logout</button></a>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)