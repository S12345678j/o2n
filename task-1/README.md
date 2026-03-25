# 🚀 Student CRUD REST API

A production-style **Student Management REST API** built using **Flask**, following best practices like **RESTful design, Twelve-Factor App, testing, and clean architecture**.

---

# 📌 Features

* ✅ Student CRUD operations
* ✅ REST API with versioning (`/api/v1`)
* ✅ Database integration (SQLAlchemy)
* ✅ DB migrations (Flask-Migrate)
* ✅ Environment-based configuration
* ✅ Healthcheck endpoint
* ✅ Unit testing with pytest
* ✅ Makefile automation
* ✅ Simple UI for interaction

---

# 🧱 Tech Stack

| Layer     | Technology                        |
| --------- | --------------------------------- |
| Backend   | Flask                             |
| Database  | SQLite (extendable to PostgreSQL) |
| ORM       | SQLAlchemy                        |
| Migration | Flask-Migrate (Alembic)           |
| Testing   | Pytest                            |
| Config    | python-dotenv                     |
| UI        | HTML + JavaScript                 |

---

# 📁 Project Structure

```
SRE-Bootcamp/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── db.py
│
├── templates/
│   └── index.html
│
├── tests/
│   └── test_routes.py
│
├── migrations/
├── instance/
├── run.py
├── requirements.txt
├── Makefile
├── README.md
└── .env
```

---

# ⚙️ Setup & Installation

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd SRE-Bootcamp
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment

Create `.env` file:

```
DATABASE_URL=sqlite:///students.db
```

---

## 5️⃣ Run Database Migration

```bash
flask db upgrade
```

---

## 6️⃣ Run Application

```bash
make run
```

App will start at:

```
http://127.0.0.1:5000/
```

---

# 🌐 API Endpoints

Base URL:

```
/api/v1/students
```

| Method | Endpoint | Description      |
| ------ | -------- | ---------------- |
| POST   | /        | Create student   |
| GET    | /        | Get all students |
| GET    | /<id>    | Get student      |
| PUT    | /<id>    | Update student   |
| DELETE | /<id>    | Delete student   |

---

# ❤️ Healthcheck

```
GET /healthcheck
```

Response:

```json
{
  "status": "ok"
}
```

---

# 🖥️ UI

Access UI in browser:

```
http://127.0.0.1:5000/
```

Features:

* Add student
* View students
* Delete student

---

# 🧪 Running Tests

```bash
make test
```

* Uses pytest
* In-memory database for isolation

---

# 🛠️ Makefile Commands

```
make run       # Run app
make test      # Run tests
make migrate   # Create migration
make upgrade   # Apply migration
```

---

# 🔐 Configuration

Uses environment variables (12-Factor App):

```
DATABASE_URL=sqlite:///students.db
```

---

# 📊 Logging

* Info logs → creation/update
* Warning logs → deletion

---

# 🧠 Key Concepts Implemented

* RESTful API design
* API versioning
* App factory pattern
* Blueprint architecture
* Environment-based configuration
* Database migrations
* Unit testing
* Basic UI integration

---

# 🚀 Future Improvements

* Docker & Docker Compose
* PostgreSQL integration
* Authentication (JWT)
* Input validation
* Rate limiting
* Prometheus + Grafana monitoring
* CI/CD (GitHub Actions)
* React frontend

---

# 🎯 Learning Outcomes

* Backend development with Flask
* Database handling using ORM
* Debugging real-world issues
* Writing testable code
* Applying DevOps practices

---

# 🏁 Conclusion

This project demonstrates a **production-ready backend system** with clean architecture, testing, and DevOps practices. It is suitable for:

* Backend Engineering roles
* Site Reliability Engineering (SRE)
* DevOps positions

---

⭐ If you found this useful, consider starring the repo!
