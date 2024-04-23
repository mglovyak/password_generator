from random import choice

symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Введите длину пароля: "))
x = ""
for i in range(length):
    x+=choice(symbol)

print("Ваш пароль это: ",x)
