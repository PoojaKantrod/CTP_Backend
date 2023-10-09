from iconMapping import getIconUrl

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
