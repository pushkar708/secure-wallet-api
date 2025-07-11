# 🔐 Secure Wallet API

A secure Django REST API for user registration, JWT-based authentication, and wallet management including top-up and transaction tracking.


## 🚀 Getting Started

### Clone the Project

```bash
git clone https://github.com/pushkar708/secure-wallet-api.git
cd secure-wallet-api
```

### Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create `.env` File

```
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASS=your_db_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_django_secret_key
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Server

```bash
python manage.py runserver
```

---

## 🔑 Authentication Flow (JWT)

| Endpoint                  | Method | Description                          |
|---------------------------|--------|--------------------------------------|
| `/api/v1/register/`       | POST   | Register a new user                  |
| `/api/v1/login/`          | POST   | Login and get access + refresh token |
| `/api/v1/.auth/me/`       | GET    | Get authenticated user details       |
| `/api/v1/token/refresh/`  | POST   | Refresh access token                 |

> 💡 Send access token in the header for protected routes:  
> `Authorization: Bearer <access_token>`

---

## 💰 Wallet Management

| Endpoint                                     | Method | Description                              |
|----------------------------------------------|--------|------------------------------------------|
| `/api/v1/wallet/`                            | GET    | View wallet balance                      |
| `/api/v1/wallet/top-up/`                     | POST   | Request to top-up balance                |
| `/api/v1/wallet/top-up/confirm/`             | POST   | Confirm top-up payment before update     |
| `/api/v1/wallet/transaction/<reference>/`    | GET    | Get transaction details by reference     |

> ⚠️ All wallet routes require a valid **access token**.

---

## 📘 API Documentation (Swagger/OpenAPI)

Swagger UI is available at:

```
http://localhost:8000/swagger/
```


## 🧪 Run Unit Tests

```bash
python manage.py test
```

Covers:
- Registration & Login
- JWT handling
- Wallet balance
- Top-up logic
- Transaction integrity

---

## 🔐 Security Highlights

- JWT (Access + Refresh)
- Rate limiting (login, registration)
- Password hashing
- Safe financial transactions (`@atomic`)
- Token blacklisting & rotation (optional)

---

## 📦 Technologies Used

- Django 5
- Django REST Framework
- PostgreSQL
- SimpleJWT (for authentication)
- django-ratelimit (for brute force protection)
- drf-yasg (for Swagger/OpenAPI docs)