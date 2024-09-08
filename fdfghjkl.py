summa = 0
g = 0
cod = input("какие оценки")
while cod != "стоп":
    q = int(cod)
    summa = summa + q
    g= g + 1
    cod = input('')
print(summa/g) 