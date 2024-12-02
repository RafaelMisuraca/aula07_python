#Continuação da atividade1
def somarNumeros(num1, num2):
  return f"A soma é : {num1 + num2}"

def subtrairNumeros(num1, num2):
  return f"A subtração é : {num1 - num2}"

def multiplicarNumeros(num1, num2):
  return f"A multiplicação é: {num1 * num2}"

def dividirNumeros(num1, num2):
  if num2 == 0:
    return "A divisão por zero não é definida!"
  else:
    return f"A divisão é: {num1 / num2}"