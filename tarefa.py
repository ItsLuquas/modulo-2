#-----PRIMEIROS PASSOS-----

# Tarefa 1
print("Ola, Mundo!")

# Tarefa 2
nome = "Lucas"
idade = 18
cidade = "Uberlândia"

print(nome, idade, cidade)

# Tarefa 3
nome = input()

print(f"Ola, {nome}")

# Tarefa 4
idade = input()

print(f"Você tem {idade} anos")

# Tarefa 5
a = int(input())
b = int(input())

c = a + b

print(c)

# Tarefa 6
a = int(input())
b = int(input())

soma = a + b
sub = a - b
mult = a * b
div = a / b

print(soma, sub, mult, div)

# Tarefa 7
a = int(input())

resultado = a * 2

print(resultado)

# Tarefa 8
a = int(input())

mult = a * 3
div = a / 2

print(mult, div)

# Tarefa 9
nome = input()
sobrenome1 = input()
sobrenome2 = input()

print(nome, sobrenome1, sobrenome2)

# Tarefa 10
ano = int(input())

result = 2026 - ano

print(f"Você tem {result} anos")

# Tarefa 11
metro = int(input())

cm = metro * 100
mm = metro * 1000

print(f"{metro}m, {cm}cm, {mm}mm") 

# Tarefa 12
mnt = int(input())

seg = mnt * 60

print(f"{mnt} minutos, {seg} segundos")

# Tarefa 13
hr = int(input())

mnt = hr * 60

print(f"{hr} horas, {mnt} minutos")

# Tarefa 14
C = int(input())
F = C * 9 / 5 + 32

print(f"{C}°Celsius, {F}°Fahrenheit")

# Tarefa 15
reais = float(input())
cotacao = 5.00
dolar = reais / cotacao

print(f"Com R${reais}, você consegue comprar U${dolar}")

#-----OPERADORES E CALCULOS-----
# Tarefa 16
lado = float(input())
area = lado**2

print(f"a área do quadrado é {area}")

# Tarefa 17
larg = float(input())
alt = float(input())
area = larg * alt

print(f"a área do retângulo é {area}")

# Tarefa 18
base = float(input())
alt = float(input())
area = (base * alt) / 2

print(f"a área do triangulo é {area}")

# Tarefa 19
raio = float(input())
area = (raio ** 2) * 3.14

print(f"A área do círculo é {area}")

# Tarefa 20
larg = float(input())
alt = float(input())

perim = 2 * (larg + alt)

print(f"O perímetro do retângulo é: {perim}")

# Tarefa 21
nota1 = float(input())
nota2 = float(input())
nota3 = float(input())

media = (nota1 + nota2 + nota3) / 3

print(f"Média: {media:.2f}")

# Tarefa 22
hora = float(input(""))
mes = float(input(""))
bruto = hora * mes

print(f"O salário bruto é R$ {bruto:.2f}")

# Tarefa 23
original = float(input())

aumento = original * 0.10
novosalario = original + aumento

print(f"Salário original: R$ {original:.2f}")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novosalario:.2f}")

# Tarefa 24
original = float(input(""))
desconto = original * 0.15
final = original - desconto

print(f"Valor do desconto: R$ {desconto:.2f}")
print(f"Preço final: R$ {final:.2f}")

# Tarefa 25
total = float(input())
parcelas = int(input())
valor_parcela = total / parcelas

print(f"O valor de cada parcela é: R$ {valor_parcela:.2f}")

# Tarefa 26
peso = float(input())
altura = float(input())
imc = peso / (altura ** 2)
print(f"{imc:.2f}")

# Tarefa 27
nota1 = float(input())
nota2 = float(input())
media = (nota1 * 2 + nota2 * 3) / 5
print(f"{media:.2f}")

# Tarefa 28
num1 = int(input())
num2 = int(input())
quociente = num1 // num2
resto = num1 % num2
print(quociente)
print(resto)

# Tarefa 29
num = int(input())
print(num - 1)
print(num + 1)

# Tarefa 30
base = float(input())
expoente = float(input())
resultado = base ** expoente
print(resultado)

#-----Condicionais (if, elif e else)-----

# Tarefa 31
num1 = float(input("Digite um número:"))

if num1 > 0:
    print(f"O número é positivo")

elif num1 < 0:
    print(f"O número é negativo")

else:
    print(f"O número é 0")

# Tarefa 32
idade = int(input("Digite sua idade:"))
if idade >= 18:
  print(f'Você é maior de idade')
else:
  print(f'Você é menor de idade')

# Tarefa 33
num = int(input('Digite um número:'))

