from flask import Flask, Response
import mysql.connector
import json

app = Flask(__name__)

def format_profiles(profiles):
    formatted_profiles = []

    for profile in profiles:
        formatted_profile = {
            "uniqueId": profile["uniqueId"],
            "firstName": profile["firstName"],
            "middleName": profile["middleName"],
            "lastName": profile["lastName"],
            "orderNumber": profile["orderNumber"],
            "emailUsed": profile["emailUsed"],
            "birthDate": profile["birthDate"],
            "bannerPhoto": profile["bannerPhoto"],
            "usOrCanadianOrInternationalSchool": profile["usOrCanadianOrInternationalSchool"],
            "cannotFindSchoolPleaseProvideIt": profile["cannotFindSchoolPleaseProvideIt"],
            "Degree": profile["Degree"],
            "graduationYear": profile["graduationYear"],
            "usUndergradSchool": profile["usUndergradSchool"],
            "aboutMe": profile["aboutMe"],
            "myAcademics": profile["myAcademics"],
            "myExtracurricularActivities": profile["myExtracurricularActivities"],
            "myAthletics": profile["myAthletics"],
            "myPlansForFuture": profile["myPlansForFuture"],
            "myJobsInternships": profile["myJobsInternships"],
            "mySkills": profile["mySkills"],
            "myLanguages": profile["myLanguages"],
            "myHonorsAwards": profile["myHonorsAwards"],
            "favoriteBook": profile["favoriteBook"],
            "favoriteQuote": profile["favoriteQuote"],
            "favoriteCharitableCauses": profile["favoriteCharitableCauses"],
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
            "placesIHaveLived": profile["placesIHaveLived"],
            "placesIHaveTraveled": profile["placesIHaveTraveled"],
            "myFavoritePodcasts": profile["myFavoritePodcasts"],
            
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
                "iconUrl": "yourOwnWebsite icon URL",
                "url": profile["yourOwnWebsite"]
            })
        
        if profile["yourBlog"]:
            social_media_icons.append({
                "platform": "yourBlog",
                "iconUrl": "yourBlog icon URL",
                "url": profile["yourBlog"]
            })
            
        if profile["LinkedIn"]:
            social_media_icons.append({
                "platform": "LinkedIn",
                "iconUrl": "LinkedIn icon URL",
                "url": profile["LinkedIn"]
            })
            
        if profile["Instagram"]:
            social_media_icons.append({
                "platform": "Instagram",
                "iconUrl": "Instagram icon URL",
                "url": profile["Instagram"]
            })
            
            
        if profile["Twitter"]:
            social_media_icons.append({
                "platform": "Twitter",
                "iconUrl": "Twitter icon URL",
                "url": profile["Twitter"]
            })
            
        if profile["Facebook"]:
            social_media_icons.append({
                "platform": "Facebook",
                "iconUrl": "Facebook icon URL",
                "url": profile["Facebook"]
            })
            
            
        if profile["GooglePlus"]:
            social_media_icons.append({
                "platform": "GooglePlus",
                "iconUrl": "GooglePlus icon URL",
                "url": profile["GooglePlus"]
            })
            
        if profile["Pinterest"]:
            social_media_icons.append({
                "platform": "Pinterest",
                "iconUrl": "Pinterest icon URL",
                "url": profile["Pinterest"]
            })
            
        if profile["Youtube"]:
            social_media_icons.append({
                "platform": "Youtube",
                "iconUrl": "Youtube icon URL",
                "url": profile["Youtube"]
            })
            
        if profile["Flickr"]:
            social_media_icons.append({
                "platform": "Flickr",
                "iconUrl": "Flickr icon URL",
                "url": profile["Flickr"]
            })
            
        if profile["Behance"]:
            social_media_icons.append({
                "platform": "Behance",
                "iconUrl": "Behance icon URL",
                "url": profile["Behance"]
            })
            
        if profile["Tumblr"]:
            social_media_icons.append({
                "platform": "Tumblr",
                "iconUrl": "Tumblr icon URL",
                "url": profile["Tumblr"]
            })
            
        if profile["Etsy"]:
            social_media_icons.append({
                "platform": "Etsy",
                "iconUrl": "Etsy icon URL",
                "url": profile["Etsy"]
            })
            
        if profile["WayUp"]:
            social_media_icons.append({
                "platform": "WayUp",
                "iconUrl": "WayUp icon URL",
                "url": profile["WayUp"]
            })
            
        if profile["academiaEdu"]:
            social_media_icons.append({
                "platform": "academiaEdu",
                "iconUrl": "academiaEdu icon URL",
                "url": profile["academiaEdu"]
            })
            
        if profile["Researchgate"]:
            social_media_icons.append({
                "platform": "Researchgate",
                "iconUrl": "Researchgate icon URL",
                "url": profile["Researchgate"]
            })
            
        if profile["Digication"]:
            social_media_icons.append({
                "platform": "Digication",
                "iconUrl": "Digication icon URL",
                "url": profile["Digication"]
            })
            
        if profile["Issuu"]:
            social_media_icons.append({
                "platform": "Issuu",
                "iconUrl": "Issuu icon URL",
                "url": profile["Issuu"]
            })
            
        if profile["VSCO"]:
            social_media_icons.append({
                "platform": "VSCO",
                "iconUrl": "VSCO icon URL",
                "url": profile["VSCO"]
            })
            
        if profile["500px"]:
            social_media_icons.append({
                "platform": "500px",
                "iconUrl": "500px icon URL",
                "url": profile["500px"]
            })
            
        if profile["helperHelper"]:
            social_media_icons.append({
                "platform": "helperHelper",
                "iconUrl": "helperHelper icon URL",
                "url": profile["helperHelper"]
            })
            
        if profile["Github"]:
            social_media_icons.append({
                "platform": "Github",
                "iconUrl": "Github icon URL",
                "url": profile["Github"]
            })
            
        if profile["projectsThatMatterorg"]:
            social_media_icons.append({
                "platform": "projectsThatMatterorg",
                "iconUrl": "projectsThatMatterorg icon URL",
                "url": profile["projectsThatMatterorg"]
            })
            
        if profile["Quora"]:
            social_media_icons.append({
                "platform": "Quora",
                "iconUrl": "Quora icon URL",
                "url": profile["Quora"]
            })
            
        if profile["TikTok"]:
            social_media_icons.append({
                "platform": "TikTok",
                "iconUrl": "TikTok icon URL",
                "url": profile["TikTok"]
            })
            
        if profile["Strava"]:
            social_media_icons.append({
                "platform": "Strava",
                "iconUrl": "Strava icon URL",
                "url": profile["Strava"]
            })
            
        if profile["sportsRecruits"]:
            social_media_icons.append({
                "platform": "sportsRecruits",
                "iconUrl": "sportsRecruits icon URL",
                "url": profile["sportsRecruits"]
            })
            
        if profile["mileSplit"]:
            social_media_icons.append({
                "platform": "mileSplit",
                "iconUrl": "mileSplit icon URL",
                "url": profile["mileSplit"]
            })
            
        if profile["prestoSports"]:
            social_media_icons.append({
                "platform": "prestoSports",
                "iconUrl": "prestoSports icon URL",
                "url": profile["prestoSports"]
            })
            
        if profile["Harri"]:
            social_media_icons.append({
                "platform": "Harri",
                "iconUrl": "Harri icon URL",
                "url": profile["Harri"]
            })
            
        if profile["eliteProspects"]:
            social_media_icons.append({
                "platform": "eliteProspects",
                "iconUrl": "eliteProspects icon URL",
                "url": profile["eliteProspects"]
            })
        
        if profile["Hudl"]:
            social_media_icons.append({
                "platform": "Hudl",
                "iconUrl": "Hudl icon URL",
                "url": profile["Hudl"]
            })
            
        if profile["maxPreps"]:
            social_media_icons.append({
                "platform": "maxPreps",
                "iconUrl": "maxPreps icon URL",
                "url": profile["maxPreps"]
            })
            
        if profile["NCSA"]:
            social_media_icons.append({
                "platform": "NCSA",
                "iconUrl": "NCSA icon URL",
                "url": profile["NCSA"]
            })
            
        if profile["athleticNet"]:
            social_media_icons.append({
                "platform": "athleticNet",
                "iconUrl": "athleticNet icon URL",
                "url": profile["athleticNet"]
            })
            
            
        if profile["medium"]:
            social_media_icons.append({
                "platform": "medium",
                "iconUrl": "medium icon URL",
                "url": profile["medium"]
            })
            
        if profile["twitch"]:
            social_media_icons.append({
                "platform": "twitch",
                "iconUrl": "twitch icon URL",
                "url": profile["twitch"]
            })
            
        if profile["soundCloud"]:
            social_media_icons.append({
                "platform": "soundCloud",
                "iconUrl": "soundCloud icon URL",
                "url": profile["soundCloud"]
            })
            
        if profile["artStation"]:
            social_media_icons.append({
                "platform": "artStation",
                "iconUrl": "artStation icon URL",
                "url": profile["artStation"]
            })
            
        if profile["firstRobotics"]:
            social_media_icons.append({
                "platform": "firstRobotics",
                "iconUrl": "firstRobotics icon URL",
                "url": profile["firstRobotics"]
            })
            
        if profile["Patreon"]:
            social_media_icons.append({
                "platform": "Patreon",
                "iconUrl": "Patreon icon URL",
                "url": profile["Patreon"]
            })
            
            
        if profile["soundClick"]:
            social_media_icons.append({
                "platform": "soundClick",
                "iconUrl": "soundClick icon URL",
                "url": profile["soundClick"]
            })
            
        if profile["bandcamp"]:
            social_media_icons.append({
                "platform": "bandcamp",
                "iconUrl": "bandcamp icon URL",
                "url": profile["bandcamp"]
            })
            
        if profile["vexRobotics"]:
            social_media_icons.append({
                "platform": "vexRobotics",
                "iconUrl": "vexRobotics icon URL",
                "url": profile["vexRobotics"]
            })
            
            
        if profile["Rivals"]:
            social_media_icons.append({
                "platform": "Rivals",
                "iconUrl": "Rivals icon URL",
                "url": profile["Rivals"]
            })
            
            
        if profile["swimCloud"]:
            social_media_icons.append({
                "platform": "swimCloud",
                "iconUrl": "swimCloud icon URL",
                "url": profile["swimCloud"]
            })

        formatted_profile["socialMediaIcons"] = social_media_icons

    return formatted_profiles

       

