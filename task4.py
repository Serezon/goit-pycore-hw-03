import datetime

users = [{
            "name": f"User {i}", 
            "birthday": (datetime.datetime.now().date() + datetime.timedelta(days=i)).strftime("%Y.%m.%d")
        } for i in range(0, 11)]

def get_upcoming_birthdays(users):
    today = datetime.datetime.now().date()
    upcoming_birthdays = []
    
    for user in users:
        birthday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date().replace(year=today.year)

        if birthday < today:
            birthday = birthday.replace(year=today.year + 1)

        if birthday.weekday() >= 5:
            birthday = birthday + datetime.timedelta(days=7 - birthday.weekday())

        if (birthday - today).days <= 7:
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": birthday.strftime("%Y.%m.%d")})
            
    return upcoming_birthdays

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
