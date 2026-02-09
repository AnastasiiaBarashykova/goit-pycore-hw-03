from datetime import datetime

def get_days_from_today(date="1996-09-20"):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()

        return (given_date.date() - today.date()).days

    except ValueError or TypeError or SyntaxError:
        return "Дата має бути у форматі 'YYYY-MM-DD'"

print(get_days_from_today())