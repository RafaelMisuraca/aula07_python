import random

numero_aleatorio = random.randint(1, 10)


while True:
  user_number = int(input("Digite um número de 1 a 10: "))
  if user_number == numero_aleatorio:
    print(f"Parabens, o número aleatório era {numero_aleatorio}")
    break
  elif user_number > numero_aleatorio:
    print("O número é MENOR do que o escolhido!")
    
  else:
    print("o número é MAIOR do que o escolhido!")
    