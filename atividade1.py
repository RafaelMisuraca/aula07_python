import operacoes
while True:
  print("1. Soma")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")
  escolha= input("Digite uma opção: ")
  numero1 = int(input("Digite o primeiro número: "))
  numero2 = int(input("Digite o segundo número: "))

  if escolha == "1":
    soma = operacoes.somarNumeros(numero1, numero2)
    print(soma)
    
  elif escolha == "2":
    subtracao = operacoes.subtrairNumeros(numero1, numero2)
    print(subtracao)
  elif escolha == "3":
    multiplicacao = operacoes.multiplicarNumeros(numero1, numero2)
    print(multiplicacao)
  elif escolha == "4":
    divisao = operacoes.dividirNumeros(numero1, numero2)
    print(divisao)
  else:
    print("Opção inválida, tente novamente.")
