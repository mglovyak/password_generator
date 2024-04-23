import random

symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
length = int(input("Введите длину пароля: "))
x = ""
for i in range(length):
    x+=random.choice(symbol)

print("Ваш пароль это: ",x)

