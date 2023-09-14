## Introduction

## MySQL Database

In the `MySQL_Database` folder, you'll find mock databases and tables, including a `wordpress_profile` table.

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

## Running the Flask Application

To use the Flask application for creating an API for student profiles, follow these steps:

1. Install Flask by running the following command in your command prompt or terminal:
  
2. Install the MySQL connector for Python using the following command:

3. Run the `flask_app.py` script. This script establishes a connection to the database using Flask and creates an API for student profile information.

## API Endpoints

You can access the API using the following endpoints:

- To view all student profiles in JSON format, navigate to:
- http://192.168.1.11:5000/api/profiles
- To access the data of a specific student, use the following URL pattern, replacing `Infl-college-student-0000280` with the student's identifier:
- http://192.168.1.11:5000/api/profile/Infl-college-student-0000280
  
