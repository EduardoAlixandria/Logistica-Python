def dimensoesObjeto(): #Inicio função da dimensão do objeto
  print('-------- Menu 1 de 3 - Dimensões do Objeto --------')
  while True:
    try:
        comprimento=float(input('Digite  o comprimento do objeto (em cm): '))
        largura=float(input('Digite a largura do objeto (em cm): '))
        altura=float(input('Digite  a altura do objeto (em cm): '))
        volume=comprimento*largura*altura
        print('O  volume do objeto é (em cm³): {:.2f}' .format(volume))
        if volume < 1000:
            return 10 #Retorna o valor a ser cobrado da dimensão do objeto
        elif 1000 <= volume < 10000:
            return 20 #Retorna o valor a ser cobrado da dimensão do objeto
        elif 10000 <= volume < 30000:
            return 30 #Retorna o valor a ser cobrado da dimensão do objeto
        elif 30000 <= volume < 100000:
            return 50 #Retorna o valor a ser cobrado da dimensão do objeto
        elif volume >= 100000:
            print('Não aceitamos objetos com essas dimensões!')
    except ValueError: #Caso o usuário digite qualquer letra no lugar de uma valor numérico
        print('Você digitou alguma dimensão  com valor não numérico!')
        print('Por favor insira novamente as dimensões do objeto!')
# Fim da função dimensãoObjeto().

def pesoObjeto(): #Inicio função do peso do objeto
  print('-------- Menu 2 de 3 - Peso do Objeto -------------')
  while True:
    try:
        peso=float(input('Digite o peso do objeto (em Kg): '))
        if peso <= 0.1:
            return 1
        elif 0.1 <= peso < 1:
            return 1.5
        elif 1 <= peso < 10:
            return 2
        elif 10 <= peso < 30:
            return 3
        elif peso >= 30:
            print('Não transportamos objetos tão pesados!')
            print('Por favor insira novamente o peso do objeto!')
    except ValueError: #Caso o usuário digite qualquer letra no lugar de uma valor numérico
        print('Digite um valor numérico para o peso do objeto!')

# Fim da função pesoObjeto().

def rotaObjeto(): #Inicio função de rota do objeto
  print('-------- Menu 3 de 3 - Rota  da entrega -----------')
  print('------------ Rotas Disponíveis -----------')
  print('      CS - Curitiba p/ São Paulo')
  print('      SC - São Paulo p/ Curitiba')
  print('      SB - São Paulo p/ Belo Horizonte')
  print('      BS - Belo Horizonte p/ São Paulo')
  print('      CB - Curitiba p/ Belo Horizonte')
  print('      BC - Belo Horizonte p/ Curitiba')

  while True:
    rota=input('Digite a sigla da rota desejada: ')
    rota=rota.upper() #Resolve o problema entre maiuscula e minuscula
    if rota != 'CS' and rota != 'SC' and rota != 'SB' and rota != 'BS' and rota != 'CB' and rota != 'BC':
        print('Você digitou uma rota inexistente!')
        print('Por favor insira novamente a rota desejada!')
        continue
    elif rota == 'CS':
        return 1
    elif rota == 'SC':
        return 1
    elif rota == 'SB':
        return 1.2
    elif rota == 'BS':
        return 1.2
    elif rota == 'CB':
        return 1.5
    elif rota == 'BC':
        return 1.5
    else:
        break
# Fim da função rotaObjeto().

#Inicio do Main
print('Bem Vindo a  empresa de Logística João Alixandria S.A')
valorDimensão=dimensoesObjeto()
multiplicadorPeso=pesoObjeto()
multiplicadorRota=rotaObjeto()
valorTotal=valorDimensão*multiplicadorPeso*multiplicadorRota #Valor total a ser pago pelo cliente
print('Valor total a ser pago: R${:.2F}  (Dimensão: R${:.2F}, * Peso: {:.2F}, * Rota: {:.2F})' .format(valorTotal,valorDimensão,multiplicadorPeso,multiplicadorRota))




