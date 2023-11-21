let profileInfo = {

    /* 1. Identifier Information */
    identificationInfo: {
        uniqueId: '0123456789',
        firstName: '',
        middleName: '',
        lastName: '',

        /* frontend schoolName field is extracted from these 3 backend fields */
        usUndergradSchool: '',
        usOrCanadianOrInternationalSchool: '',
        cannotFindSchoolPleaseProvideIt: '',

        Degree: '', // frontend field name: degree
        schoolWebsite: '', /* Jotform and Mocked Wordpress db does not include this field  -> orgLink */
        bannerPhoto: '',

        headshotPhoto: '', // It is Crop_it_to_square from Jotform before cleaning
    },


    /* 2. About Me sections */
    aboutMeInfo: {
        aboutMe: '',
        myPlansForFuture: '', // frontend field name: myPlan
        myAcademics: '',
        myExtracurricularActivities: '', // frontend field name: myExtracurriculars
        myAthletics: '',
        myJobsInternships: '',
        myHonorsAwards: '',
        mySkills: '',
        myLanguages: '',
        favoriteBook: '', //frontend field name: myFavoriteBooks
        favoriteQuote: '', //frontend field name: myFavoriteQuote
    },

    /* 3. What I am doing for a better world sections */
    betterWorldInfo: {
        myThoughtsOnMakingADifference: '',
        favoriteCharitableCauses: '', // frontend field name: myFavoriteCauses
        regionsAndCharitableNeedsICareAbout: '', // frontend field name: regionsAndCountriesICareAbout
        metropolitanAreasWhoseCharitableNeedsICareAbout: '', //frontend field name: metropolitanAreasICareAbout
        ethnicGroupsWhoseCharitableNeedsICareAbout: '', //frontend field name: ethnicCommunitiesICareAbout
        religiousGroupsWhoseCharitableNeedsICareAbout: '', //frontend field name: religiousCommunitiesICareAbout
        'favoriteNonprofitOrganizations': '', //frontend field name: myFavoriteNonprofits ; 
        howMyLifestyleIsMakingtheWorldBetterPlace: '', // frontend field name: mySustainableLifeStyle
        volunteeringCommunityService: '', //frontend field name: myVolunteeringAndCommunityService
        myFundraisingActivities: '', //frontend field name: myCharitableFundrasing
        charitableWishlists: '', //frontend field name: charitableWisLists

        wishListUrl: '', // no provided yet. It is `If_you_have_Charitable_Wish_List_provide_URL.` from Jotform before cleaning!
    },


    /* 4. Social Media Icons */
    // Ask backend team: how many social media links in total if a user enters all? Could we have that list?
    socialMediaIcons: [
        /* Example of 2 items. Backend team please return all social media links. We appreciate it! */
        {
            "platform": "LinkedIn",
            "iconUrl": "https://cdn.shopify.com/s/files/1/1842/4701/t/25/assets/round-icon-Linkedin.png?v=9479525859996414661639243590",
            "url": "https://www.linkedin.com/in/saidayashankar/"
        },
        {
            "platform": "Website",
            "iconUrl": "https://cdn.shopify.com/s/files/1/1842/4701/t/25/assets/round-icon-Website.png?v=181891691508174651511639243588",
            "url": "https://www.linkedin.com/in/saidayashankar/"
        },
    ],

    /* 5. Organisations and 6. Local Organisation */
    organisations: [
        // Example:
        {
            "iconURL": "https://www.energystar.gov/tmp/cal/GSA_logo-stackedjpg",
            "accountURL": "http://www.greenschoolsalliance.org/home"
        },
    ],


    localOrganisations: [
        //Example:
        {
            "name": "Model UN",
            "role": "Vice President"
        }
    ]


}