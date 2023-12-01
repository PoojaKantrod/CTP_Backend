import os
import pandas as pd
import re
import csv
# Load raw data from CSV into a DataFrame
raw_data = pd.read_csv('data/05 JF input - CTP - Profiles - College - Students 2021_07_25 - jotform clean.csv')
# Function to generate default order numbers
#def generate_default_order_number(index):
    #return f'#s{index:04d}'  # Format the index with leading zeros
def clean_name(name):
    # Check if the value is a string
    if isinstance(name, str):
        # Remove numeric characters and convert names to title case
        cleaned_name = re.sub(r'\d', '', name)
        return cleaned_name.strip().title()
    return name
def clean_email(email):
    # Convert email addresses to lowercase
    return email.lower() if pd.notnull(email) else email
def clean_order_number(order_number):
    # Remove emails and text from order numbers
    return re.sub(r'[^0-9#]', '', order_number)
last_Order_number = 1  # Initialize the order number
def generate_order_number(email):
    global last_Order_number  # Use the global variable to track the last order number
    if pd.notnull(email):
        last_order_number += 1
        return email
    else:
        order_number = f'#{last_Order_number}'
        last_order_number += 1
        return Order_number
# Generate default order numbers for rows with empty 'Order_number' column
#raw_data['Order_number'] = raw_data.apply(lambda row: generate_default_order_number(row.name) if pd.isna(row['Order_number']) else row['Order_number'], axis=1)
raw_data['First_Name'] = raw_data['First_Name'].apply(clean_name)
raw_data['Middle_Name'] = raw_data['Middle_Name'].apply(clean_name)
raw_data['Last_Name'] = raw_data['Last_Name'].apply(clean_name)
# Convert valid numeric values to integers and replace invalid values with NaN
#raw_data['Graduation_Year'] = pd.to_numeric(raw_data['Graduation_Year'], errors='coerce', downcast='integer')
# Remove ".0" from valid numeric values
#raw_data['Graduation_Year'] = raw_data['Graduation_Year'].apply(lambda x: str(x).replace('.0', '') if pd.notnull(x) else x)
# Convert the column to string type
#raw_data['Graduation_Year'] = raw_data['Graduation_Year'].astype(str)
columns_to_remove=['Ryzer', 'Submission_ID']
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
columns_to_remove_all=['Graduation_Year','My_Skills.1','check_this_if_national_sorority_not_found','cannot_find_school_Please_provide_it ','Year_of_undergrad_graduation', 'My_CommunityService_Volunteering','Languages_you_speak ','Honors_and_Awards','Tell_about_your_activities', 'Show_me','One_last_step_show_your_online_presence','Strava_com_2','Video_1_Choose_your_platform','Video_1_Embed_code_if_YouTube','Video_1_Embed_code_if_TikTok','Video_2_Choose_your_platform','Video_2_Embed_code_if_YouTube','Video_2_Embed_code_if_TikTok',' This_shows_current_date_time','Are_you_finished ','No_Label','No_Label_2','Her_Campus','Be_Recruited_com', 'Order_number', 'Birthdate', 'Email_Used',
    ' Name_your_other_national_organization_which_you_cannot_find ','If_your_national_social_fraternity_not_found',
    'If_your_women_sports_team_not_found_please_check_this ','If_your_men_sports_team_not_found_please_check_this','If_your_national_organizations_not_found_in_list_please_check', 'Places_I_Have_Lived','Places_I_Have_Traveled','My_Favorite_Podcasts']
