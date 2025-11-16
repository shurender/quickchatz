# quickchatz
#This documentation is an detailed overview of the project going from basics knowledge needed to develope to final end result of the project
what is quickchatz?
quickchat is a secure, real-time chat web app where users sign up/login, create rooms, and chat live — using Django + Channels + Redis, with frontend using Django templates and plain JavaScript.

QuickChatz — Beginner-Friendly Setup Guide

This guide explains everything from installing tools to running the project.
It is written in simple steps so a beginner can follow along easily.

0. Before You Start
Make sure these tools are installed on your system:
Python
Visual Studio Code
Git

1. Create and Open Your Project Folder

Create a folder on your computer, for example:
quickchatz
Open VS Code
Go to File → Open Folder → select the quickchatz folder

2. Set Up Git and GitHub
Step 1: Create a GitHub Repository
Visit GitHub and create a new repository
Name it: quickchatz
Copy the repository URL

Step 2: Initialize Git in your project folder
Open the terminal in VS Code and run:
git init

Step 3: Connect GitHub repository
git remote add origin <your-repo-url>

Step 4: Make your first commit
git add .
git commit -m "Initial commit"
git push -u origin main

3. Create and Activate a Virtual Environment
A virtual environment keeps your project’s Python packages separate.
Create venv:
python -m venv venv
Activate venv (Windows):
venv\Scripts\activate
Your terminal should now show:
(venv)

4. Install Required Packages for QuickChatz
Install only the dependencies needed for this project:
pip install Django channels channels_redis redis gunicorn python-dotenv
Save the installed packages:
pip freeze > requirements.txt

5. Create the Django Project
Create the main Django project inside the current folder:
django-admin startproject quickchatz .
The dot at the end means “create project in this folder”.

6. Create the Chat App
This app will contain the chat functionality.
python manage.py startapp chat
This creates a folder named chat where you will add all chat-related code.

7. Run the Project to Test
Run the development server:
python manage.py runserver
Open the link shown in the terminal, usually:
http://127.0.0.1:8000/

If the Django welcome page appears, your setup is correct.


Requirements and skillz
Python basics — syntax, functions, classes, virtual environments
Git & GitHub basics — init repo, add, commit, push, branch, pull request
Django fundamentals — project/app, models, views, templates, static files, migrations
Django Authentication — user model, login/logout, @login_required
HTML & CSS basics — structure and layout for the chat UI
JavaScript basics — DOM selection, event listeners, JSON
WebSockets concept — what a WebSocket connection is and how it works (client ↔ server)
Django Channels basics — ASGI, consumers, channel layers
Redis basics — purpose as a channel layer (not deep Redis commands)
Deploying Django — database config (Postgres), env vars, static files, HTTPS
Security basics — secret keys, HTTPS, CORS, input validation
