# Team Task Manager

A full-stack Team Task Manager web application built using Flask, PostgreSQL, and Streamlit.

The application allows users to:
- Create projects
- Add team members
- Create and assign tasks
- Track task progress
- View dashboard statistics
- Manage role-based access

---

# Tech Stack

## Backend
- Flask
- Flask JWT Extended
- SQLAlchemy
- PostgreSQL

## Frontend
- Streamlit

## Other Tools
- Postman
- GitHub
- Railway

---

# Features

## Authentication
- User Signup
- User Login
- JWT Authentication

## Project Management
- Create Projects
- Add Members
- View Projects

## Task Management
- Create Tasks
- Assign Tasks
- Update Task Status
- Delete Tasks

## Dashboard
- Total Projects
- Total Tasks
- Completed Tasks
- Pending Tasks

## Role-Based Access Control
- Admins can add members
- Only assigned users can update tasks
- Only creators can delete tasks

---

# Folder Structure

```bash
team-task-manager/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── config.py
│   ├── routes/
│   │    ├── auth.py
│   │    ├── projects.py
│   │    ├── tasks.py
│   │    └── dashboard.py
│
├── frontend/
│   └── streamlit_app.py
│
└── README.md