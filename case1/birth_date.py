
from datetime import date, datetime

DIGITS = {
    '0': ["***","* *","* *","* *","***"],
    '1': ["  *"," **","  *","  *","***"],
    '2': ["***","  *","***","*  ","***"],
    '3': ["***","  *","***","  *","***"],
    '4': ["* *","* *","***","  *","  *"],
    '5': ["***","*  ","***","  *","***"],
    '6': ["***","*  ","***","* *","***"],
    '7': ["***","  *","  *","  *","  *"],
    '8': ["***","* *","***","* *","***"],
    '9': ["***","* *","***","  *","***"],
}

def day_of_week(d, m, y):
    return datetime(y, m, d).strftime("%A")

def is_leap_year(y):
    return y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)

def get_age(d, m, y):
    today = date.today()
    age = today.year - y
    if (today.month, today.day) < (m, d):
        age -= 1
    return age

def print_stars(date_str):
    lines = [""] * 5
    for char in date_str:
        if char == " ":
            for i in range(5):
                lines[i] += "   "
        else:
            for i in range(5):
                lines[i] += DIGITS[char][i] + " "
    for line in lines:
        print(line)

day = int(input("День: "))
month = int(input("Месяц: "))
year = int(input("Год: "))

print("День недели:", day_of_week(day, month, year))
print("Високосный год:", "Да" if is_leap_year(year) else "Нет")
print("Возраст:", get_age(day, month, year))

print("\nДата рождения:")
print_stars(f"{day:02d} {month:02d} {year}")
