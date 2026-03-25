# 🚀 Student CRUD REST API

A production-style **Student Management REST API** built using **Flask**, following best practices like **RESTful design, Twelve-Factor App, testing, clean architecture, and containerization**.

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
* ✅ 🐳 Dockerized with multi-stage build
* ✅ Runtime environment variable injection

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
| Container | Docker                            |

---

# 📁 Project Structure

```
SRE-Bootcamp/
│
├── app/
├── templates/
├── tests/
├── migrations/
├── instance/
├── Dockerfile
├── .dockerignore
├── Makefile
├── run.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Local Setup & Installation

## 1️⃣ Clone Repository

```bash
git clone <your-repo-url>
cd SRE-Bootcamp
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment

```env
DATABASE_URL=sqlite:///students.db
```

---

## 5️⃣ Run Migrations

```bash
flask db upgrade
```

---

## 6️⃣ Run Application

```bash
make run
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

---

# 🖥️ UI

```
http://127.0.0.1:5000/
```

---

# 🧪 Running Tests

```bash
make test
```

---

# 🛠️ Makefile Commands

```
make run
make test
make migrate
make upgrade
make build        # Docker build
make run-docker   # Run container
make stop-docker  # Stop container
```

---

# 🐳 Docker Setup (Multi-Stage Build)

## 🔨 Build Image (Semver Tagging)

```bash
docker build -t student-api:1.0.0 .
```

---

## ▶️ Run Container (Inject Env at Runtime)

```bash
docker run -d \
  -p 5000:5000 \
  -e DATABASE_URL=sqlite:///students.db \
  --name student-api \
  student-api:1.0.0
```

---

## 📦 Run Using .env File

```bash
docker run --env-file .env -p 5000:5000 student-api:1.0.0
```

---

## ⛔ Stop Container

```bash
docker stop student-api && docker rm student-api
```

---

# 🔐 Configuration (12-Factor App)

Environment variables are injected at runtime:

```
DATABASE_URL=sqlite:///students.db
```

✔ No hardcoding
✔ Same image works across environments

---

# 📉 Docker Best Practices Implemented

* Multi-stage Docker build
* Slim base image (`python:3.12-slim`)
* Dependency caching
* `.dockerignore` for smaller image
* Runtime configuration via env variables
* No use of `latest` tag (uses semver)

---

# 🧠 Key Concepts Implemented

* RESTful API design
* API versioning
* App factory pattern
* Blueprint architecture
* Environment-based configuration
* Database migrations
* Unit testing
* Docker containerization
* Runtime env injection

---


# 🎯 Learning Outcomes

* Backend + API development
* Docker & containerization
* Config management (12-factor)
* Debugging real-world issues
* DevOps & SRE practices

---

# 🏁 Conclusion

This project demonstrates a **production-ready, containerized backend system** with:

* Clean architecture
* Testing
* DevOps readiness
* Docker best practices

---

⭐ Star the repo if you found it useful!
