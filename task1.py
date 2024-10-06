import datetime

def get_days_from_today(date: str) -> int:
    today = datetime.datetime.now()
    try:
        parsed_date = datetime.datetime.strptime(date, "%Y-%m-%d")
    except:
        # I would prefer to raise an exception here and let the caller handle it
        # but task required to have some sort of exception handling
        # so here were are
        print("Invalid date format. Please use YYYY-MM-DD format.")
        return 0
    return (today - parsed_date).days

print(get_days_from_today("2024-01-01"))
print(get_days_from_today("2027-12-01"))
print(get_days_from_today("1-2-3"))