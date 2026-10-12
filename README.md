# Employee Management REST API

A backend application built with **Python, Django, Django REST Framework, SQLite, and Django ORM** to manage employee records through RESTful APIs.

## Features

- **CRUD Operations:** Create, retrieve, update, and delete employee records.
- **RESTful APIs:** Handle requests and return employee data in JSON format.
- **Database Integration:** Store and manage records using SQLite and Django ORM.
- **Input Validation:** Validate employee information, email addresses, and salary values.
- **Pagination:** Retrieve employee records in manageable pages.
- **Django Admin:** Manage employee records through the Django admin interface.
- **Automated Testing:** Test API endpoints and core employee management operations.

## Tech Stack

- **Language:** Python 3.x
- **Framework:** Django
- **API Framework:** Django REST Framework
- **Database:** SQLite
- **ORM:** Django ORM
- **Testing:** Django Test Framework, REST Framework `APITestCase`
- **Version Control:** Git and GitHub

## Project Structure

```text
django-employee-management-api/
├── employee_api/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── employees/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   └── views.py
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

## Getting Started

### Prerequisites

Install Python 3.10 or later and Git.

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/django-employee-management-api.git
cd django-employee-management-api
```

Replace `YOUR-USERNAME` with your GitHub username.

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows:

```bash
.venv\Scripts\activate
```

On macOS/Linux:

```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Apply Database Migrations

```bash
python manage.py migrate
```

### 5. Start the Development Server

```bash
python manage.py runserver
```

Open the following URL in your browser:

`http://127.0.0.1:8000/api/employees/`

You can use Django REST Framework's browsable API to interact with the endpoints.

## API Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| GET | `/api/employees/` | Retrieve the employee list |
| POST | `/api/employees/` | Create an employee |
| GET | `/api/employees/{id}/` | Retrieve an employee by ID |
| PUT | `/api/employees/{id}/` | Replace an employee record |
| PATCH | `/api/employees/{id}/` | Update selected employee fields |
| DELETE | `/api/employees/{id}/` | Delete an employee |

## Example API Request

Create an employee by sending a `POST` request to `/api/employees/` with the following JSON body:

```json
{
  "full_name": "Priya Das",
  "email": "priya@example.com",
  "department": "Engineering",
  "job_title": "Backend Developer",
  "salary": "600000.00",
  "date_joined": "2025-03-01"
}
```

A successful request returns the created employee record with an HTTP `201 Created` status.

## Data Model

The Employee model contains the following fields:

- `id`: Unique employee identifier, generated automatically.
- `full_name`: Employee's full name.
- `email`: Unique email address.
- `department`: Employee's department.
- `job_title`: Employee's job title.
- `salary`: Employee's salary.
- `date_joined`: Employee's joining date.

## Input Validation

The API uses Django REST Framework serializers to validate employee data before saving it.

- Email addresses must be valid.
- Duplicate email addresses are rejected.
- Employee names cannot be blank.
- Negative salary values are rejected.
- Invalid requests return validation errors.

## Running Tests

Execute the automated test suite with:

```bash
python manage.py test
```

The included tests cover employee listing, creation, updating, deletion, and duplicate-email validation.

## Future Improvements

- Add authentication and role-based permissions.
- Introduce filtering and searching by department or job title.
- Configure PostgreSQL for a production-oriented database setup.
- Add API documentation using Swagger or OpenAPI.
- Deploy the application to a hosting platform.

## Learning Outcomes

This project demonstrates practical application of **Python, Django, REST API development, Django ORM, relational database operations, input validation, and automated testing**.



