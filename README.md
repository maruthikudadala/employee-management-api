# 🏢 Employee Management API

A robust and secure RESTful API built with Django REST Framework for managing company employees. Features JWT authentication, complete CRUD operations, filtering, pagination, and comprehensive testing.

## ✨ Features

- **🔐 JWT Authentication** - Secure token-based authentication with refresh tokens
- **🔄 Complete CRUD Operations** - Create, Read, Update, Delete employees
- **🔍 Advanced Filtering** - Filter employees by department and role
- **📄 Smart Pagination** - 10 employees per page with navigation links
- **✅ Input Validation** - Email uniqueness, required fields, proper error messages
- **🧪 Comprehensive Testing** - Unit tests for all endpoints and edge cases
- **📚 Detailed Documentation** - Clear setup and usage instructions

## 🛠️ Tech Stack

**Backend Framework:** Django 4.2, Django REST Framework  
**Authentication:** JWT (Simple JWT)  
**Database:** SQLite (Development)  
**Testing:** Django Test Framework  
**Tools:** Postman, Git, GitHub

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

Step 1: Clone the Repository
git clone https://github.com/your-username/employee-management-api.git
cd employee-management-api

Step 2: Create Virtual Environment
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Configure Database
python manage.py makemigrations
python manage.py migrate


Step 5: Create Superuser 
python manage.py createsuperuser

Base URL
http://127.0.0.1:8000/api/


##API Endpoints
Employee Management
Method	  Endpoint	          Description	 
POST	    /employees/	        Create new employee	
GET	      /employees/	        List all employees	
GET	      /employees/{id}/	  Get specific employee	
PUT	      /employees/{id}/	  Update employee	
DELETE	  /employees/{id}/	  Delete employee	
