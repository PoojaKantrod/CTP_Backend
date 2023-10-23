
import pandas as pd
# Load raw data from CSV into a DataFrame
raw_data = pd.read_csv('05 JF input - CTP - Profiles - College - Students 2021_07_25 - jotform clean.csv')

def clean_name(name):
    # Convert names to title case and remove leading/trailing whitespaces
    return name.strip().title() if pd.notnull(name) else name

def clean_email(email):
    # Convert email addresses to lowercase
    return email.lower() if pd.notnull(email) else email

def clean_date(date):
    # Assuming date is in MM/DD/YYYY format, convert to YYYY-MM-DD
    try:
        parts = date.split('/')
        return f"{parts[2]}-{parts[0].zfill(2)}-{parts[1].zfill(2)}"
    except (AttributeError, IndexError):
        return None


raw_data['First_Name'] = raw_data['First_Name'].apply(clean_name)
raw_data['Middle_Name'] = raw_data['Middle_Name'].apply(clean_name)
raw_data['Last_Name'] = raw_data['Last_Name'].apply(clean_name)
raw_data['Email_Used'] = raw_data['Email_Used'].apply(clean_email)
raw_data['Birthdate'] = raw_data['Birthdate'].apply(clean_date)

columns_to_remove=['High-resolution_banner_photo','Ryzer', 'Submission_ID']
column_names = raw_data.columns.tolist()

raw_data = raw_data.drop(columns=columns_to_remove)

import numpy as np
field1 = raw_data['US_school_withA-M']
field2 = raw_data['US_Schools']

# Combine the two fields using an OR operation
usOrCanadianOrInternationalSchool = np.where(field1.notnull(), field1, field2)

# Find the index of one of the original fields (e.g., 'Field1')
insert_index = raw_data.columns.get_loc('US_school_withA-M')

# Remove the original fields
raw_data.drop(['US_school_withA-M', 'US_Schools'], axis=1, inplace=True)

# Insert the combined field at the found index
raw_data.insert(loc=insert_index, column='usOrCanadianOrInternationalSchool', value=usOrCanadianOrInternationalSchool)


field1 = raw_data['US_undergrads-school_withA-M']
field2 = raw_data['US_undergrads-school_withN-Z ']
field3 = raw_data['Canadian_undergrad_school']
field4 = raw_data['Other_international_undergrad_school']

usUndergradSchool = np.where(field1.notnull(), field1, field2)

# Find the index of one of the original fields (e.g., 'Field1')
insert_index = raw_data.columns.get_loc('US_undergrads-school_withA-M')

# Remove the original fields
raw_data.drop(['US_undergrads-school_withA-M', 'US_undergrads-school_withN-Z ', 'Canadian_undergrad_school', 'Other_international_undergrad_school'], axis=1, inplace=True)


# Insert the combined field at the found index
raw_data.insert(loc=insert_index, column='usUndergradSchool', value=usUndergradSchool)

# %%
column_names = raw_data.columns.tolist()
columns_to_remove_all=['My_Skills.1','check_this_if_national_sorority_not_found','cannot_find_school_Please_provide_it ','Year_of_undergrad_graduation', 'My_CommunityService_Volunteering','Languages_you_speak ','Honors_and_Awards','Feel_free_to_edit_this_message_about_Charitable_Wish_Lists ','Tell_about_your_activities','If_your_national_social_fraternity_not_found','If_your_national_organizations_not_found_in_list_please_check', 'Show_me','If_your_men_sports_team_not_found_please_check_this','If_your_women_sports_team_not_found_please_check_this ','One_last_step_show_your_online_presence','Strava_com_2','Video_1_Choose_your_platform','Video_1_Embed_code_if_YouTube','Video_1_Embed_code_if_TikTok','Video_2_Choose_your_platform','Video_2_Embed_code_if_YouTube','Video_2_Embed_code_if_TikTok',' This_shows_current_date_time','Are_you_finished ','No_Label','No_Label_2','Her_Campus','Be_Recruited_com']
raw_data = raw_data.drop(columns=columns_to_remove_all)

