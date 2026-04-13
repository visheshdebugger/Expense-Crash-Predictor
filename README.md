# 💳 WalletGuard AI

A smart full-stack personal finance web application that helps users predict how long their balance can last, detect risky spending habits, simulate savings decisions, and improve budgeting through real-time analytics.

---

## 🚀 Live Demo

Frontend: [https://expense-crash-predictor.vercel.app/]  
Backend API Docs: [https://expense-backend-anh3.onrender.com/docs]

---

## 📌 Problem It Solves

Many people track expenses only after overspending happens.

WalletGuard AI focuses on **prevention** by helping users understand:

- how many days their money may last
- whether spending pace is risky
- where unusual expense spikes happened
- how savings change future runway
- overall wallet health score

---

## ✨ Key Features

### 💸 Expense Runway Predictor
Estimates how many days your current balance may last based on recent expenses.

### 🚨 Risk Detection
Classifies financial risk as:

- Low
- Medium
- High

### 💡 Smart Insights
Provides readable spending guidance and playful financial tips.

### 🚀 What-If Savings Simulator
Example:

If you save ₹50/day, how many extra days do you gain?

### 📅 Survival Planner
Calculates safe daily budget for a target number of days.

### ⚠️ Overspending Detector
Warns if your average daily spending is above safe pace.

### 📈 Spending Spike Detector
Finds abnormal expense days compared to your average pattern.

### 💳 Wallet Score Dashboard
Gives an easy-to-understand wallet health score out of 100.

### 💾 Data Persistence
Remembers previous inputs using browser local storage.

### 📊 Interactive Charts
Visualizes expense patterns using charts.

---

## 🛠 Tech Stack

### Frontend
- HTML
- CSS
- JavaScript
- Chart.js

### Backend
- Python
- FastAPI
- Uvicorn

### Deployment
- Frontend: Vercel
- Backend: Render

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

```bash
project/
│── backend/
│   ├── main.py
│   ├── logic.py
│   └── requirements.txt
│
│── frontend/
│   └── index.html
