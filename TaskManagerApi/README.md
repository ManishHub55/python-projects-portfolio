# TaskManagerApi

A simple Task Manager API built with FastAPI, SQLAlchemy ORM, and PostgreSQL.

This project demonstrates how to perform real CRUD (Create, Read, Update, Delete) operations using SQLAlchemy and PostgreSQL, both through standalone Python scripts and REST API endpoints.

---

## Features

* Create tasks
* Read all tasks
* Read a task by ID
* Update task titles
* Delete tasks
* PostgreSQL database integration
* SQLAlchemy ORM
* FastAPI REST API

---

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* psycopg2

---

## Project Structure

```text
TaskManagerApi/
│
├── __init__.py
├── database.py
├── models.py
├── main.py
│
├── create_tables.py
├── insert_tasks.py
├── read_tasks.py
├── update_tasks.py
├── delete_tasks.py
│
├── requirements.txt
├── README.md
├── .gitignore
│
└── __pycache__/
```

---

## Database Model

### Task

| Column | Type                  |
| ------ | --------------------- |
| id     | Integer (Primary Key) |
| title  | String                |

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd TaskManagerApi
```

### 2. Create and activate virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## PostgreSQL Setup

Create a PostgreSQL database:

```sql
CREATE DATABASE taskdb;
```

Update the database connection string inside `database.py`:

```python
DATABASE_URL = "postgresql://YOUR_USERNAME:YOUR_PASSWORD@localhost/taskdb"
```

---

## Create Database Tables

Run:

```bash
python create_tables.py
```

Expected output:

```text
Tables created successfully
```

---

## CRUD Scripts

### Insert Task

```bash
python insert_tasks.py
```

Creates a new task:

```text
Learn FastAPI
```

---

### Read Tasks

```bash
python read_tasks.py
```

Example output:

```text
id:1 title:Learn FastAPI
id:2 title:LEARN REAL CRUD SYSTEM
```

---

### Update Task

```bash
python update_tasks.py
```

Updates the task with ID 2.

---

### Delete Task

```bash
python delete_tasks.py
```

Deletes the task with ID 2.

---

## FastAPI Endpoints

Start the API server:

```bash
uvicorn TaskManagerApi.main:app --reload
```

---

### Get All Tasks

```http
GET /tasks
```

---

### Get Task By ID

```http
GET /tasks/{id}
```

Example:

```http
GET /tasks/1
```

---

### Create Task

```http
POST /tasks?title=Learn SQLAlchemy
```

---

### Update Task

```http
PUT /tasks/{id}?new_title=Updated Task
```

Example:

```http
PUT /tasks/1?new_title=Master FastAPI
```

---

### Delete Task

```http
DELETE /tasks/{id}
```

Example:

```http
DELETE /tasks/1
```

---

## Concepts Practiced

* SQLAlchemy Engine
* SQLAlchemy Sessions
* ORM Models
* PostgreSQL Connection
* Table Creation
* Querying Data
* Filtering Records
* Updating Rows
* Deleting Rows
* FastAPI Dependency Injection
* REST API Development

---

## Learning Purpose

This project was created to learn:

* Database fundamentals
* SQLAlchemy ORM
* PostgreSQL integration
* CRUD operations
* FastAPI basics
* Backend development workflows

It serves as a foundation for building larger backend applications with FastAPI.

---

## Future Improvements

* Pydantic Schemas
* Request Validation
* Error Handling
* Response Models
* Async SQLAlchemy
* Authentication & Authorization
* Docker Support
* Unit Testing

---

## Author

Built as part of a backend development learning journey using Python, FastAPI, SQLAlchemy, and PostgreSQL.