raw_data = raw_data.drop(columns=columns_to_remove_all)
column_mapping = {
    'Unique_ID': 'uniqueId',
    'First_Name': 'firstName',
    'Middle_Name': 'middleName',
    'Last_Name': 'lastName',
    'usUndergradSchool': 'usUndergradSchool',
    'usOrCanadianOrInternationalSchool': 'usOrCanadianOrInternationalSchool',
    'cannot_find_your_undergraduate_school_Provide_it ': 'cannotFindSchoolPleaseProvideIt',
    'Degree': 'degree',
    'High-resolution_banner_photo': 'bannerPhoto',
    'Crop_it_to_square': 'headshotPhoto',
    'About_Me': 'aboutMe',
    'My_Plans_for_Future': 'myPlan',
    'My_Academics ': 'myAcademics',
    'My_Extracurricular_Activities': 'myExtracurriculars',
    'My_Athletics': 'myAthletics',
    'My_Jobs_Internships': 'myJobsInternships',
    'My_Honors_Awards': 'myHonorsAwards',
    'My_Skills': 'mySkills',
    'My_Languages': 'myLanguages',
    'Favorite_Book': 'myFavoriteBooks',
    'Favorite_Quote': 'myFavoriteQuote',
    'My_Thoughts_on_Making_a_Difference': 'myThoughtsOnMakingADifference',
    'Favorite_Charitable_Causes': 'myFavoriteCauses',
    'Regions_Whose_Charitable_Needs_I_Care_About': 'regionsAndCountriesICareAbout',
    'Metropolitan_Areas_Whose_Charitable_Needs_I_Care_About': 'metropolitanAreasICareAbout',
    'Ethnic_Groups_Whose_Charitable_Needs_I_Care_About': 'ethnicCommunitiesICareAbout',
    'Religious_Groups_Whose_Charitable_Needs_I_Care_About': 'religiousCommunitiesICareAbout',
    'Favorite_Nonprofit_Organizations. ': 'myFavoriteNonprofits',
    'How_My_Lifestyle_is_Making_the_World _Better_Place': 'mySustainableLifeStyle',
    'Volunteering_Community_Service': 'myVolunteeringAndCommunityService',
    'My_Fundraising_Activities': 'myCharitableFundrasing',
    'Feel_free_to_edit_this_message_about_Charitable_Wish_Lists ': 'charitableWisLists',
    'If_you_have_Charitable_Wish_List_provide_URL.': 'wishListUrl',
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
    'SwimCloud': 'swimCloud',
}
# Rename columns using the mapping dictionary
raw_data.rename(columns=column_mapping, inplace=True)
# List of columns to exclude from special character removal
exclude_columns = [
    'uniqueId', 'orderNumber', 'emailUsed', 'birthDate', 'bannerPhoto', 'headshotPhoto', 'wishListUrl','yourOwnWebsite', 'yourBlog',
    'LinkedIn', 'Instagram', 'Twitter', 'Facebook', 'GooglePlus',
    'Pinterest', 'Youtube', 'Flickr', 'Behance', 'Tumblr', 'Etsy',
    'WayUp', 'academiaEdu', 'Researchgate', 'Digication', 'Issuu', 'VSCO',
    '500px', 'helperHelper', 'Github', 'projectsThatMatterorg', 'Quora',
    'TikTok', 'Strava', 'sportsRecruits', 'mileSplit', 'prestoSports',
    'Harri', 'eliteProspects', 'Hudl', 'maxPreps', 'NCSA', 'athleticNet',
    'medium', 'twitch', 'soundCloud', 'artStation', 'firstRobotics',
    'Patreon', 'soundClick', 'bandcamp', 'vexRobotics', 'Rivals', 'swimCloud'
]
# Ensure all columns are of string data type
raw_data = raw_data.astype(str)
# Define a custom regular expression pattern to keep the period (.) while removing other special characters
pattern = '[^a-zA-Z0-9#s#p\s.]'
# Remove special characters using the custom pattern for selected columns
for col in raw_data.columns:
    if col not in exclude_columns:
        raw_data[col] = raw_data[col].apply(lambda cell: re.sub(pattern, '', cell) if isinstance(cell, str) else cell)
# Replace "nan" with an empty string ('') in the DataFrame
raw_data = raw_data.replace('nan', '', regex=False)
current_directory = os.getcwd()
# Specify the file name for the CSV in the current directory
csv_file_name = 'cleaned_data.csv'
# Create the full path to the CSV file
csv_file_path = os.path.join(current_directory, csv_file_name)
# Use the to_csv method to save the DataFrame to a CSV file
raw_data.to_csv(csv_file_path, index=False, quoting=csv.QUOTE_ALL)