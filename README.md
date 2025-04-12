# 📚 Library Management System (Django)

A simple web-based application to manage authors, books, and borrow records in a library using Django. Admins can add data, view paginated lists, and export everything to Excel — all behind a login screen.

---

## 🚀 Features

- ✅ User authentication (Login required)
- 📖 Add and list **Authors**, **Books**, and **Borrow Records**
- 📄 Pagination for clean display
- 📦 Export all data to **Excel**
- 🛡️ Admin-only access for modifications

---

## 🛠️ Technologies Used

- Python 3.10+
- Django 4.x
- SQLite (default DB)
- openpyxl (for Excel export)
- Bootstrap (for frontend, optional)

---

## 📁 Project Structure

```
library_system/
├── library/                  # App folder
│   ├── models.py             # DB Models
│   ├── forms.py              # Django Forms
│   ├── views.py              # Views/logic
│   ├── templates/library/    # HTML Templates
│   ├── urls.py               # App URLs
│   └── admin.py              # Admin site setup
├── library_system/           # Project settings
│   └── settings.py
├── manage.py                 # Django CLI
└── db.sqlite3                # Default DB
```

---

## ⚙️ Setup Instructions

### 1. 🔁 Clone the Repo

```bash
git clone https://github.com/your-username/Library-Management-System.git
cd Library-Management-System
```

> Replace `your-username` with your GitHub username.

### 2. 📦 Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. 📚 Install Dependencies

```bash
pip install -r requirements.txt
```

> If `requirements.txt` is missing, install manually:
```bash
pip install django openpyxl
```

### 4. 🏗️ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. 🔐 Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create admin credentials.

### 6. 🚦 Run the Server

```bash
python manage.py runserver
```

Now go to [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧩 Usage Guide

### 🔐 Login
Login using your admin credentials (created via `createsuperuser`)

### ➕ Add Entries
- **Add Author:** `/add_author/`
- **Add Book:** `/add_book/`
- **Add Borrow Record:** `/add_borrow_record/`

### 📋 View Lists
- **Authors:** `/list_authors/`
- **Books:** `/list_books/`
- **Borrow Records:** `/list_borrow_records/`

### 📤 Export All Data
- **Excel Export:** `/export_excel/`

---

## 🧼 Optional Cleanup

To ignore unnecessary files:

Create `.gitignore` with:

```
__pycache__/
*.pyc
db.sqlite3
.env
venv/
```

---



