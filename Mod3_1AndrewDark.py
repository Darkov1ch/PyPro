import datetime as ty


zara = ty.datetime.now()
t = ""
def get_days_from_today_date(t):
    Data = input("Введіть дату у форматі РРРР/ММ/ДД >>> ")
    try:
        correct_data = ty.datetime.strptime(Data, "%Y/%m/%d")
        if correct_data > zara:
            future = correct_data - zara
            fd = future.days
            print("Ця дата настане через", {fd}, "дні")
        elif correct_data < zara:
            pas = correct_data - zara
            pd = pas.days
            print("Ця дата була", {pd}, "днів тому назад")
        else:
            print("Не потрібно вводити одинакові дати") # це був зайвий рядок)

    except ValueError:
        print("Формат бачиш?)")
        get_days_from_today_date(t)





get_days_from_today_date(t)




