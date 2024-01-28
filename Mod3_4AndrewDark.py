from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays_list = []

    for user in users:
        birthday_this_year = datetime.strptime(f"{today.year}.{user['birthday'][5:]}", "%Y.%m.%d").date()

        # наступний рік
        if birthday_this_year < today:
            birthday_this_year = datetime.strptime(f"{today.year + 1}.{user['birthday'][5:]}", "%Y.%m.%d").date()


        days_difference = (birthday_this_year - today).days

        # вихідні
        if birthday_this_year.weekday() > 4:  # субота або неділя
            # Переносимо на наступний понеділок
            birthday_this_year += timedelta(days=7 - birthday_this_year.weekday())


        if 0 <= days_difference <= 7:
            upcoming_birthdays_list.append(
                {"Ім*я": user["Ім*я"], "Будемо вітати ": birthday_this_year.strftime("%Y.%m.%d")})

    return upcoming_birthdays_list


# Тестові
users = [
    {"Ім*я": "Бронислав Шевченко", "birthday": "1985.01.23"},
    {"Ім*я": "Тарас Хмельницький", "birthday": "1990.01.29"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
