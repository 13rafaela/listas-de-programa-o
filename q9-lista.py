print('Este programa calcula a velocidade média.')
tempo = int(input('Digite o tempo em minutos gasto na viagem:'))
litros = int(input('Digite a quantidade de litros gasto:'))
preço = int(input('Digite o preço do combustível:'))
distancia = int(input('Digite a distância percorrida:'))
vm=distancia/tempo 
print(' A velociade média que seu carro percorreu é de:' , vm)
custo = litros*preço
print('O gasto total da viagem é igual a:', custo)
desempenho = distancia/litros, litros/tempo, preço/distancia
print(' o desempenho do veículo foi de:', desempenho) 