if num % 2 == 0:
  print(f'O número é par')
else:
  print(f'O número é ímpar')

# Tarefa 34
num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))

if num1 > num2:
  print(f'O maior número é {num1}')
elif num2 > num1:
  print(f'O maior número é {num2}')
else:
  print(f'Os números são iguais')


# Tarefa 35
num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))
num3 = float(input('Digite outro número:'))

maior = num1

if num2 > maior:
  maior = num2

if num3 > maior:
  maior = num3

print(f'O maior número é o {maior}')
num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))
num3 = float(input('Digite outro número:'))

maior = num1

if num2 > maior:
  maior = num2

if num3 > maior:
  maior = num3

print(f'O maior número é o {maior}')

# Tarefa 36
num1 = float(input('Digite um número:'))
num2 = float(input('Digite outro número:'))
num3 = float(input('Digite outro número:'))

menor= num1

if num2 < menor:
  menor= num2

if num3 < menor:
  menor = num3

print(f'O maior número é o {menor}')

# Tarefa 37
media = float(input('Média do aluno:'))

if media >= 6:
  print(f'Aluno aprovado')
elif media < 6:
  print(f'Aluno reprovado')

# Tarefa 38
media = float(input('Média do aluno:'))

if media >= 7:
  print(f'Aluno aprovado')
elif media >= 5:
  print(f'Aluno em recuperação')
elif media < 5:
  print(f'Aluno reprovado')

# Tarefa 39
idade = int(input('Sua idade: '))

if idade >= 118:
    print('Caixão e vela preta')
elif idade >= 60:
    print('Idoso')
elif idade >= 18:
    print('Adulto')
elif idade >= 12:
    print('Adolescente')
elif idade >= 0:
    print('Criança')
else:
    print('Idade inválida')

# Tarefa 40
senha = 12345 
tentativa = int(input('Digite sua senha:'))

if tentativa == senha:
  print(f'Acesso permitido')
else:
  print(f'Acesso negado')

# Tarefa 41
usuario = "Lucas"
senha = 12345

useracess = input('Digite o usuário:')
password = int(input('Digite a senha'))

if useracess == usuario and password == senha:
  print(f'Acesso permitido')
else:
  print(f'Acesso negado')

# Tarefa 42
num = int(input('Digite um número:'))

if num % 5 == 0:
  print(f'O número é múltiplo por 5')
else:
  print(f'O número não é múltiplo por 5')

# Tarefa 43
num = int(input('Digite um número:'))

if num % 3 == 0 and num % 5 == 0 :
  print(f'O número é divisível por 3 e 5 simultaneamente')
else:
  print(f'O número não cumpre os requisitos')

# Tarefa 44
num = int(input('Digite um número:'))

if num % 4 == 0:
  print(f'O ano é bissexto')
else:
  print(f'O ano não é bissexto')

# Tarefa 45
valor_compra = float(input("Digite o valor da compra (R$): "))

if valor_compra >= 200.0:
    valor_final = valor_compra * 0.90
    print(f"Desconto de 10% aplicado! Valor final: R$ {valor_final:.2f}")
else:
    print(f"Valor original mantido. Valor final: R$ {valor_compra:.2f}")

# Tarefa 46
valor_compra = float(input('Digite o valor da compra (R$):'))

if valor_compra >= 150.0:
  print(f'R$:{valor_compra}, frete grátis.')
else:
  valor_compra = valor_compra + 20
  print(f'R$:{valor_compra}, R$:20,00 de frete')

# Tarefa 47
num1 = float(input('Digite o primeiro número:'))
num2 = float(input('Digite o segundo número:'))
operacao = input('Digite o sinal (+, -, x, /):')

if operacao == '+':
  resultado = num1 + num2
  print(f'Resultado: {num1} + {num2} = {resultado}')

elif operacao == '-':
  resultado = num1 - num2
  print(f'Resultado: {num1} - {num2} = {resultado}')

elif operacao == 'x':
  resultado = num1 * num2
  print(f'Resultado: {num1} x {num2} = {resultado}')

elif operacao == '/':
  resultado = num1 / num2
  print(f'Resultado: {num1} / {num2} = {resultado}')

# Tarefa 48
lado1 = float(input('Digite o primeiro número:'))
lado2 = float(input('Digite o segundo número:'))
lado3 = float(input('Digite o terceiro número:'))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
  print(f'Os lados podem formar um triângulo')

else:
  print(f'Os lados não podem formar um triângulo')

