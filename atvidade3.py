import math

while True:
  print("1. Área e perímetro do quadrado")
  print("2. Area e perímetro do Retângulo")
  print("3. Área e perímetro do circulo")
  print("4. Sair")
  escolha = int(input("Digite uma opção: "))
  if escolha == "1":
    lado = float(input("Digite aqui o lado do quadrado: "))
    area_quadrado = math.sqrt(lado)
    print(f"A área do quadrado é: {area_quadrado}")
    perimetro_quadrado = lado * 4
    print(f"O perímetro do quadrado é")
  elif escolha == "2":
    base = float(input("Digite a base do retângulo"))
    altura = float(input("Digite a altura do retângulo"))
    if math.isfinite(base) and math.isfinite(altura):
      area_retangulo = base * altura
      perimetro_retangulo= 2 * (base + altura)
      print(f"A área do retângulo é {area_retangulo}")
      print(f"O perimetro do retângulo é: {perimetro_retangulo}")
    else:
      print("os valores fornecidos são inválidos!")
  elif escolha == "3":
    raio = float(input("Digite o raio do círculo: "))
    if math.isfinite(raio) and raio > 0:
      area = math.pi * raio**2
      perimetro = 2 * math.pi *raio
      print(f"A área do circulo é {area:.2f}")
      print(f"O perimetro do circulo é: {perimetro:.2f}")
    else:
      print("O valor do raio deve ser positivo  e válido!")
  elif escolha == "4":
    print("Encerrando o programa!")
    break
  else:
    print("Digite um número válido")

