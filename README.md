## Introduction

## MySQL Database

In the `MySQL_Database` folder, you'll find mock databases and tables, including a `wordpress_profile` table.

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
  