@app.route('/api/profiles', methods=['GET'])
def get_profiles():
    db_host = '127.0.0.1'
    db_port = 3306
    db_user = 'root'
    db_password = 'Scorpio@2024'
    db_database = 'mock_data'

    db_connection = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_database,
        auth_plugin='mysql_native_password'
    )

    cursor = db_connection.cursor(dictionary=True)
    query = "SELECT * FROM Wordpress_profile"
    cursor.execute(query)
    profiles = cursor.fetchall()
    cursor.close()
    db_connection.close()
    
    
    formatted_profiles = format_profiles(profiles)
    response_data = json.dumps(formatted_profiles, indent=2)
    response = Response(response_data, content_type='application/json')
    return response


@app.route('/api/profile/<uniqueId>', methods=['GET'])
def get_profile(uniqueId):
    db_host = '127.0.0.1'
    db_port = 3306
    db_user = 'root'
    db_password = 'Scorpio@2024'
    db_database = 'mock_data'

    db_connection = mysql.connector.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_database,
        auth_plugin='mysql_native_password'
    )

    cursor = db_connection.cursor(dictionary=True)
    query = "SELECT * FROM Wordpress_profile WHERE uniqueId = %s"
    cursor.execute(query, (uniqueId,))
    profile = cursor.fetchone()
    cursor.close()
    db_connection.close()
    
    if profile:
        formatted_profile = format_profiles([profile])[0]
        response_data = json.dumps(formatted_profile, indent=2)
        response = Response(response_data, content_type='application/json')
        return response
    else:
        return "Profile not found", 404



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
