# 📚 LMS - Flask Learning Management System

This is a simple **Learning Management System (LMS)** web application built using **Flask** and **SQLAlchemy**.  
It allows basic management of courses using CRUD operations.

---

## 🚀 Features

- 📚 Add new courses  
- 📝 View all available courses  
- ✏️ Update course information  
- ❌ Delete courses  
- 🗄️ Database integration using SQLAlchemy  
- 🌐 Simple web interface using Flask templates  

---

## 🛠️ Technologies Used

- Python 🐍  
- Flask 🌐  
- Flask-SQLAlchemy 🗄️  
- HTML / CSS 🎨  
- SQLite Database  

---

## 📂 Project Structure

```
lms/
│
├── app.py
├── models.py
├── templates/
│   ├── index.html
│   ├── add.html
│   ├── update.html
│   └── base.html
│
├── static/
│   └── style.css
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/asfa-shamim/lms.git
```

### 2. Go to project folder
```bash
cd lms
```

### 3. Create virtual environment (recommended)
```bash
python -m venv venv
```

Activate it:
```bash
venv\Scripts\activate   (Windows)
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the project
```bash
python app.py
```

---

## 🌐 How it works

1. Run Flask application  
2. Open browser: `http://127.0.0.1:5000/`  
3. Perform CRUD operations on courses  
4. Data is stored in SQLite database  

---

## 💡 Future Improvements

- 🔐 User login system  
- 👨‍🎓 Student management module  
- 📊 Admin dashboard  
- 🎨 Better UI with Bootstrap  
- 📅 Attendance system  

---

## 👩‍💻 Author

**Asfa Shamim**  
Software Engineering Student | Flask Developer  

---

## ⭐ Support

If you like this project, don’t forget to give it a ⭐ on GitHub!
