s = str(input("Введите строку>>"))
s = s.replace(" ","/")
k = str(input("Введите ключ>>"))
shifr = str(input("шифр/дешифр>>"))
finish = ''
mas = []
for i in range(len(s)):
    number = ord(s[i])
    mas.append(number)
new = ""
if len(s) > len(k):
    pr = len(s) // len(k)+1
    k = k*pr
    new = ""
    for i in range(len(mas)):
        new+=k[i]
        if mas[i] == 47:
            new += k[i]

if shifr =="шифр":
    for i in range(len(mas)):
        symbol = int(mas[i])
        if symbol >= 65 and symbol <= 90:
            if mas[i] != "/":
                temp = int(mas[i]) + int(new[i])
            else:
                finish+="/"
            if temp > 90:
                temp -=26
            finish += chr(temp)
        else:
            finish+=chr(symbol)


elif shifr == "дешифр":
    for i in range(len(mas)):
        symbol = int(mas[i])
        if symbol >= 65 and symbol <= 90:
            if mas[i] != "/":
                temp = int(mas[i]) - int(new[i])
            else:
                finish+="/"
            if temp < 65:
                temp +=26
            finish += chr(temp)
        else:
            finish += chr(symbol)
finish = finish.replace("/"," ")
print("Шифрокод:",finish)