# Tarefa 49
lado1 = float(input('Digite o primeiro número:'))
lado2 = float(input('Digite o segundo número:'))
lado3 = float(input('Digite o terceiro número:'))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
  print(f'Os lados podem formar um triângulo')
  if lado1 == lado2 == lado3:
    print(f'O triângulo é equilátero')
  elif lado1 != lado2 and lado2 != lado3 and lado1!= lado3:
    print(f'O triângulo é escaleno')
  else:
    print(f'O triângulo é isósceles')


else:
  print(f'Os lados não podem formar um triângulo')

# Tarefa 50
salario = float(input('Digite seu salário:'))

if salario <= 2000.0:
  imposto = 0.0
elif salario <= 4000.0:
  imposto = salario * 0.10
else:
  imposto = salario * 0.20

resto = salario - imposto

print(f"Valor do imposto: R$ {imposto:.2f}")
print(f"Salário restante: R$ {resto:.2f}")

#-----Repetição: while e for-----

# Tarefa 51
for numeros in range (1,11):
  print(numeros)

# Tarefa 52
for numeros in range (10, -1, -1):
  print(numeros)
print('Fim!')

# Tarefa 53
for pares in range (0, 101, 2):
  print(pares)

# Tarefa 54
for impares in range (1, 101, 2):
  print(impares)

# Tarefa 55
num = int(input('Digite seu número:'))
for i in range(1, 11):
  resultado = num * i
  print (f'{num} x {i} = {resultado}')

# Tarefa 56
num = int(input('Digite seu número:'))
soma = 0
for i in range(1, num + 1):
  soma += i
print(f'A soma de 1 até {num} é: {soma}')

# Tarefa 57
num = int(input('Digite seu número:'))
fatorial = 1
for i in range(1, num + 1):
  fatorial *= i
print(f'{fatorial}')

# Tarefa 58
pares = 0
for i in range(1, 11):
  num = int(input('Digite seu número:  '))
  if num % 2 == 0:
    pares += 1
print(f'Entre esses números, existem {pares} números pares')

# Tarefa 59
positivos = 0
for i in range(1, 11):
  num = float(input('Digite seu número:  '))
  if num > 0:
    positivos += num
print(f'A soma dos números positivos é: {positivos}')

# Tarefa 60
maior = 0
for i in range(5):
  num = float(input('Digite seu número:  '))
  if i == 0 or num > maior:
    maior = num
print(f'O maior número digitado foi: {maior}')

# Tarefa 61
menor = 0
for i in range(5):
  num = float(input('Digite seu número:  '))
  if i == 0 or num < menor:
    menor = num
print(f'O menor número digitado foi: {menor}')

# Tarefa 62
soma = 0
for i in range(5):
  nota = float(input('Digite a nota:'))
  soma += nota
media = soma / 5
print(f'A média final acumulada das 5 notas é {media:.1f}.')

# Tarefa 63
certa = '12345'
tentativa = input('Digite sua senha:')
while tentativa != certa:
  print(f'Senha incorreta')
  tentativa = int(input('Digite sua senha:'))
print(f'Senha correta')

# Tarefa 64
num = int(input('Digite um número: '))
while num <= 0:
  print(f'O número deve ser maior que zero!')
  num = float(input('Digite novamente: '))
print(f'Sucesso! O número {num:.2f} é maior que zero.')

# Tarefa 65
menu = int(input('Digite seu número: '))
while menu != 0:
  match menu:
    case 1: print('Olá')
    case 2 print('Mostrar uma mensagem')
  menu = int(input(''))
print('Sessão encerrada')

# Tarefa 66
soma = 0
num = -1
while num != 0:
  num = int(input('Digite um número (0 para parar): '))
  if num == 0:
    break
  soma += num
print(f'A soma final é {soma}')

# Tarefa 67
soma = 0
quantidade = 0
while True:
  nota = float(input(f'Digite a nota (-1 para sair): '))
  if nota == -1:
    break
  soma = soma + nota
  quantidade += 1
if quantidade > 0:
  media = soma / quantidade
  print(f'Quantidade de notas válidas: {quantidade} | Média final: {media:.2f}')
else:
  print(f'Nenhuma nota válida foi digitada')

# Tarefa 68
real = 88
palpite = -1
while palpite != real:
  palpite = int(input('Digite o código secreto: '))
  if palpite > real:
    print(f'O número é menor')
  elif palpite < real:
    print(f'O número é maior')
print(f'Você acertou!')

# Tarefa 69
num = int(input('Digite um número inteiro maior que 1: '))
while num <= 1:
    print('O número deve ser maior que 1!')
    num = int(input('Digite novamente: '))
divisores = 0
for i in range(1, num + 1):
    if num % i == 0:
        divisores += 1
