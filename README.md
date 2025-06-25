# 🏦 Bank API Assignemnt

**Live Demo : https://bank-api-project.onrender.com/**  

### Example Endpoints:
- `/banks` → Returns list of all banks  
- `/branches/SBIN0000001` → Fetch branch details using IFSC  
- `/branches?bank_name=STATE%20BANK%20OF%20INDIA&city=MUMBAI` → Search by bank and city

## 📅 Timeline

- **Start Date**: June 24, 2025  
- **End Date**: June 25, 2025  
- **Duration**: ~2 days  

---
## My Understanding about the Assignment

The core objective of this assignment was to build a backend API that allows users to retrieve Indian bank branch information, such as bank names, IFSC codes, and branch details, using a large combined CSV dataset. The API was expected to support search operations by IFSC code and by city & bank name.

The challenge was not just in exposing this data but handling its **size (127K+ rows)** efficiently, **normalizing the dataset**, and **deploying** the project in a secure, modular, and scalable way using cloud-based services.

---

## ⚙️ Implementation Strategy
The assignment allowed using either GraphQL or REST API to expose the bank branch dataset.I chose to implement a `RESTful API` because of `Familiarity & Speed`.

I started by loading the original dataset (`bank_branches.csv`) and splitting it into two normalized tables: `banks` and `branches`. Using SQLAlchemy models, I created a relational schema and initially tried inserting the data via Python (`import_data.py`), which was slow. I then optimized it further and eventually split the dataset into `banks.csv` and `branches.csv` to import directly into **Supabase's PostgreSQL DB** via its GUI.

The API was developed using **Flask** with routes to serve bank and branch details. I secured the credentials using a `.env` file and deployed the application using **Render**. After facing connection issues with Heroku and IPv6-related errors on Render, I successfully completed the deployment by switching to **Supabase IPv4 pooler** and updating environment variables accordingly.

---



## ✅ Features

- `GET /banks` – List of all banks  
- `GET /branches/<ifsc>` – Branch details via IFSC  
- `GET /branches?bank_name=XYZ&city=ABC` – Search branches by bank & city  
- Environment-secured credentials  
- Hosted live with Supabase DB + Render deployment  
- Optimized data handling with Python scripts

---

## 💥 Challenges Faced & Overcome

### 1. 🔒 Secret Exposure
- **Issue**: Accidentally committed `.env` file → GitGuardian alert  
- **Solution**: Regenerated credentials, properly added `.env` to `.gitignore`

### 2. 🐌 Slow Inserts (128k+ rows)
- **Issue**: `psycopg2` single-row inserts were slow (took more than ~15 minutes)  
- **Solution**: Used `executemany()` + batching log messages to monitor speed but still slow. So I split the original dataset as `banks.csv` and `branches.csv` and imported into Supabase via GUI which finished under a minute.

### 3. 🌐 Deployment Failures
- **Issue**: Heroku required payment verification  
- **Solution**: Switched to Render for deployment, Supabase for DB

### 4. ❌ Internal Server Errors
- **Issue**: Render couldn't connect to Supabase (IPv6 issue)  
- **Solution**: Updated Supabase connection string in Render environment variables (used IPv4 pooler instead)

---

## 📁 Project Structure

```bash
bank_api_project/
├── app.py                  # Main Flask application
├── models.py               # SQLAlchemy models for Bank and Branch
├── import_data.py          # Script to insert CSV data into DB
├── split_csv.py            # Helper script to split large CSV into banks.csv & branches.csv
├── test_connection.py      # Quick script to test DB connection
├── bank_branches.csv       # Original full dataset
├── banks.csv               # Extracted unique banks
├── branches.csv            # Cleaned branch data
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (ignored)
├── .gitignore              # To ignore sensitive files
├── Procfile                # For Render deployment (uses Gunicorn)
└── README.md               # This file

```
---
## 🧠 Final Thoughts

This project helped me solidify my understanding of backend development, data normalization, ORM usage, environment security, and cloud deployment. Despite challenges with speed and connectivity, I successfully built and deployed a fully working production-grade API with public endpoints that serve real-time branch data efficiently.

> *Note: Test cases have not been added to this submission as the primary focus was on building a robust and deployment-ready API, along with managing and normalizing a large dataset effectively. The codebase has been structured in a clean and modular way, making it easy to integrate tests in future iterations.*
