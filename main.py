import random 

caracteres= "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud= int(input("de q longuitud desea la contraseña:"))

pasword=""
for i in range(longitud):
    pasword += random.choice(caracteres)
print(pasword)
