# FraudAlert 🚨
### Suspicious Transaction Monitoring System

FraudAlert is a rule-based banking transaction monitoring system designed to identify potentially suspicious transactions. It analyzes transaction amounts, customer profiles, daily spending limits, and transaction frequency to assign risk levels with clear explanations.

## Features

- Customer Registration
- Automatic Customer ID Generation
- Transaction Monitoring
- Low, Medium and High Risk Classification
- Daily Transaction Limit Detection
- Frequent Transaction Detection
- Risk Explanation
- Transaction History

## How It Works

1. Register customers by entering their name and category.
2. The system assigns a predefined base amount and daily limit.
3. When a transaction is submitted, the system checks its amount, daily spending and recent transaction frequency.
4. It assigns a risk level with a reason and stores the transaction in SQLite.

## Risk Detection Logic

| Condition | Risk |
|---|---|
| Daily transaction limit exceeded | High |
| 3 or more previous transactions within 5 minutes | High |
| Amount exceeds 4x base amount | High |
| Amount exceeds 2x base amount | Medium |
| Normal transaction | Low |

## Tech Stack

- Python
- FastAPI
- SQLite
- HTML
- CSS
- JavaScript

## Project Structure

    FraudFlagger/
    │
    ├── main.py
    ├── db.py
    ├── fraud_detection.py
    ├── index.html
    ├── style.css
    ├── fraudalert.db
    └── requirements.txt

## Installation

### 1. Clone Repository

    git clone <your-repository-url>

### 2. Navigate to Project

    cd FraudFlagger

### 3. Install Dependencies

    pip install -r requirements.txt

### 4. Run Application

    uvicorn main:app --reload

### 5. Open in Browser

    http://127.0.0.1:8000

## API Documentation

FastAPI Swagger documentation:

    http://127.0.0.1:8000/docs

## Note

FraudAlert uses rule-based detection to identify potentially suspicious activities. Risk levels are indicators and do not confirm actual fraud.