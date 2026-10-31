def get_base_amount(category):

    amounts = {
        "Student": 5000,
        "Working Professional": 50000,
        "Business": 200000,
        "Corporate": 1000000
    }

    return amounts[category]


def get_daily_limit(category):

    limits = {
        "Student": 20000,
        "Working Professional": 200000,
        "Business": 800000,
        "Corporate": 4000000
    }

    return limits[category]


def detect_fraud(amount, base, daily_total, daily_limit, count):

    if daily_total + amount > daily_limit:
        return "High"

    elif count >= 3:
        return "High"

    elif amount > base * 4:
        return "High"

    elif amount > base * 2:
        return "Medium"

    else:
        return "Low"