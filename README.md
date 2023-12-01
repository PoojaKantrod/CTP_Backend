## Introduction

## MySQL Database

In the `MySQL_Database` folder, you'll find mock databases and tables, including a `wordpress_profile` table.

# Application Setup Guide

## Setting up Conda
Run enviroment.yml file using following command to setup conda for this project.
``` 
conda env create --file environment.yml
```

When installing new packages to the conda env, please export them using the following command for other developers
```
conda env export --from-history --name ctpbackend > environment.yml
```

## Setting up your .env file
Use the following command in your project terminal to copy paste .env.example file and create .env file
```
cp .env.example .env
```

Please go to .env file and add you local configuration or db server config if you have that.


## Data Cleaning

1. Execute the data cleaning script to generate a cleaned CSV file:

    ```bash
    python Data_cleaning.py
    ```

    This will create a file named `cleaned_data.csv`.

2. Access your MySQL database:

    ```bash
    mysql -u root -p
    ```

    Enter your password when prompted.

3. Switch to the `mock_data` database:

    ```sql
    use mock_data;
    ```

4. Verify the successful loading of cleaned data:

    ```sql
    SELECT degree FROM cleaned_data;
    ```

    Note: Replace "degree" with the desired field for verification.

## Running the Flask Application

1. Install Flask:

    ```bash
    pip install Flask
    ```

2. Install the MySQL connector for Python:

    ```bash
    pip install mysql-connector-python
    ```

3. Run the Flask application:

    ```bash
    python flask_app.py
    ```
    

## API Endpoints

You can access the API using the following endpoints:

- To view all student profiles in JSON format, navigate to:
- http://192.168.1.11:5000/api/profiles
- To access the data of a specific student, use the following URL pattern, replacing `Infl-college-student-0000280` with the student's identifier:
- http://192.168.1.11:5000/api/profile/Infl-college-student-0000280
- For adding a new record use http://192.168.1.11:5000/api/profile and put the json data from file `api_post_data.json` in body section.
  
## Use authentication via Postman to access the endpoints 
- Get the json file from team member for importing the collection in postman.
- Select `CTP Backend` after importing the json file. 
- Scroll down and click on `Get New Access Token` .
- Login in with cognito using credentials created for authentication. Once the token is generated rename it as `access_token`.
- Once this is done, under the API endpoints replace the value of cookie cognito_access_token with new token in Cookies [can be found under the send button] section.
- Once this is done, under the API endpoints replace the cookie cognito_access_token with new token in `Cookies` [can be found under the send button] section. 
- Now try running all the endpoints under the collection as mentioned in the above section <b>API EndPoints</b>. 
