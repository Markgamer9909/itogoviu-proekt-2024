import time
import os
import pyautogui as p
# Создание файла в папке File
path = r'C:\Users\КреITивика\Desktop'
projectfolder = 'File'
fullpath = path + "\\" + projectfolder
# Если выдаёт ошибку, то идёт дальше
try:
    os.mkdir(fullpath)
except:
    os.chdir(fullpath)
# Переменые
i = 1
j = 3
# Диалог
a = input("Привет, меня зовут viRUS\nА как тебя?\n")
if a == "Марк" or a == "viRUS" or a == "марк":
    print("Меня тоже, ладно живи.")
else:
    print("Твоё имя мне не нравиться, наверно \n.\n.\n.\n.\n.")
    p.alert(text=":)  умри                                                               ", title="Erorr", button='OK') 
# Конечный цикл
    while i < 100:
        i += 1
        f = open("viRUS" + str(i) + ".txt", "w")
        if i == 56:
            f.write("Это код от конца этого viRUS\n09372")
    p.alert(text="                                      Найди код\n Иначе ты должен будешь задонатить мне в Brawl Stars", title="viRUS")
# Код для конца вируса
    while j > 0:
        h = p.prompt(text=f"            Введите код\nУ тебя осталось {j} попытки", title="viRUS")
        if h == "09372":
            p.alert(text="Ну блина, ты прав ладно иди", title="viRUS")
            break
        j -= 1
f.close()