from datetime import date

def get_days_from_today(start_date=date(1996, 9, 20)):
    today = date.today()
    return (start_date-today).days

print(get_days_from_today())
