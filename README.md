### PROJECT  NAME 
 +  myBlock


## Description

 A web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

## Author
Ivy Jeptoo

## BDD

>Signup inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  | Account username, ``eg johndoe``|
| Email  | User email, ``eg johndoe@testmail.com``|
| Password  | Account password, ``eg password123``|
| Confirm Password  | Account password, ``eg password123``|

>Login Inputs

| Inputs |  Description |
| :---         |          ---: |
| Username  |Account username, ``eg johndoe``|
| Password  | Account password, ``eg 12345678``|

## User Story

- User can sign up if they have no account.

- User can login to their account.

- Fill in profile form to choose hood.

- User can view posted posts from other individuals and also make post.

- User can create alerts and view all alerts made.

- User can rate business.

- User can view their profile and edit their details.

- User can search business according to name.

- User can comment on posts.


## <a href="https://ivyblocks.herokuapp.com/">Live preview of the site</a>

## Set up instructions and installations

### Prerequisites

- python3.8

- python virtual environment ~ to create one run the following command `python3.8 -m venv --without-pip virtual`

- python pip ~ to install pip activate virtual environment `source virtual/bin/activate` then run `curl https://bootstrap.pypa.io/get-pip.py | python`

- Postgres ~ to install follow the following commands in your home directory:
    - `sudo apt-get update`
    - `sudo apt-get install postgresql postgresql-contrib libpq-dev`
    - `sudo service postgresql start`
    - `sudo -u postgres createuser --superuser $USER`
    - `sudo -u postgres createdb $USER`
    - `touch .psql_history`

### Installation instructions

- Clone the repo ~ `git clone https://github.com/IvyJeptoo/myBlock`

- Activate virtual environment: 
   `python3.6 -m venv --without-pip virtual` then `source virtual/bin/activate`

- Install all the dependancies in the requirements.txt file to get a development env running
   `pip3 install -r requirements.txt`

- Create a database 
  ```bash
  psql
  CREATE DATABASE 'your database name';
  ```

- Create .env file and paste the following filing where appropriate:
  ```python
  SECRET_KEY = '<Secret_key>'
  DBNAME = '<your db name>'
  USER = '<Username>'
  PASSWORD = '<password>'
  DEBUG = True
  ```

- Run initial migration
  ``` bash
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```

- Run the app

   - `python3 manage.py runserver`

- Open the `localhost:8000` to check if the app is running successfully.

## Development
#### Want to make a contribution to enhance an existing module or fix a bug? Great!
* Fork the repo
* Create a new branch (git checkout -b improve-feature)
* Make the appropriate changes in the files
* Add changes to reflect the changes made
* Commit your changes (git commit -am 'Improve feature')
* Push to the branch (git push origin improve-feature)
* Create a Pull Request

## Technologies used

    - python3.8
    - Django4.0.4
    - Bootstrap
    - Postgresql

## Known Bugs
No known bugs, just that some functionalities were not fully implemented
#### 
If you find a bug (the website couldn't handle the query and or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.
## Contact Information
* For any inqueries feel free to write to me through
  + ivy.jeptoo@student.moringaschool.com

## Licence
* MIT License
* Copyright (c) 2022 Ivy Jeptoo




