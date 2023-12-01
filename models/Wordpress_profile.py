from database import DBConnection
class Wordpress_profile:
    def __init__(self):
        return
    def get_all_profiles(self):
        """
        Get a Wordpress profiles
        """
        with DBConnection() as db_connection:
            cursor = db_connection.cursor(dictionary=True)
            query = "SELECT * FROM cleaned_data"
            cursor.execute(query)
            profiles = cursor.fetchall()
            if not profiles:
                return
            return profiles
    def get_by_id(self, uniqueId):
        """
        Get a Wordpress profile by unique id
        """
        with DBConnection() as db_connection:
            cursor = db_connection.cursor(dictionary=True)
            query = "SELECT * FROM cleaned_data WHERE uniqueId = %s"
            cursor.execute(query, (uniqueId,))
            profile = cursor.fetchone()
            if not profile:
                return
            return profile
    def delete_by_id(self, uniqueId):
        """
        Delete a Wordpress profile by unique id
        """
        with DBConnection() as db_connection:
            cursor = db_connection.cursor()
            query = "DELETE FROM cleaned_data WHERE uniqueId = %s"
            result = cursor.execute(query, (uniqueId,))
            db_connection.commit()
            if result.rowcount > 0:
                return {"message": "Profile deleted successfully", "status_code":200}
            else:
                return {"message":f"Failed to delete profile with {uniqueId}", "status_code":200}
    def update_profile_by_id(self, uniqueId, data):
        """
        Update profile by the data. UniqueId is the ID used to identify row.
        """
        with DBConnection() as db_connection:
            cursor = db_connection.cursor(dictionary=True)
            # Check if the profile with the given uniqueId exists
            check_query = "SELECT * FROM cleaned_data WHERE uniqueId = %s"
            cursor.execute(check_query, (uniqueId,))
            existing_profile = cursor.fetchone()
            if not existing_profile:
                return {"message":"Profile not found", "status_code":404}
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
            return {"message":"Profile updated successfully", "status_code": 200}
    def create_profile(self, data):
        with DBConnection() as db_connection:
            cursor = db_connection.cursor(dictionary=True)
            # Insert the new profile data into the database
            insert_query = """
                INSERT INTO cleaned_data (
                    uniqueId, firstName, middleName, lastName, bannerPhoto, headshotPhoto
                    usOrCanadianOrInternationalSchool, cannotFindSchoolPleaseProvideIt, degree, ,
                    usUndergradSchool, aboutMe, myAcademics, myExtracurriculars, myAthletics, myPlans,
                    myJobsInternships, mySkills, myLanguages, myHonorsAwards, myFavoriteBooks, myFavoriteQuote,
                    myFavoriteCauses, regionsAndCountriesICareAbout, metropolitanAreasICareAbout,
                    ethnicCommunitiesICareAbout, religiousCommunitiesICareAbout,
                    mySustainableLifeStyle, myFavoriteNonprofits, myVolunteeringAndCommunityService,
                    myCharitableFundraising, charitableWishlists, wishListUrl, doYouBelongToGreek, shareYourNationalSocialFraternityMembership,
                    nameYourNationalSocialFraternityIfNotInList, yourNationalSocialSororityMembership,
                    nameYourNationalSocialSororityIfNotInList, yourNationalFraternityAssociations,
                    yourNationalFraternityAssociationIfNotInList, yourNationalOrganizationsMembership,
                    YourOtherNationalOrganizationWhichYouCannotFind, menSportsTeam, womenSportsTeam,
                    yourMenSportsTeamIfNotInList, yourWomenSportsTeamIfNotInList, includeTwelveStudentclubsToWhichYouBelong,
                    yourOwnWebsite, yourBlog, LinkedIn, Instagram, Twitter, Facebook, GooglePlus, Pinterest, Youtube, Flickr, Behance,
                    Tumblr, Etsy, WayUp, academiaEdu, Researchgate, Digication, Issuu, VSCO, 500px, helperHelper, Github,
                    projectsThatMatterorg, Quora, TikTok, Strava, sportsRecruits, mileSplit, prestoSports, Harri,
                    eliteProspects, Hudl, maxPreps, NCSA, athleticNet, medium, twitch, soundCloud, artStation, firstRobotics,
                    Patreon, soundClick, bandcamp, vexRobotics, Rivals, myThoughtsOnMakingADifference, swimCloud
                ) VALUES (
                    %(uniqueId)s, %(firstName)s, %(middleName)s, %(lastName)s, %(headshotPhoto)s
                    %(bannerPhoto)s, %(usOrCanadianOrInternationalSchool)s, %(cannotFindSchoolPleaseProvideIt)s, %(degree)s, %(usUndergradSchool)s, %(aboutMe)s, %(myAcademics)s, %(myExtracurricularActivities)s,
                    %(myAthletics)s, %(myPlans)s, %(myJobsInternships)s, %(mySkills)s, %(myLanguages)s,
                    %(myHonorsAwards)s, %(myFavoriteBooks)s, %(myFavoriteQuote)s, %(myFavoriteCauses)s,
                    %(regionsAndCountriesICareAbout)s, %(metropolitanAreasICareAbout)s,
                    %(ethnicCommunitiesICareAbout)s, %(religiousCommunitiesICareAbout)s,
                    %(mySustainableLifeStyle)s, %(myFavoriteNonprofits)s, %(myVolunteeringAndCommunityService)s,
                    %(myCharitableFundraising)s, %(charitableWishlists)s,%(wishListUrl)s, %(doYouBelongToGreek)s, %(shareYourNationalSocialFraternityMembership)s,
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
                    %(vexRobotics)s, %(Rivals)s, %(myThoughtsOnMakingADifference)s, %(swimCloud)s,
                )
            """
            cursor.execute(insert_query, data)
            db_connection.commit()
        return {"message":"Profile created successfully", "status_code": 201}