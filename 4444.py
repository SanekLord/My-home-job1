# Годен ли в армию по возврасту
old = input("Годен ли ты в армию? Введи свой возраст: ")
if old.isdigit():
    old = int(old)
    if old <= 17:
        print("Не годен! Подрости!")
    elif 18 <= old <= 27:
        print("Годен! т.Рядовой")
    else:
        print("Не годен! Ты уже стар.")

else:
    print("Error!")

