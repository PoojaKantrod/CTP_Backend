from flask import Flask, Response
import mysql.connector
import json

import os

from iconMapping import getIconUrl
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

db_host = os.environ.get("DB_HOST")
db_port = os.environ.get("DB_PORT")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PASSWORD")
db_database = os.environ.get("DB_DATABASE")

db_connection = mysql.connector.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_database,
    auth_plugin='mysql_native_password'
)

@app.errorhandler(404)
def page_not_found(error):
    return "invalid request", 404

def format_profiles(profiles):
    formatted_profiles = []

    for profile in profiles:
        formatted_profile = {
            "uniqueId": profile["uniqueId"],
            "firstName": profile["firstName"],
            "middleName": profile["middleName"],
            "lastName": profile["lastName"],
            "bannerPhoto": profile["bannerPhoto"],
            "usOrCanadianOrInternationalSchool": profile["usOrCanadianOrInternationalSchool"],
            "cannotFindSchoolPleaseProvideIt": profile["cannotFindSchoolPleaseProvideIt"],
            "Degree": profile["Degree"],
            "aboutMe": profile["aboutMe"],
            "myAcademics": profile["myAcademics"],
            "myExtracurricularActivities": profile["myExtracurricularActivities"],
            "myAthletics": profile["myAthletics"],
            "myPlansForFuture": profile["myPlansForFuture"],
            "myJobsInternships": profile["myJobsInternships"],
            "myHonorsAwards": profile["myHonorsAwards"],
            "mySkills": profile["mySkills"],
            "myLanguages": profile["myLanguages"],
            "favoriteBook": profile["favoriteBook"],
            "favoriteQuote": profile["favoriteQuote"],
            "myFavoritePodcasts": profile["myFavoritePodcasts"],
            "placesIHaveLived": profile["placesIHaveLived"],
            "placesIHaveTraveled": profile["placesIHaveTraveled"],
            "regionsAndCharitableNeedsICareAbout": profile["regionsAndCharitableNeedsICareAbout"],
            "metropolitanAreasWhoseCharitableNeedsICareAbout": profile["metropolitanAreasWhoseCharitableNeedsICareAbout"],
            "ethnicGroupsWhoseCharitableNeedsICareAbout": profile["ethnicGroupsWhoseCharitableNeedsICareAbout"],
            "religiousGroupsWhoseCharitableNeedsICareAbout": profile["religiousGroupsWhoseCharitableNeedsICareAbout"],
            "howMyLifestyleIsMakingtheWorldBetterPlace": profile["howMyLifestyleIsMakingtheWorldBetterPlace"],
            "favoriteNonprofitOrganizations.": profile["favoriteNonprofitOrganizations."],
            "volunteeringCommunityService": profile["volunteeringCommunityService"],
            "myFundraisingActivities": profile["myFundraisingActivities"],
            "charitableWishlists": profile["charitableWishlists"],
            "myThoughtsOnMakingaDifference": profile["myThoughtsOnMakingaDifference"],
            "favoriteCharitableCauses": profile["favoriteCharitableCauses"],
        }
        
        
        organization = []
        if profile["doYouBelongToGreek"]:
            organizations = profile["doYouBelongToGreek"].split("\n")
            for org in organizations:
                organization.append({
                    "name": org,
                    "iconURL": "Organization icon URL",
                    "accountURL": "Organization account URL"
                })
        if profile["shareYourNationalSocialFraternityMembership"]:
            organizations = profile["shareYourNationalSocialFraternityMembership"].split("\n")
            for org in organizations:
                organization.append({
                    "name": org,
                    "iconURL": "Organization icon URL",
                    "accountURL": "Organization account URL"
                })
                
        if profile["nameYourNationalSocialFraternityIfNotInList"]:
            organizations = profile["nameYourNationalSocialFraternityIfNotInList"].split("\n")
            for org in organizations:
                organization.append({
                    "name": org,
                    "iconURL": "Organization icon URL",
                    "accountURL": "Organization account URL"
                })
                
        if profile["yourNationalSocialSororityMembership"]:
            organizations = profile["yourNationalSocialSororityMembership"].split("\n")
            for org in organizations:
                organization.append({
                    "name": org,
                    "iconURL": "Organization icon URL",
                    "accountURL": "Organization account URL"
                })
                
        if profile["nameYourNationalSocialSororityIfNotInList"]:
            organizations = profile["nameYourNationalSocialSororityIfNotInList"].split("\n")
            for org in organizations:
                organization.append({
                    "name": org,
                    "iconURL": "Organization icon URL",
                    "accountURL": "Organization account URL"
                })
                
        if profile["yourNationalFraternityAssociations"]:
            organizations = profile["yourNationalFraternityAssociations"].split("\n")
            for org in organizations:
                organization.append({
                    "name": org,
                    "iconURL": "Organization icon URL",
                    "accountURL": "Organization account URL"
                })
                
        if profile["yourNationalFraternityAssociationIfNotInList"]:
            organizations = profile["yourNationalFraternityAssociationIfNotInList"].split("\n")
            for org in organizations:
                organization.append({
                    "name": org,
                    "iconURL": "Organization icon URL",
                    "accountURL": "Organization account URL"
                })
                
        if profile["yourNationalOrganizationsMembership"]:
            organizations = profile["yourNationalOrganizationsMembership"].split("\n")
            for org in organizations:
                organization.append({
                    "name": org,
                    "iconURL": "Organization icon URL",
                    "accountURL": "Organization account URL"
                })
                
        if profile["YourOtherNationalOrganizationWhichYouCannotFind"]:
            organizations = profile["YourOtherNationalOrganizationWhichYouCannotFind"].split("\n")
            for org in organizations:
                organization.append({
                    "name": org,
                    "iconURL": "Organization icon URL",
                    "accountURL": "Organization account URL"
                })
                
                
        if profile["menSportsTeam"]:
            organizations = profile["menSportsTeam"].split("\n")
            for org in organizations:
                organization.append({
                    "name": org,
                    "iconURL": "Organization icon URL",
                    "accountURL": "Organization account URL"
                })
                
                
        if profile["womenSportsTeam"]:
            organizations = profile["womenSportsTeam"].split("\n")
            for org in organizations:
                organization.append({
                    "name": org,
                    "iconURL": "Organization icon URL",
                    "accountURL": "Organization account URL"
                })
                
        if profile["yourMenSportsTeamIfNotInList"]:
            organizations = profile["yourMenSportsTeamIfNotInList"].split("\n")
            for org in organizations:
                organization.append({
                    "name": org,
                    "iconURL": "Organization icon URL",
                    "accountURL": "Organization account URL"
                })
                
        if profile["yourWomenSportsTeamIfNotInList"]:
            organizations = profile["yourWomenSportsTeamIfNotInList"].split("\n")
            for org in organizations:
                organization.append({
                    "name": org,
                    "iconURL": "Organization icon URL",
                    "accountURL": "Organization account URL"
                })
                
                
        formatted_profile["organisation"] = organization

        
        local_organization = []
        if profile["includeTwelveStudentclubsToWhichYouBelong"]:
            student_clubs = profile["includeTwelveStudentclubsToWhichYouBelong"].split("\n")
            for club in student_clubs:
                parts = club.split("Position (if any):")
                if len(parts) == 2:
                    local_organization.append({
                        "name": parts[0].strip(),
                        "role": parts[1].strip()
                    })

        formatted_profile["localOrganisation"] = local_organization

        formatted_profiles.append(formatted_profile)
        
        
        social_media_icons = []
        if profile["yourOwnWebsite"]:
            social_media_icons.append({
                "platform": "yourOwnWebsite",
                "iconUrl": getIconUrl("yourOwnWebsite"),
                "url": profile["yourOwnWebsite"]
            })
        
        if profile["yourBlog"]:
            social_media_icons.append({
                "platform": "yourBlog",
                "iconUrl": getIconUrl("yourBlog"),
                "url": profile["yourBlog"]
            })
            
        if profile["LinkedIn"]:
            social_media_icons.append({
                "platform": "LinkedIn",
                "iconUrl": getIconUrl("LinkedIn"),
                "url": profile["LinkedIn"]
            })
            
        if profile["Instagram"]:
            social_media_icons.append({
                "platform": "Instagram",
                "iconUrl": getIconUrl("Instagram"),
                "url": profile["Instagram"]
            })
            
            
        if profile["Twitter"]:
            social_media_icons.append({
                "platform": "Twitter",
                "iconUrl": getIconUrl("Twitter"),
                "url": profile["Twitter"]
            })
            
        if profile["Facebook"]:
            social_media_icons.append({
                "platform": "Facebook",
                "iconUrl": getIconUrl("Facebook"),
                "url": profile["Facebook"]
            })
            
            
        if profile["GooglePlus"]:
            social_media_icons.append({
                "platform": "GooglePlus",
                "iconUrl": getIconUrl("GooglePlus"),
                "url": profile["GooglePlus"]
            })
            
        if profile["Pinterest"]:
            social_media_icons.append({
                "platform": "Pinterest",
                "iconUrl": getIconUrl("Pinterest"),
                "url": profile["Pinterest"]
            })
            
        if profile["Youtube"]:
            social_media_icons.append({
                "platform": "Youtube",
                "iconUrl": getIconUrl("Youtube"),
                "url": profile["Youtube"]
            })
            
        if profile["Flickr"]:
            social_media_icons.append({
                "platform": "Flickr",
                "iconUrl": getIconUrl("Flickr"),
                "url": profile["Flickr"]
            })
            
        if profile["Behance"]:
            social_media_icons.append({
                "platform": "Behance",
                "iconUrl": getIconUrl("Behance"),
                "url": profile["Behance"]
            })
            
        if profile["Tumblr"]:
            social_media_icons.append({
                "platform": "Tumblr",
                "iconUrl": getIconUrl("Tumblr"),
                "url": profile["Tumblr"]
            })
            
        if profile["Etsy"]:
            social_media_icons.append({
                "platform": "Etsy",
                "iconUrl": getIconUrl("Etsy"),
                "url": profile["Etsy"]
            })
            
        if profile["WayUp"]:
            social_media_icons.append({
                "platform": "WayUp",
                "iconUrl": getIconUrl("WayUp"),
                "url": profile["WayUp"]
            })
            
        if profile["academiaEdu"]:
            social_media_icons.append({
                "platform": "academiaEdu",
                "iconUrl": getIconUrl("academiaEdu"),
                "url": profile["academiaEdu"]
            })
            
        if profile["Researchgate"]:
            social_media_icons.append({
                "platform": "Researchgate",
                "iconUrl": getIconUrl("Researchgate"),
                "url": profile["Researchgate"]
            })
            
        if profile["Digication"]:
            social_media_icons.append({
                "platform": "Digication",
                "iconUrl": getIconUrl("Digication"),
                "url": profile["Digication"]
            })
            
        if profile["Issuu"]:
            social_media_icons.append({
                "platform": "Issuu",
                "iconUrl": getIconUrl("Issuu"),
                "url": profile["Issuu"]
            })
            
        if profile["VSCO"]:
            social_media_icons.append({
                "platform": "VSCO",
                "iconUrl": getIconUrl("VSCO"),
                "url": profile["VSCO"]
            })
            
        if profile["500px"]:
            social_media_icons.append({
                "platform": "500px",
                "iconUrl": getIconUrl("500px"),
                "url": profile["500px"]
            })
            
        if profile["helperHelper"]:
            social_media_icons.append({
                "platform": "helperHelper",
                "iconUrl": getIconUrl("helperHelper"),
                "url": profile["helperHelper"]
            })
            
        if profile["Github"]:
            social_media_icons.append({
                "platform": "Github",
                "iconUrl": getIconUrl("Github"),
                "url": profile["Github"]
            })
            
        if profile["projectsThatMatterorg"]:
            social_media_icons.append({
                "platform": "projectsThatMatterorg",
                "iconUrl": getIconUrl("projectsThatMatterorg"),
                "url": profile["projectsThatMatterorg"]
            })
            
        if profile["Quora"]:
            social_media_icons.append({
                "platform": "Quora",
                "iconUrl": getIconUrl("Quora"),
                "url": profile["Quora"]
            })
            
        if profile["TikTok"]:
            social_media_icons.append({
                "platform": "TikTok",
                "iconUrl": getIconUrl("TikTok"),
                "url": profile["TikTok"]
            })
            
        if profile["Strava"]:
            social_media_icons.append({
                "platform": "Strava",
                "iconUrl": getIconUrl("Strava"),
                "url": profile["Strava"]
            })
            
        if profile["sportsRecruits"]:
            social_media_icons.append({
                "platform": "sportsRecruits",
                "iconUrl": getIconUrl("sportsRecruits"),
                "url": profile["sportsRecruits"]
            })
            
        if profile["mileSplit"]:
            social_media_icons.append({
                "platform": "mileSplit",
                "iconUrl": getIconUrl("mileSplit"),
                "url": profile["mileSplit"]
            })
            
        if profile["prestoSports"]:
            social_media_icons.append({
                "platform": "prestoSports",
                "iconUrl": getIconUrl("prestoSports"),
                "url": profile["prestoSports"]
            })
            
        if profile["Harri"]:
            social_media_icons.append({
                "platform": "Harri",
                "iconUrl": getIconUrl("Harri"),
                "url": profile["Harri"]
            })
            
        if profile["eliteProspects"]:
            social_media_icons.append({
                "platform": "eliteProspects",
                "iconUrl": getIconUrl("eliteProspects"),
                "url": profile["eliteProspects"]
            })
        
        if profile["Hudl"]:
            social_media_icons.append({
                "platform": "Hudl",
                "iconUrl": getIconUrl("Hudl"),
                "url": profile["Hudl"]
            })
            
        if profile["maxPreps"]:
            social_media_icons.append({
                "platform": "maxPreps",
                "iconUrl": getIconUrl("maxPreps"),
                "url": profile["maxPreps"]
            })
            
        if profile["NCSA"]:
            social_media_icons.append({
                "platform": "NCSA",
                "iconUrl": getIconUrl("NCSA"),
                "url": profile["NCSA"]
            })
            
        if profile["athleticNet"]:
            social_media_icons.append({
                "platform": "athleticNet",
                "iconUrl": getIconUrl("athleticNet"),
                "url": profile["athleticNet"]
            })
            
            
        if profile["medium"]:
            social_media_icons.append({
                "platform": "medium",
                "iconUrl": getIconUrl("medium"),
                "url": profile["medium"]
            })
            
        if profile["twitch"]:
            social_media_icons.append({
                "platform": "twitch",
                "iconUrl": getIconUrl("twitch"),
                "url": profile["twitch"]
            })
            
        if profile["soundCloud"]:
            social_media_icons.append({
                "platform": "soundCloud",
                "iconUrl": getIconUrl("soundCloud"),
                "url": profile["soundCloud"]
            })
            
        if profile["artStation"]:
            social_media_icons.append({
                "platform": "artStation",
                "iconUrl": getIconUrl("artStation"),
                "url": profile["artStation"]
            })
            
        if profile["firstRobotics"]:
            social_media_icons.append({
                "platform": "firstRobotics",
                "iconUrl": getIconUrl("firstRobotics"),
                "url": profile["firstRobotics"]
            })
            
        if profile["Patreon"]:
            social_media_icons.append({
                "platform": "Patreon",
                "iconUrl": getIconUrl("Patreon"),
                "url": profile["Patreon"]
            })
            
            
        if profile["soundClick"]:
            social_media_icons.append({
                "platform": "soundClick",
                "iconUrl": getIconUrl("soundClick"),
                "url": profile["soundClick"]
            })
            
        if profile["bandcamp"]:
            social_media_icons.append({
                "platform": "bandcamp",
                "iconUrl": getIconUrl("bandcamp"),
                "url": profile["bandcamp"]
            })
            
        if profile["vexRobotics"]:
            social_media_icons.append({
                "platform": "vexRobotics",
                "iconUrl": getIconUrl("vexRobotics"),
                "url": profile["vexRobotics"]
            })
            
            
        if profile["Rivals"]:
            social_media_icons.append({
                "platform": "Rivals",
                "iconUrl": getIconUrl("Rivals"),
                "url": profile["Rivals"]
            })
            
            
        if profile["swimCloud"]:
            social_media_icons.append({
                "platform": "swimCloud",
                "iconUrl": getIconUrl("swimCloud"),
                "url": profile["swimCloud"]
            })

        formatted_profile["socialMediaIcons"] = social_media_icons

    return formatted_profiles

       

@app.route('/api/profiles', methods=['GET'])
def get_profiles():
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = "SELECT * FROM Wordpress_profile"
        cursor.execute(query)
        profiles = cursor.fetchall()
    except Exception as e:
        response = Response({"error":e}, content_type='application/json')
    finally:
        cursor.close()
        
    formatted_profiles = format_profiles(profiles)
    response_data = json.dumps(formatted_profiles, indent=2)
    response = Response(response_data, content_type='application/json')
    
    return response


@app.route('/api/profile/<uniqueId>', methods=['GET'])
def get_profile(uniqueId):
    cursor = db_connection.cursor(dictionary=True)
    try:
        query = "SELECT * FROM Wordpress_profile WHERE uniqueId = %s"
        cursor.execute(query, (uniqueId,))
        profile = cursor.fetchone()
    except Exception as e:
        return "Error occured", 501
    finally:
        cursor.close()
        
    if profile:
        formatted_profile = format_profiles([profile])[0]
        response_data = json.dumps(formatted_profile, indent=2)
        response = Response(response_data, content_type='application/json')
        return response
    else:
        return "Profile not found", 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
