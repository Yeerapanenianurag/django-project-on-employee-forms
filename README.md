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
├── information/ # Main app
│ ├── models.py # Employee model
│ ├── forms.py # Employee form (ModelForm)
│ ├── views.py # View logic
│ ├── urls.py # App-specific URLs
│ └── templates/ # HTML templates
│ ├── welcome.html # Welcome page with project intro
│ └── employee_form.html # Form and table UI
├── EmployeeDatabase/ # Django project settings
│ ├── settings.py # Config and DB settings
│ └── urls.py # Project URLs
├── static/ # Static files (optional)
├── manage.py
└── README.md
