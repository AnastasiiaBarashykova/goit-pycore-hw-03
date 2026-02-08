from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        congratulation_date = birthday_this_year
        if congratulation_date.weekday() == 5:  
            congratulation_date += timedelta(days=2)
        elif congratulation_date.weekday() == 6:  
            congratulation_date += timedelta(days=1)

        delta_days = (congratulation_date - today).days

        if 0 <= delta_days <= 7:
            upcoming.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming

users = [
    {"name": "Max", "birthday": "2005.04.10"},
    {"name": "Anastasiia", "birthday": "1996.09.20"},
    {"name": "Olha", "birthday": "1970.06.17"},
    {"name": "Oleh", "birthday": "1966.01.16"},
    {"name": "Emma", "birthday": "1935.02.14"},
    {"name": "Tamara", "birthday": "1938.08.14"},
    {"name": "Borys", "birthday": "1940.02.20"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

