# 🧾 Employee Database Backend Project (Django)

This is a backend project built using Django that manages an employee database with CRUD functionality, form handling, and an interactive UI. It demonstrates core Django concepts like models, views, templates, forms, and database connectivity using MySQL.

---

## 🚀 Features

- 🔍 View all employee details in a styled HTML table
- 📝 Add, update, and delete employee records via Django forms
- ✅ ModelForm-based input validation
- 📦 MySQL database integration
- 🎨 Clean and responsive frontend using HTML + CSS
- 🔗 Django template inheritance and URL routing

---

## 🛠️ Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS
- **Database**: MySQL
- **Tools**: MySQL Workbench, Git, GitHub

---

## 📁 Project Structure

Employee-database-backend-project-using-django/
├── information/             # Main Django app
│   ├── models.py            # Defines the Employee model
│   ├── forms.py             # Contains the Employee ModelForm
│   ├── views.py             # Business logic for handling requests
│   ├── urls.py              # URL patterns specific to this app
│   └── templates/           # HTML templates
│       ├── welcome.html     # Welcome/landing page
│       └── employee_form.html # Form and table UI for employees
├── EmployeeDatabase/        # Django project configuration
│   ├── settings.py          # Main settings file with DB config
│   └── urls.py              # Root URL configurations
├── static/                  # (Optional) Static files like CSS/JS
├── manage.py                # Django management script
└── README.md                # Project documentation

