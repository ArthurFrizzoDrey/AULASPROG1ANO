# calcule quant. de combustível necessario para viagem com base na distância e consumo do veículo.
consumo= float(input('Digite o consumo do veículo (km/l): '))
distancia= float(input('Digite a distancia da viagem (km): '))

while distancia >0:
    combustivel_necessario= distancia / consumo
    print(f'Para {distancia} km, você precisará de {combustivel_necessario:.2f} litros de combustível.')
    distancia = float(input('Digite outra distância (ou 0 para sair):'))
print('Calculo encerrado') 