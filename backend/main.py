from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from logic import predict_days_left, get_risk_level, generate_insights

app = FastAPI()

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ExpenseInput(BaseModel):
    balance: float
    expenses: List[float]


@app.get("/")
def home():
    return {"message": "Backend Running 🚀"}


@app.post("/predict")
def predict(data: ExpenseInput):

    days = predict_days_left(data.balance, data.expenses)

    risk = get_risk_level(days)

    insights = generate_insights(data.balance, data.expenses, days)

    return {"days_left": days, "risk": risk, "insights": insights}
