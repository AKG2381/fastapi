# FastAPI Todos Application

This is a Todos application built with FastAPI and SQLite.

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
3. [Running the Application](#running-the-application)
4. [Creating Users](#creating-users)
5. [Testing the APIs](#testing-the-apis)

## Requirements
- Python version > 3.10
- SQLite3 installed and configured

## Installation
Clone the repository and navigate to the project directory:
- git clone https://github.com/AKG2381/fastapi.git
- cd fastapi/Project3
- python libraries to install :
- pip install fastapi "uvicorn[standard]" bcrypt==4.0.1 cryptography psycopg2-binary PyMySQL python-jose python-multipart SQLAlchemy uvicorn passlib pytest httpx pytest-asyncio aiofiles jinja2 "python-jose[cryptography]"

## Running the Application
Start the FastAPI server with:
- uvicorn TodoApp.main:app --reload
The application will be available at: http://127.0.0.1:8000/docs


## Creating Users
To create users with different roles, use the following steps:

1. Open the Swagger UI at: http://127.0.0.1:8000/docs

2. Use the /auth/create_user endpoint to create a new user. An example request body for creating an admin user:
   {
     "username": "user1",
     "email": "user1@gmail.com",
     "first_name": "user1",
     "last_name": "user_last_name",
     "password": "test12345",
     "role": "admin",
     "phone_number": "1234567890"
   }

3. Test different APIs using the Swagger UI.

## Testing the APIs
To run the tests for the APIs, navigate to the project directory and run:
- cd fastapi/Project3
- python -m pytest --disable-warnings