column_mapping = {
    'Unique_ID': 'uniqueId',
    'First_Name': 'firstName',
    'Middle_Name': 'middleName',
    'Last_Name': 'lastName',
    'Order_number': 'orderNumber',
    'Email_Used': 'emailUsed',
    'Birthdate': 'birthDate',
    'Crop_it_to_square': 'bannerPhoto',
    'usOrCanadianOrInternationalSchool': 'usOrCanadianOrInternationalSchool',
    'cannot_find_your_undergraduate_school_Provide_it ': 'cannotFindSchoolPleaseProvideIt',
    'Degree': 'Degree',
    'Graduation_Year': 'graduationYear',
    'usUndergradSchool': 'usUndergradSchool',
    'About_Me': 'aboutMe',
    'My_Academics ': 'myAcademics',
    'My_Extracurricular_Activities': 'myExtracurricularActivities',
    'My_Athletics': 'myAthletics',
    'My_Plans_for_Future': 'myPlansForFuture',
    'My_Jobs_Internships': 'myJobsInternships',
    'My_Skills': 'mySkills',
    'My_Languages': 'myLanguages',
    'My_Honors_Awards': 'myHonorsAwards',
    'Favorite_Book': 'favoriteBook',
    'Favorite_Quote': 'favoriteQuote',
    'Favorite_Charitable_Causes': 'favoriteCharitableCauses',
    'Regions_Whose_Charitable_Needs_I_Care_About': 'regionsAndCharitableNeedsICareAbout',
    'Metropolitan_Areas_Whose_Charitable_Needs_I_Care_About': 'metropolitanAreasWhoseCharitableNeedsICareAbout',
    'Ethnic_Groups_Whose_Charitable_Needs_I_Care_About': 'ethnicGroupsWhoseCharitableNeedsICareAbout',
    'Religious_Groups_Whose_Charitable_Needs_I_Care_About': 'religiousGroupsWhoseCharitableNeedsICareAbout',
    'How_My_Lifestyle_is_Making_the_World _Better_Place': 'howMyLifestyleIsMakingtheWorldBetterPlace',
    'Favorite_Nonprofit_Organizations. ': 'favoriteNonprofitOrganizations.',
    'Volunteering_Community_Service': 'volunteeringCommunityService',
    'My_Fundraising_Activities': 'myFundraisingActivities',
    'If_you_have_Charitable_Wish_List_provide_URL.': 'charitableWishlists',
    'Do_you_belong_to_Greek': 'doYouBelongToGreek',
    'Share_your_national_social_fraternity_membership': 'shareYourNationalSocialFraternityMembership',
    'Name_your_national_social_fraternity_not_found_in_the_list_above': 'nameYourNationalSocialFraternityIfNotInList',
    'Share_your_national_social_sorority_membership': 'shareYourNationalSocialSororityMembership',
    'Name_your_national_social_sorority_not_found_in_list?': 'nameYourNationalSocialSororityIfNotInList',
    'List_eight_national_fraternity_associations_you_belong': 'yourNationalFraternityAssociations',
    'If_your_national_fraternity_association_not_found ': 'yourNationalFraternityAssociationIfNotInList',
    ' Name_your_national_fraternity_association_not_found': 'yourNationalFraternityAssociationIfNotInList',
    'List_national_organizations_membership_you_belong': 'yourNationalOrganizationsMembership',
    ' Name_your_other_national_organization_which_you_cannot_find ': 'YourOtherNationalOrganizationWhichYouCannotFind',
    'Men_Sports_Teams': 'menSportsTeam',
    'Women_Sports_Teams': 'womenSportsTeam',
    'Name_of_your_men_sports_team_not_found ': 'yourMenSportsTeamIfNotInList',
    'Name_of_your_women_sports_team_not_found ': 'yourWomenSportsTeamIfNotInList',
    'Include_twelve_student_clubs_to_which_you_belong': 'includeTwelveStudentclubsToWhichYouBelong',
    'Your_Own_Website': 'yourOwnWebsite',
    'Your_Blog': 'yourBlog',
    'LinkedIn': 'LinkedIn',
    'Instagram': 'Instagram',
    'Twitter': 'Twitter',
    'Facebook': 'Facebook',
    'Google_Plus': 'GooglePlus',
    'Pinterest': 'Pinterest',
    'Youtube': 'Youtube',
    'Flickr': 'Flickr',
    'Behance': 'Behance',
    'Tumblr': 'Tumblr',
    'Etsy': 'Etsy',
    'Way_Up': 'WayUp',
    'Academia_edu': 'academiaEdu',
    'Researchgate': 'Researchgate',
    'Digication': 'Digication',
    'Issuu': 'Issuu',
    'VSCO': 'VSCO',
    '500px': '500px',
    'Helper_Helper': 'helperHelper',
    'Github': 'Github',
    'Projects_ThatMatter_org': 'projectsThatMatterorg',
    'Quora_com': 'Quora',
    'TikTok_com': 'TikTok',
    'Strava_com': 'Strava',
    'SportsRecruits_com': 'sportsRecruits',
    'MileSplit_com': 'mileSplit',
    'PrestoSports_com': 'prestoSports',
    'Harri': 'Harri',
    'Elite_Prospects': 'eliteProspects',
    'Hudl': 'Hudl',
    'MaxPreps': 'maxPreps',
    'NCSA': 'NCSA',
    'Athletic_net': 'athleticNet',
    'Medium_com': 'medium',
    'Twitch_com': 'twitch',
    'SoundCloud': 'soundCloud',
    'ArtStation': 'artStation',
    'First_Robotics ': 'firstRobotics',
    'Patreon': 'Patreon',
    'SoundClick': 'soundClick',
    'Bandcamp': 'bandcamp',
    'Vex_Robotics ': 'vexRobotics',
    'Rivals': 'Rivals',
    'My_Thoughts_on_Making_a_Difference': 'myThoughtsOnMakingaDifference',
    'SwimCloud': 'swimCloud',
    'Places_I_Have_Lived': 'placesIHaveLived',
    'Places_I_Have_Traveled': 'placesIHaveTraveled',
    'My_Favorite_Podcasts': 'myFavoritePodcasts'
}

# Rename columns using the mapping dictionary
raw_data.rename(columns=column_mapping, inplace=True)

current_directory = os.getcwd()

# Specify the file name for the CSV in the current directory
csv_file_name = 'new_cleaned_data.csv'

# Create the full path to the CSV file
csv_file_path = os.path.join(current_directory, csv_file_name)

# Use the to_csv method to save the DataFrame to a CSV file
new_cleaned_data.to_csv(csv_file_path, index=False)