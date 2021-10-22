

# encontrando o fatorial de um número
numero = int(input(' Digite um número: '))
if numero > 0:
  fatorial = 1
  for item in range(1, numero +1):
    fatorial = fatorial * item
  print(fatorial)

  # chute um número
  # gerar um número aleatório de 1 a 10
  # comparara o chute do usuário com o valor aleatório gerado
  # import random = chamar uma biblioteca no python
  # While (enquanto)

import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
 chute = int(input(' Chute um valor de 1 a 10: '))
 if chute > valor_aleatorio:
  print('Chute maior que o valor gerado!')
 elif chute < valor_aleatorio:
  print(' Chute menor que o valor gerado ')
 elif chute == valor_aleatorio:
   acertou = True
   print(' Parabéns! Você acertou. ')
 


# Limite de velocidade permitido
velocidade_atual = int(input('Qual a sua velocidade ao transitar a rua? '))
velocidade_maxima = 80
if velocidade_atual >= velocidade_maxima and velocidade_atual <= velocidade_maxima + 10:
  print(' Você levou uma multa leve! ')
elif velocidade_atual >= velocidade_maxima + 11 and velocidade_atual <= velocidade_maxima + 20:
  print(' Você levou uma multa grave! ')
elif velocidade_atual > velocidade_maxima + 20:
  print(' Você levou uma multa gravíssima! ')
elif velocidade_atual <= 80:
  print(' Parabéns! Você é um motorista cauteloso! ')



