#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

#Laco for que percorre a lista aleatoriamente designando as letras
for let in range(nr_letters):
    let = random.randint(0,51)
    password += letters[let]

#Laco for que percorre a lista aleatoriamente designando os simbolos
for sym in range(nr_symbols):
    sym = random.randint(0,8)
    password += symbols[sym]

#Laco for que percorre a lista aleatoriamente designando os numeros
for numb in range(nr_numbers):
    numb = random.randint(0,9)
    password += numbers[numb]    


#transforma a senha em uma lista e joga os valores na variavel ls
ls = list(password)

#usa a funcao shuffle (embaralha) da biblioteca random *só pode ser usada em uma lista
random.shuffle(ls)

#usa a funcao join (retorna uma string resultada da junção de uma lista, string, 
# ou tuple com o outro argumento sendo o separador) com o '', ou seja, transformou em string.
password = ''.join(ls)

print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P