import random

print('Welcome to number guessing!')
name = input("Qual é o seu nome? ")
choice_number = input("Digite o número do teto do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: o valor inserido não é numérico. Execute novamente e insira um número")
    raise

random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    user_answer = input("Tente adivinhar o numero:  ")

    if user_answer.isdigit():
        user_answer = int(user_answer)
    else:
        print("Erro: o valor inserido não é numérico. Por favor, coloque um numero!")
        continue

    n_choices = n_choices + 1
    if user_answer == random_number:
        print("Parabens! {} você acertou com {} tentativas!".format(name, n_choices))
        break
    elif user_answer > random_number:
        print("Errou! Tente um numero menor..")
    else:
        print("Errou! Tente um numero maior..")
