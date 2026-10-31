# 🚨 FraudAlert

### Suspicious Transaction Monitoring System

<p align="center">
  A rule-based transaction monitoring system that identifies potentially suspicious banking activities and assigns risk levels with clear explanations.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi" />
  <img src="https://img.shields.io/badge/SQLite-Database-003B57?logo=sqlite" />
  <img src="https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-orange" />
  <img src="https://img.shields.io/badge/Status-Working-brightgreen" />
</p>

---

## 💡 Overview

**FraudAlert** is a lightweight banking transaction monitoring application designed to detect potentially suspicious financial activities using predefined rule-based detection techniques.

The system evaluates transactions based on customer profiles, transaction amounts, daily spending limits, and transaction frequency.

Each transaction is classified into one of three risk levels:

* 🟢 **LOW** – Transaction appears normal.
* 🟡 **MEDIUM** – Transaction amount is above the normal range.
* 🔴 **HIGH** – Transaction triggers one or more high-risk rules.

Unlike a system that only flags suspicious activity, FraudAlert also provides an explanation behind every risk classification, making the results easier to understand.

---

## ✨ Key Features

| Feature                    | Description                                                  |
| -------------------------- | ------------------------------------------------------------ |
| 👤 Customer Registration   | Register customers under different account categories.       |
| 🆔 Automatic Customer ID   | Generate unique customer IDs automatically.                  |
| 💳 Transaction Monitoring  | Evaluate submitted transactions in real time.                |
| ⚡ Risk Classification      | Categorize transactions into Low, Medium, and High risk.     |
| 📊 Daily Spending Analysis | Monitor cumulative transaction amounts against daily limits. |
| ⏱️ Frequency Detection     | Identify multiple transactions within a short time window.   |
| 🧠 Explainable Detection   | Display the reason behind every risk classification.         |
| 📜 Transaction History     | Store and retrieve previously evaluated transactions.        |
| 💾 Persistent Storage      | Maintain customer and transaction records using SQLite.      |

---

## ⚙️ How It Works

FraudAlert follows a simple transaction monitoring workflow:

```text
        Customer Registration
                 |
                 v
        Select Account Category
                 |
                 v
        Submit Transaction
                 |
                 v
        Fetch Customer Data
                 |
                 v
       Analyze Transaction Data
                 |
        +--------+--------+
        |        |        |
        v        v        v
      Daily   Frequency  Amount
      Limit   Analysis   Analysis
        |        |        |
        +--------+--------+
                 |
                 v
          Risk Classification
                 |
        +--------+--------+
        |        |        |
        v        v        v
       LOW    MEDIUM    HIGH
        |        |        |
        +--------+--------+
                 |
                 v
        Generate Risk Reason
                 |
                 v
        Save in SQLite Database
                 |
                 v
        Display Transaction Result
```

---

## 🧠 Risk Detection Engine

The detection engine uses predefined rules to evaluate transaction behavior.

### 1. Customer-Based Transaction Limits

Different customer categories have different base transaction amounts and daily spending limits.

| Customer Category    | Base Amount | Daily Limit |
| -------------------- | ----------: | ----------: |
| Student              |      ₹5,000 |     ₹20,000 |
| Working Professional |     ₹50,000 |   ₹2,00,000 |
| Business             |   ₹2,00,000 |   ₹8,00,000 |
| Corporate            |  ₹10,00,000 |  ₹40,00,000 |

### 2. Risk Classification Rules

| Detection Condition                              | Risk Level |
| ------------------------------------------------ | ---------- |
| Daily transaction limit exceeded                 | 🔴 HIGH    |
| 3 or more previous transactions within 5 minutes | 🔴 HIGH    |
| Transaction amount exceeds 4× base amount        | 🔴 HIGH    |
| Transaction amount exceeds 2× base amount        | 🟡 MEDIUM  |
| None of the above conditions triggered           | 🟢 LOW     |

### 3. Explainable Risk Assessment

Every transaction receives a risk level along with a corresponding explanation.

Example:

```json
{
    "risk_level": "High",
    "reason": "Daily transaction limit exceeded"
}
```

This makes the detection process more transparent and understandable.

---

## 🛠️ Tech Stack

| Technology | Purpose                                       |
| ---------- | --------------------------------------------- |
| Python     | Core programming and detection logic          |
| FastAPI    | Backend and REST API development              |
| SQLite     | Database for customer and transaction records |
| HTML       | Frontend structure                            |
| CSS        | Frontend styling                              |
| JavaScript | API integration and dynamic updates           |

---

## 🏗️ Project Structure

```text
FraudFlagger/
│
├── main.py              # FastAPI application and API endpoints
├── db.py                # Database creation and configuration
├── fraud_detection.py   # Rule-based risk detection engine
│
├── index.html           # Frontend interface
├── style.css            # Frontend styling
│
├── fraudalert.db        # SQLite database
│
└── requirements.txt     # Project dependencies
```

---

## 🚀 Getting Started

Follow these steps to run FraudAlert locally.

### Prerequisites

* Python 3.x
* pip
* Git

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
```

### 2. Navigate to the Project Directory

```bash
cd FraudFlagger
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Application

```bash
uvicorn main:app --reload
```

### 5. Access the Application

Open your browser and visit:

**Frontend:**

```text
http://127.0.0.1:8000
```

**API Documentation:**

```text
http://127.0.0.1:8000/docs
```

---

## 🔌 API Endpoints

FraudAlert provides the following REST API endpoints:

| Method | Endpoint        | Description                   |
| ------ | --------------- | ----------------------------- |
| GET    | `/`             | Load the frontend application |
| POST   | `/customer`     | Register a new customer       |
| GET    | `/customers`    | Retrieve registered customers |
| POST   | `/transaction`  | Evaluate a transaction        |
| GET    | `/transactions` | Retrieve transaction history  |

### Example: Transaction Evaluation

**Request:**

```http
POST /transaction
```

```json
{
    "customer_id": 1,
    "amount": 25000
}
```

**Response:**

```json
{
    "risk_level": "High",
    "reason": "Transaction amount is unusually high"
}
```

*The response above is an illustrative example; actual results depend on the customer's category and transaction history.*

---

## 🔮 Future Enhancements

Potential improvements to make FraudAlert more scalable and intelligent:

* [ ] Machine Learning-based fraud detection.
* [ ] Real-time transaction alerts and notifications.
* [ ] Interactive analytics dashboard.
* [ ] Transaction pattern visualization.
* [ ] Advanced anomaly detection.
* [ ] Authentication and role-based access control.
* [ ] Integration with external banking APIs.

---

## ⚠️ Disclaimer

FraudAlert is an educational prototype that demonstrates basic transaction monitoring using rule-based detection.

Its risk classifications indicate potentially suspicious activity and **do not confirm actual financial fraud**. The application is not intended for production banking or financial decision-making.

---

## 👨‍💻 Author

**Developed as an individual hackathon project.**

Built with Python, FastAPI, SQLite, HTML, CSS, and JavaScript.

---

<p align="center">
  <b>FraudAlert — Detect Suspicious. Understand Risk. Monitor Transactions.</b>
</p>
