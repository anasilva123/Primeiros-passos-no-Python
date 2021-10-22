# condicinoais
# if, elif e else
# Usar dois símbolos de == para comparar uma informação

leitura_concluida = False
if leitura_concluida == True:
  print( 'Legal! Vamos para o próximo? ' )
else:
  print( ' Então não podemos perder mais tempo! ' )
  

horario_disponivel = True
if horario_disponivel == True:
  print( ' Sim, eu tenho horários disponíveis. ' )
else:
  print( ' Infelizmente, não tenho horários disponíveis. ' )
  
  
numero_de_atrasos = 0
if numero_de_atrasos >= 3:
  print( ' Você está suspenso! ' )
elif numero_de_atrasos == 2:
  print( ' Se chegar atrasado mais uma vez, será suspenso! ' )
elif numero_de_atrasos == 1:
  print( ' Pode entrar, mas, tente não se atrasar mais. ' )
else:
  print( ' Pode entrar. ' )


primeiro_valor = input(' Didite o 1º valor: ' )
segundo_valor = input(' Digite o 2º valor: ')

if int(primeiro_valor) > int(segundo_valor):
  print(' O primeiro valor é maior do que o segundo. ')
else:
  print(' O segundo valor é maior do que o primeiro. ')


