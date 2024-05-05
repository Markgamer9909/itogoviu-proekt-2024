import time
import pyautogui as p
# Создание файла для атаки
my_file = open("DeadFile.txt", "w")
i = 1
# Диалог
a = input("Привет, меня зовут 10000011100100001100001000100000010000111010\nА как тебя?\n")
if a == "Марк" or a == "10000011100100001100001000100000010000111010":
    print("Меня тоже, ладно живи.")
else:
    print("Твоё имя мне не нравиться, наверно \n...\n...\n...\n...\n...")
    p.alert(text=":)  умри                                                               ", title="Ошибка", button='OK') 
    # Бесконечный цикл для атаки
    while i > 0:
        i += 1
        f = open("hello" + str(i) + ".txt", "w")
        break
f.close()
my_file.close()