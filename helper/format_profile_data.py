from iconMapping import getIconUrl
def format_profiles(profiles):
    formatted_profiles = []
    # Define field mappings
    identification_info_fields = {
        "uniqueId": "uniqueId",
        "firstName": "firstName",
        "middleName": "middleName",
        "lastName": "lastName",
        "usUndergradSchool": "usUndergradSchool",
        "usOrCanadianOrInternationalSchool": "usOrCanadianOrInternationalSchool",
        "cannotFindSchoolPleaseProvideIt": "cannotFindSchoolPleaseProvideIt",
        "degree": "degree",
        "bannerPhoto": "bannerPhoto",
        "headshotPhoto": "headshotPhoto",
    }
    about_me_info_fields = {
        "aboutMe": "aboutMe",
        "myAcademics": "myAcademics",
        "myExtracurriculars": "myExtracurriculars",
        "myAthletics": "myAthletics",
        "myPlan": "myPlan",
        "myJobsInternships": "myJobsInternships",
        "mySkills": "mySkills",
        "myLanguages": "myLanguages",
        "myHonorsAwards": "myHonorsAwards",
        "myFavoriteBooks": "myFavoriteBooks",
        "myFavoriteQuote": "myFavoriteQuote",
    }
    better_world_info_fields = {
        "myThoughtsOnMakingADifference": "myThoughtsOnMakingADifference",
        "myFavoriteCauses": "myFavoriteCauses",
        "regionsAndCountriesICareAbout": "regionsAndCountriesICareAbout",
        "metropolitanAreasICareAbout": "metropolitanAreasICareAbout",
        "ethnicCommunitiesICareAbout": "ethnicCommunitiesICareAbout",
        "religiousCommunitiesICareAbout": "religiousCommunitiesICareAbout",
        "myFavoriteNonprofits": "myFavoriteNonprofits",
        "mySustainableLifeStyle": "mySustainableLifeStyle",
        "myVolunteeringAndCommunityService": "myVolunteeringAndCommunityService",
        "myCharitableFundraising": "myCharitableFundraising",
        "charitableWishlists": "charitableWishlists",
        "wishListUrl": "wishListUrl"
    }
    for profile in profiles:
        formatted_profile = {
            "identificationInfo": {key: profile.get(value, None) for key, value in identification_info_fields.items()},
            "aboutMeInfo": {key: profile.get(value, None) for key, value in about_me_info_fields.items()},
            "betterWorldInfo": {key: profile.get(value, None) for key, value in better_world_info_fields.items()},
        }
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
                    print("org" , org)
                    organization.append({
                        "name": org,
                        "iconURL": getIconUrl(org),
                        "accountURL": "Organization account URL"
                    })
        formatted_profile["organization"] = organization
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
        formatted_profile["localOrganization"] = local_organization
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