import time
import os
import pyautogui as p
import shutil
# Создание файла
my_file = open("DeadFile.txt", "w")
i = 1
# Диалог
a = input("Привет, меня зовут 10000011100100001100001000100000010000111010\nА как тебя?\n")
if a == "Марк" or a == "10000011100100001100001000100000010000111010" or a == "марк":
    print("Меня тоже, ладно живи.")
else:
    print("Твоё имя мне не нравиться, наверно \n.\n.\n.\n.\n.")
    p.alert(text=":)  умри                                                               ", title="Erorr", button='OK') 
    # Бесконечный цикл
    while i > 0:
        i += 1
        f = open("hello" + str(i) + ".txt", "w")
        path = r'C:\Users\user\Desktop'
        projectname = 'File'
        folders = \
        ['input' ,
        'output' ,
        'scenes' ,
        'assets']

        fullPath = os. path. join (path, projectname)
        os. mkdir(fullPath)
        shutil.copy("DeadFile.txt", "File\DeadFileA.txt")
        #shutil.copy("DeadFile.txt","DeadFile")
        time.sleep(5)
        break
f.close()
my_file.close()