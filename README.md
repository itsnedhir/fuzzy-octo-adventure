# fuzzy-octo-adventure

# Overview 

This a simple project that consists of a simple web application that allo users to subscribe to events. 
The app contains two areas: User Area and Admin Area. This app demonstrates, the concept of :
- User Authentication
- Authorization and Role based access
- CRUD operations on a database model
- Dockerizing the app 
- CI/CD pipeline using Github Actions


# Tech Stack
- Python > 3.11
- Flask
- Gunicorn
- MySQL & SQLAlchemy
- Docker & Docker Compose
- Github Actions

# Specifications

## User Area

### User Registration
- Users can register to the app by providing the following information:
    - First Name
    - Last Name
    - Email
    - Password
    - Confirm Password

These information will be stored in the database. Passwords will be hashed using `bcrypt` before storing them in the database.

### User Login
- Users can login to the app by providing the following information:
    - Email
    - Password

### User Event Subscription
- Users can access the list of events and subscribe to an event by providing its id.


## Admin Area

### User Management
- Admins can access the list of users and perform these actions : 
    - Sgrant or revoke access/scopes for userscope **TBD** 

### Event Management
- Admins can access the list of events and perform these actions : 
    - Create a new event
        - Event Title
        - Event Description
        - Event Date
        - Event Location
    - Update an existing event
    - Delete an existing event


# Project Structure

```bash
├── 📁 app # Contains the source code of the application 
│   ├── 📁 api # Contains the API routes of the application (Flask Blueprints)
│   ├── 📁 models # Contains the database models of the application (ORM SQL Alchemy)
│   ├── 📁 utils # Contains the utility functions of the application
│   └── 📁 tests # Contains the unit tests of the application
│   └──    main.py # Entry points of the Application (where blueprints are registered)
│   └──    Dockerfile # Dockerfile for the app service
│   └──    requirements.txt # Python dependencies for the app service
├── 📁 db # Contains the database SQL init scripts and migrations 
├── docker-compose.yml # Docker compose for app and MySQL services
├── 📁 .github # Contains the Github Actions workflows
```


# Development Setup

## Prerequisites
- Python >= 3.11
- Docker
- Docker Compose

## Steps
### Without Docker and with SQLite DB
#### Step by step
- Create a virtual environment
    ```bash
    pyenv local 3.11.0 # or use any other python version manager to install python 3.11.0
    git clone git@github.com:itsnedhir/fuzzy-octo-adventure.git
    cd fuzzy-octo-adventure
    python -m venv .venv
    source .venv/bin/activate
    pip install -r app/requirements.txt
    ```
- PYTHONPATH Setup: in order to use complete imports in our app (like `from app.models.xxx import yyy`), we need to set the PYTHONPATH inside our virtualenv to include to the root of the project. 
    ```bash
    export PYTHONPATH=$PYTHONPATH:$(pwd)
    ```

- Using SQLite DB [In the version without MySQL service]
SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process. 
Quickstart: https://docs.python.org/3/library/sqlite3.html 
#### Run the setup script
- Simply run the bash script `setup.sh` that create and activate the virtualenv :
    ```bash
    ./setup.sh
    ```

#### Run the app
- We will serve the app using Guicorn Server (in debug mode for dev run this) : 
    ```bash
    cd app # Make sure you are inside app directory before running the command
    gunicorn --timeout=60 --workers=2 --threads=1 --worker-class=sync -b 0.0.0.0:5000 --log-level DEBUG --reload main:app
    ```












