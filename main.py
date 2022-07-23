import random
import numpy as np

simb = np.array(["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                 "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                 "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])

s_simb = np.array(["!", "@", "№", "#", "$", "%", "^",
                   "&", "*", "_", "-", "=", "+", "-", "/", "|"])


leng = int(input("Введите кол-во знаков в пароле: "))
col = int(input("Введите кол-во паролей: "))
sp = input("Использовать специальные символы?: ")
name = input("введите название файла: ")

true = ["y", "1", "true", "True", " "]

if sp in true:
    us_alph = np.append(simb, s_simb)


else:
    us_alph = simb

lst = ""
password = ""

for i in range(col):
    
    password = ""
    for j in range(leng):
        password += us_alph[random.randint(0, len(us_alph)-1)]
    lst += password + "\n"
        
file = open(name+".txt", "w")
file.write(lst)