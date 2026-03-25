# 🚀 SRE Bootcamp Repository

This repository is designed as a structured **Site Reliability Engineering (SRE) learning path** for engineers who want to build strong foundations in reliability, scalability, and production-grade systems.

It combines **theory + hands-on practice + real-world best practices** followed by modern SRE teams.

---

## 📌 Purpose

The goal of this repo is to:

* Provide a **step-by-step SRE learning roadmap**
* Help you gain **hands-on experience** with tools and systems
* Follow **industry best practices** used in real production environments
* Build a strong understanding of:

  * Reliability engineering
  * Monitoring & observability
  * Incident management
  * Infrastructure as Code (IaC)
  * Automation & scalability

---


## ⚙️ Local Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/sre-bootcamp.git
cd sre-bootcamp
```

---

### 2️⃣ Prerequisites

Make sure you have the following installed:

* Git
* Linux / WSL / macOS
* Docker
* Terraform
* AWS CLI
* Python (optional)

---

### 3️⃣ Verify Installation

```bash
git --version
docker --version
terraform --version
aws --version
```

---

### 4️⃣ Configure AWS (Optional)

```bash
aws configure
```

Provide:

* Access Key
* Secret Key
* Region
* Output format (json)

---

### 5️⃣ Run Sample Terraform Project

```bash
cd terraform/basic-setup
terraform init
terraform plan
terraform apply
```

---

### 6️⃣ Run Monitoring Stack (Optional)

```bash
cd monitoring
docker-compose up -d
```

Access:

* Prometheus → [http://localhost:9090](http://localhost:9090)
* Grafana → [http://localhost:3000](http://localhost:3000)

---

## 🛠️ Best Practices Followed

* Infrastructure as Code (IaC)
* Modular Terraform design
* Reusable scripts
* Observability-first approach
* Automation over manual work
* Production-like project structure

---

## 📈 How to Use This Repo

* Follow folders **in sequence**
* Practice each module hands-on
* Build projects from scratch
* Modify configs to experiment
* Document your learnings

---

## 🤝 Contribution

Contributions are welcome!

You can:

* Add new projects
* Improve documentation
* Fix issues
* Share best practices

---

## 📚 Recommended Approach

* Spend **70% time on hands-on**
* Focus on **real-world scenarios**
* Break things → debug → learn
* Treat this repo like a **production environment**

---

## ⭐ Final Note

This is not just a repo — it's a **practical SRE journey**.

If you complete this properly, you’ll be able to:

* Handle production systems
* Debug real incidents
* Design scalable infrastructure
* Think like an SRE engineer
