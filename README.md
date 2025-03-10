# Todo App API

This project provides a Todo API where users can view and manage only their own todo lists. Users can add new todos, update or delete existing ones. Additionally, only authorized users can perform actions. 

## Features

- **User Authentication**: Users can log in using token authentication via `dj-rest-auth`.
- **User Registration**: Users can register using `allauth`, and upon registration, a token is automatically created.
- **Todo Management**: Users can only view, update, or delete their own todos.
- **Swagger Support**: The API comes with Swagger documentation for testing purposes.
- **Access Control**: Unauthenticated users cannot access the API.

## Technologies

- **Django**: Backend framework
- **Django REST Framework**: API development
- **dj-rest-auth**: Token authentication
- **Django Allauth**: User registration and login management
- **Swagger**: API documentation
- **Docker**: You can create an image and run the container using Dockerfile

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/aykhanko/API-Simple-Todo-DB-SQLITE.git
2. Open the Folder
3. Create .env inside the folder
   ```bash
   python -m venv .env
4. Activate .env (Windows)
    ```bash
   .env\scripts\activate 
5. Activate .env (Linux)
    ```bash
   source .env/bin/activate 
5. Install requirements
    ```bash
   pip install requirements.txt
5. Run local server
    ```bash
   python manage.py runserver