if divisores == 2:
    print(f'O número {num} é primo!')
else:
    print(f'O número {num} não é primo.')
    
#-----Strings-----

# Tarefa 70  (Peguei da Nicole pq nao consegui entender)
inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))
print("Números primos entre" ,inicio ,"e" ,fim)
for num in range(inicio, fim + 1):
    if num > 1:
        divisores = 0
        for i in range(1, num + 1):
            if num % i == 0:
                divisores += 1
        if divisores == 2:
            print(num, end=" ")
print()

# Tarefa 71
a1 = input("Diga algo: ")
print("Sua palavra ou frase tem", len(a1), "caracteres.")

# Tarefa 72
a1 = input("Diga algo para maiúsculas e minúsculas: ")
print(a1.upper())
print(a1.lower())

# Tarefa 73
a1 = input("Insira uma palavra: ")
print(a1[0])
print(a1[len(a1) - 1])

# Tarefa 74
a1 = input("Insira uma frase: ")
a2 = a1.lower()
print("Existem", a2.count("a"), "letras 'a' nesta frase.")

# Tarefa 75
a1 = input("Insira uma palavra: ")
a2 = a1.lower()
a3 = a2[::-1]

if a2 == a3:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")

# Tarefa 76
a1 = input(
    "Insira uma frase para ser dividida e invertida na ordem oposta: "
)
a2 = a1.split()
for i in range(len(a2) - 1, -1, -1):
    print(a2[i])

# Tarefa 77
a1 = input("Insira uma frase: ")
a2 = a1.split()
for a3 in a2:
    print(a3)

# Tarefa 78
a1 = input("Digite uma frase:")
a2 = len(a1.split())
print(a2)

# Tarefa 79
a1 = input("Digite sua frase: ")
a2 = input("Digite a palavra que você deseja substituir: ")
a3 = input("Digite a palavra que você quer colocar no lugar: ")
print(a1.replace(a2, a3))

# Tarefa 80
a1 = input("Digite seu e-mail: ")
if "@" in a1 and "." in a1.split("@")[-1]:
    print("E-mail válido.")
else:
    print("E-mail inválido.")


#-----Listras, tuplas, dicionarios e conjuntos-----

# Tarefa 81
a1 = ["Finn", "Jake", "BMO", "e", "Marceline"]
for a2 in a1:
    print(a2)

# Tarefa 82
for i in range(5):
    a2 = input("Digite um nome: ")
    a1.append(a2)
    print(a1)

# Tarefa 83
a1 = 0
a2 = [1, 2, 3, 4, 10, 5, 6]
for i in range(len(a2)):
    a1 = a1 + a2[i]
print(a1)

# Tarefa 84
a1 = [-1, -2, -3, 67, -5]
a2 = a1[0]
for a3 in a1:
    if a3 > a2:
        a2 = a3
print(a2)

# Tarefa 85
a1 = [-1, -2, -3, 67, -5]
a2 = a1[0]
for a3 in a1:
    if a3 < a2:
        a2 = a3
print(a2)

# Tarefa 86
a1 = []

for i in range(5):
    a2 = int(input("Digite a nota: "))
    a1.append(a2)

a3 = sum(a1) / len(a1)
print("A média é:", a3)

# Tarefa 87
a1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

a2 = []

for a3 in a1:
    if (a3 % 2 == 0):
        a2.append(a3)

print(a2)

print(a3)

# Tarefa 88
a1 = ["Lucas", "Davi", "Bruno", "Gustavo", "César"]

a2 = input("Digite um nome para remover: ")

if (a2 in a1):

    a1.remove(a2)
    print("Lista atualizada: " ,a1)

else:

    print("Tal nome não está na lista.")

# Tarefa 89
a1 = []
for i in range(5):
    a2 = input("Digite um item: ")
    a1.append(a2)
a3 = input("Pesquise um item: ")
if (a3 in a1):
    print("Item registrado.")
else:
    print("Item não encontrado.")

# Tarefa 90
a1 = []
for i in range(6):
    numero = int(input("Insira um número: "))
    a1.append(numero)
a1.sort()
print("Ordem crescente", a1)
a1.sort(reverse=True)
print("Ordem decrescente:", a1)

# Tarefa 91
a1 = []
for i in range(10):
    a2 = int(input("Insira um número: "))
    a1.append(a2)
a3 = set(a1)
print(a3)

# Tarefa 92
a1 = {1, 2, 3, 10, 13, 33, 44, 67}
a2 = {3, 5, 6, 7, 12, 13, 54, 67}
a3 = a1 & a2
print(sorted(a3))

