# Data-Source-API-Analyst-Test

Homework assignment for the Data Source API Analyst role.

## 📌 Objective

This project demonstrates the process of accessing the GitHub REST API, authenticating using a personal access token, extracting data about repositories from a public user profile, and handling common challenges like pagination, rate limits, and error handling.

The exercise is executed via a Python notebook in Google Colab and can be reused as a base for larger API-based data ingestion pipelines.

---

## 🗂️ Repository Structure

Data-Source-API-Analyst-Test/
├── README.md
├── Content/
│ ├── api_auth.py
│ ├── data_extraction.py
│ ├── error_handling.py
│ └── pagination_and_limits.py
└── Postman_Collection/
└── google_colab_notebook.ipynb

## 🔍 Project Overview

### 🔐 API Authentication (`api_auth.py`)

- Authenticates to the GitHub API using a personal access token (PAT).
- The token is passed via the `Authorization` header as a bearer token.
- Credentials are loaded in a secure and reusable way using Python variables or external secrets (not hardcoded).

### 📦 Data Extraction (`data_extraction.py`)

- Fetches repository metadata from the following GitHub account:
  [`alura-cursos`](https://github.com/alura-cursos)

### 🚨 Error Handling (`error_handling.py`)

- Catches and logs HTTP errors (e.g., `401 Unauthorized`, `403 Forbidden`, `404 Not Found`).
- Handles invalid or expired tokens gracefully.
- Includes fallback messages and explanations for failed requests.

### ⏳ Pagination and Rate Limits (`pagination_and_limits.py`)

- Handles paginated responses from GitHub using the `per_page` and `page` parameters.
- Implements logic to detect and respect rate limits by checking response headers like `X-RateLimit-Remaining`.
- Sleeps and retries if the rate limit is exceeded.

---

## 📒 Notebook

- All code is also provided in Jupyter Notebook format (`google_colab_notebook.ipynb`) for easy execution and documentation within Google Colab.

## 🔗 Resources

- **Used GitHub Repository (Target for API Queries):**  
[`https://github.com/alura-cursos/Pandasspark/tree/main/dados`](https://github.com/alura-cursos/Pandasspark/tree/main/dados)

- **GitHub REST API Documentation (v2022-11-28):**  
[`https://docs.github.com/en/rest?apiVersion=2022-11-28`](https://docs.github.com/en/rest?apiVersion=2022-11-28)

---

## ✍️ Reflection (Part 5)

This assignment was an excellent opportunity to practice real-world API interaction using Python. It reinforced several key skills:
- Managing credentials securely
- Navigating API documentation
- Structuring paginated data responses
- Building error-resilient scripts for automation
- Presenting code in a clean and maintainable format

The most challenging part was ensuring reliability across API limits and dealing with variable responses due to repository permissions or formats.

---

## ✅ Requirements

- Python 3.8+
- Libraries:
- `requests`
- `pandas`
- `json`

All packages are available by default in Google Colab.

---

## 👨‍💻 Author

Gustavo Moraes Marrano
