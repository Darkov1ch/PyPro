# Cподіваюся, що так виглядає цікавіше! Запустивши закоментовий код Ви зіграєте в лотерею!
# Функція з ДЗ знаходиться в 67 рядку
import random


# def get_number_ticket():
#     us_inp = int(input("Ласкаво просимо в Лото-забава!!! \nОберіть тип лотереї:\n"
#           "49 чисел\n36 чисел \n>>> "))
#     if us_inp == 49 or us_inp == 36:
#         if us_inp == 36:
#             print("працює")
#             us_number()
#             if us_list == pick1:
#                 print(f"Виграшні номера були {pick1} \nВи виграли мільйон грошей")
#             else:
#                 print(f"Виграшні номера були {pick1} \nВи нічого не виграли, проте ви солодка булочка!)")
#         if us_inp == 49:
#             us2_number()
#             if us_list2 ==  pick2:
#                 print("Ви виграли два мільйона грошей")
#             else:
#                 print(f"Виграшні номера були {pick2} \nВи програли, але Ви солодка булочка з маком!)")
#     else:
#         print(f"Виграшні номера були {pick2} \nВведіть в яку лотерею ви хочете зіграти")

#
# def us_number():
#     print("Введіть 6 чисел діапазон 1 - 36: ")
#     try:
#         q = int(input("Введіть перше число: "))
#         w = int(input("Введіть друге число: "))
#         e = int(input("Введіть третє число: "))
#         r = int(input("Введіть четверте число: "))
#         t = int(input("Введіть п'яте число: "))
#         y = int(input("Введіть шосте число: "))
#         global us_list, pick1
#         us_list = [q, w, e, r, t, y]
#         ran_num = range(1, 37)
#         pick1 = random.sample(ran_num,6 )
#     except ValueError:
#         print("Вводьте числа!!!")
#
#
# def us2_number():
#     print("Введіть 5 чисел діапазон 1 - 49: ")
#     try:
#         z = int(input("Введіть перше число: "))
#         x = int(input("Введіть друге число: "))
#         c = int(input("Введіть третє число: "))
#         v = int(input("Введіть четверте число: "))
#         b = int(input("Введіть п'яте число: "))
#         global us_list2, pick2
#         us_list2 = [z,x,c,v,b]
#         ran_num2 = range(1, 47)
#         pick2 = random.sample(ran_num2, 5)
#     except ValueError:
#         print("Вводьте числа!!!")
#
# get_number_ticket()





# це функція

def get_numbers_ticket(min, max, quantity):
    if min >= 1 and max <=1000 and quantity > 0 and quantity <= max: #перевірка необідних умов
        rand_num = range(min,max+1) # генерація чисел
        pik = random.sample(rand_num, quantity) # вибір бажаної кількості унікальних чисел
        pik_sorted = sorted(pik) # сортуємо
        print(pik_sorted)
        return pik_sorted
    else:
        print([])
        return []

# отримання бажаних значень від користувача
while True:

    try:
        z = int(input("Введіть мінімальне значення: "))
        x = int(input("Введіть максимальне значення: "))
        c = int(input("Введіть бажану кількість генерованих чисел: "))
        get_numbers_ticket(z,x,c)
        break
    except ValueError:
        print("Ну вводь числа!")









