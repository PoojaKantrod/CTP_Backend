import pandas as pd

data = {
    "identificationInfo":[
        "uniqueId",
        "firstName",
        "middleName",
        "lastName",
        "usUndergradSchool",
        "usOrCanadianOrInternationalSchool",
        "cannotFindSchoolPleaseProvideIt",
        "degree",
        "schoolWebsite",
        "bannerPhoto",
        "headshotPhoto",
    ],
    "aboutMeInfo":[
        "aboutMe",
        "myPlan",
        "myAcademics",
        "myExtracurriculars",
        "myAthletics",
        "myJobsInternships",
        "myHonorsAwards",
        "mySkills",
        "myLanguages",
        "myFavoriteBooks",
        "myFavoriteQuote",
    ],
    "betterWorldInfo":[
        "myThoughtsOnMakingADifference",
        "myFavoriteCauses",
        "regionsAndCountriesICareAbout",
        "metropolitanAreasICareAbout",
        "ethnicCommunitiesICareAbout",
        "religiousCommunitiesICareAbout",
        "myFavoriteNonprofits",
        "mySustainableLifeStyle",
        "myVolunteeringAndCommunityService",
        "myCharitableFundrasing",
        "charitableWisLists",
        "wishListUrl",
    ],
}

replaceName = {
    "identificationInfo":{
        "Degree":"degree",
        "Crop_it_to_square":"headshotPhoto",
    },
    "aboutMeInfo":{
        "myPlansForFuture":"myPlan",
        "myExtracurricularActivities":"myExtracurriculars",
        "favoriteBook":"myFavoriteBooks",
        "favoriteQuote":"myFavoriteQuote"
    },
    "betterWorldInfo":{
        "favoriteCharitableCauses":"myFavoriteCauses",
        "regionsAndCharitableNeedsICareAbout":"regionsAndCountriesICareAbout",
        "metropolitanAreasWhoseCharitableNeedsICareAbout":"metropolitanAreasICareAbout",
        "ethnicGroupsWhoseCharitableNeedsICareAbout":"ethnicCommunitiesICareAbout",
        "religiousGroupsWhoseCharitableNeedsICareAbout":"religiousCommunitiesICareAbout",
        "favoriteNonprofitOrganizations":"myFavoriteNonprofits",
        "howMyLifestyleIsMakingtheWorldBetterPlace":"mySustainableLifeStyle",
        "volunteeringCommunityService":"myVolunteeringAndCommunityService",
        "myFundraisingActivities":"myCharitableFundrasing",
        "charitableWishlists":"charitableWisLists",
        "If_you_have_Charitable_Wish_List_provide_URL":"wishListUrl"
    },
}

replaceColumn = {
        "Degree":"degree",
        "Crop_it_to_square":"headshotPhoto",
        "myPlansForFuture":"myPlan",
        "myExtracurricularActivities":"myExtracurriculars",
        "favoriteBook":"myFavoriteBooks",
        "favoriteQuote":"myFavoriteQuote",
        "favoriteCharitableCauses":"myFavoriteCauses",
        "regionsAndCharitableNeedsICareAbout":"regionsAndCountriesICareAbout",
        "metropolitanAreasWhoseCharitableNeedsICareAbout":"metropolitanAreasICareAbout",
        "ethnicGroupsWhoseCharitableNeedsICareAbout":"ethnicCommunitiesICareAbout",
        "religiousGroupsWhoseCharitableNeedsICareAbout":"religiousCommunitiesICareAbout",
        "favoriteNonprofitOrganizations":"myFavoriteNonprofits",
        "howMyLifestyleIsMakingtheWorldBetterPlace":"mySustainableLifeStyle",
        "volunteeringCommunityService":"myVolunteeringAndCommunityService",
        "myFundraisingActivities":"myCharitableFundrasing",
        "charitableWishlists":"charitableWisLists",
        "If_you_have_Charitable_Wish_List_provide_URL":"wishListUrl"
}

csv_file_path = 'new_cleaned_data.csv'

df = pd.read_csv(csv_file_path)

df.rename(columns=replaceColumn, inplace=True)
df.to_csv('updated_file.csv', index=False)
