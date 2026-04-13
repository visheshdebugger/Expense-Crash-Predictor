def calculate_daily_average(expenses):
    valid = [x for x in expenses if x > 0]

    if len(valid) == 0:
        return 0

    return sum(valid) / len(valid)


def predict_days_left(balance, expenses):
    avg = calculate_daily_average(expenses)

    if avg == 0:
        return 999  # safer than infinity

    days = balance / avg
    return round(days, 1)


def get_risk_level(days):
    if days < 5:
        return "HIGH"
    elif days < 10:
        return "MEDIUM"
    else:
        return "LOW"


def generate_insights(balance, expenses, days_left):
    insights = []

    if len(expenses) == 0:
        insights.append("Add expense data for smarter predictions.")
        return insights

    avg = sum(expenses) / len(expenses)

    # Risk-based advice
    if days_left < 5:
        insights.append("Your money may run out soon. Your wallet looks nervous 😅")
    elif days_left < 10:
        insights.append("You’re okay for now, but don’t tempt your wallet.")
    else:
        insights.append("Nice. Your wallet is calm and collected 😎")

    # Savings advice
    suggested_cut = round(avg * 0.20, 1)

    if suggested_cut > 0:
        insights.append(f"Reducing daily spending by ₹{suggested_cut} can help.")

    # Spending trend
    if avg > balance * 0.15:
        insights.append("Your average spending is high compared to balance.")

    # Expense instability
    if max(expenses) - min(expenses) > avg:
        insights.append("Your spending pattern looks inconsistent.")

    return insights