# Tarefa 93
a1 = (20 , 80)
print("X's valores iguais: ", a1[0])
print("Y's valores iguais: ", a1[1])

# Tarefa 94
a1 = {
    "Nome": "Lucas",
    "Idade": 18,
    "Cidade": "Uberlândia, MG"
}

print("Meu nome é ", a1["Nome"], ", eu moro em ", a1["Cidade"], " e tenho ", a1["Idade"], " anos.")

# Tarefa 95
a1 = []
a2 = input("Digite seu nome: ")
for i in range(2):
    a3 = int(input("Digite sua nota: "))
    a1.append(a3)
a2 = {
    "Nome": a2,
    "Notas": a1
}
a2["Média"] = (a1[0] + a1[1]) / 2
print(a2)

# Tarefa 96
a1 = []
a2 = {
    "Nome": "PS5", "Preço": "4.600",
}
a1.append(a2)
a3 = {
    "Nome": "GTA6 standart", "Preço": "449.90",
}
a1.append(a3)
a4 = {
    "Nome": "Outro Negócio", "Preço": "549.90",
}
a1.append(a4)
print(a1)

# Tarefa 97
a1 = 0
a2 = [
    {"Nome": "Switch 2", "Preço": 4.000},
    {"Nome": "Ocarina of Time remake", "Preço": 329.90},
    {"Nome": "Ocarina oficial", "Preço": 270.00},
]
for i in a2:
    if i["Preço"] > a1:
        a1 = i["Preço"]
print(a1)

# Tarefa 98
a1 = [
    {"Lucas": 34991292027},
    {"Bruno": 3491000109},
    {"Mateus": 3484107682}
]
a2 = input("De quem você quer o número?: ")
have = False
for i in a1:
    if a2 in i:
        print(i[a2])
        have = True
        break
    else:
        have = False
if (have == False):
    print("O sistema não possui esse número.")

# Tarefa 99


# Tarefa 100

#-----Funções-----

# Tarefa 101


# Tarefa 102


# Tarefa 103


# Tarefa 104


# Tarefa 105


# Tarefa 106


# Tarefa 107


# Tarefa 108


# Tarefa 109


# Tarefa 110


# Tarefa 111


# Tarefa 112


# Tarefa 113


# Tarefa 114


# Tarefa 115

#-----Arquivos, excecoes e organização-----

# Tarefa 116


# Tarefa 117


# Tarefa 118


# Tarefa 119


# Tarefa 120


# Tarefa 121


# Tarefa 122


# Tarefa 123


# Tarefa 124


# Tarefa 125


# Tarefa 126


# Tarefa 127


# Tarefa 128


# Tarefa 129


# Tarefa 130


# Tarefa 131


# Tarefa 132


# Tarefa 133


# Tarefa 134


# Tarefa 135


───────────────────────────────
───────────────████─███────────
──────────────██▒▒▒█▒▒▒█───────
─────────────██▒────────█──────
─────────██████──██─██──█──────
────────██████───██─██──█──────
────────██▒▒▒█──────────███────
────────██▒▒▒▒▒▒───▒──██████───
───────██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒███─
──────██▒▒▒▒─────▒▒▒▒▒▒▒▒▒▒▒▒█─
──────██▒▒▒───────▒▒▒▒▒▒▒█▒█▒██
───────██▒▒───────▒▒▒▒▒▒▒▒▒▒▒▒█
────────██▒▒─────█▒▒▒▒▒▒▒▒▒▒▒▒█
────────███▒▒───██▒▒▒▒▒▒▒▒▒▒▒▒█
─────────███▒▒───█▒▒▒▒▒▒▒▒▒▒▒█─
────────██▀█▒▒────█▒▒▒▒▒▒▒▒██──
──────██▀██▒▒▒────█████████────
────██▀███▒▒▒▒────█▒▒██────────
█████████▒▒▒▒▒█───██──██───────
█▒▒▒▒▒▒█▒▒▒▒▒█────████▒▒█──────
█▒▒▒▒▒▒█▒▒▒▒▒▒█───███▒▒▒█──────
█▒▒▒▒▒▒█▒▒▒▒▒█────█▒▒▒▒▒█──────
██▒▒▒▒▒█▒▒▒▒▒▒█───█▒▒▒███──────
─██▒▒▒▒███████───██████────────
──██▒▒▒▒▒██─────██─────────────
───██▒▒▒██─────██──────────────
────█████─────███──────────────
────█████▄───█████▄────────────
──▄█▓▓▓▓▓█▄─█▓▓▓▓▓█▄───────────
──█▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓█──────────
──█▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓█──────────
──▀████████▀▀███████▀──────────

