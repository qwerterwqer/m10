import random
words =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
len_password = int(input("ведите длину пароля"))
password = ""
for i in range(len_password):
    word = random.choice(words)
    password = password + word
    print("ваш пароль: ", password)

    