# Laços de repetição e listas
# Maneiras de executar o mesmo comando várias vezes
# range (gera listas no python)

for palavra in range(1,4):
  print('Carregando')


# for item in coleção:
  #expressão

  # Laços de repetição em listas

for item in range(1,21):
  print(item)
for item in range (1,35,4):
  print(item)

# Laços de repetição em nomes

nomes = ['Heloísa', 'Jailza', 'Emilly']
for nome in nomes:
  print(nome)

ingredientes = ['Farinha','Fermento','Ovos','Açúcar','Leite','Manteiga']
for ingrediente in ingredientes:
  print(ingrediente)

# Imprimir valores de 1 a N

valor_maximo = int(input('Digite o valor máximo: '))
valor_inicial = 1
for numero in range(valor_inicial,valor_maximo+1):
  print(numero)

# Coleções (listas)
precos = [356,476,234,987,125]
#          0   1   2   3   4   = número do índice
print(precos[1])

precos = [14,29,384,987,653,34,870]
for preco in precos:
  print(preco)

# Soma das idades
idades = [17,3,33,55,41]
total = 0
for idade in idades:
  total = total + idade
print(total)

