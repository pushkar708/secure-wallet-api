#  Secure Wallet API

A Django REST API for secure user registration, JWT-based authentication, and wallet management including top-up and maintaining transaction history.

---

##  Getting Started

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

##  Authentication Flow (JWT)

| Endpoint                  | Method | Description                          |
|---------------------------|--------|--------------------------------------|
| `/api/v1/register/`       | POST   | Register a new user, the user wallet is created along wiith the user                  |
| `/api/v1/login/`          | POST   | Login and get access + refresh token |
| `/api/v1/.auth/me/`       | GET    | Get authenticated user details       |
| `/api/v1/token/refresh/`  | POST   | Refresh access token, here the old token is expired and blacklisted, so that in case of any leaks, the token is safe                 |

>  Send access token in the header for protected routes:  
> `Authorization: Bearer <access_token>`

---

##  Wallet Management

| Endpoint                                        | Method | Description                              |
|-------------------------------------------------|--------|------------------------------------------|
| `/api/v1/wallet/balance/`                       | GET    | View wallet balance                      |
| `/api/v1/wallet/top-up/initiate/`               | POST   | Initiate a top-up transaction            |
| `/api/v1/wallet/top-up/confirm/`                | POST   | Confirm top-up within 10 minutes, else it will be marked ass expired automatically         |
| `/api/v1/wallet/transaction/?reference=<ref>`   | GET    | Get transaction by reference ID (provided at the time of initiating a top-up request)             |
| `/api/v1/wallet/transaction/all/`               | GET    | Get all transactions for the user logged in          |

>  All wallet routes require a valid **access token**.

---

##  API Documentation (Swagger/OpenAPI)

Swagger UI is available at:

```
http://localhost:8000/swagger/
```

---

##  Run Unit Tests

```bash
python manage.py test
```

Covers:
- Registration & Login
- JWT handling
- Wallet balance
- Top-up flow with expiration
- Transaction history & fetching details

---

##  Security Highlights

- JWT (Access + Refresh + Rotation)
- Rate limiting (login, registration)
- Password hashing to secure the passwords from decrypting
- Token refresh handling with token blacklisting

---

##  Technologies Used

- Django 5
- Django REST Framework
- PostgreSQL
- SimpleJWT (for authentication)
- django-ratelimit (for brute force protection)
- drf-yasg (for Swagger/OpenAPI docs)

---

## - Notes

This project is part of a backend interview assignment. It demonstrates secure authentication, user session management, and transaction-safe wallet operations with automatic transaction expiration logic.