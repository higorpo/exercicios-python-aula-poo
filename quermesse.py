num_caso_teste = 1
while True:
    try:
        numero_ingressos = int(input())
        ordem_chegada = [int(i) for i in input().split()]
    except EOFError:
        break

    if numero_ingressos == 0:
        break

    num_ganhador = 0

    for index, num in enumerate(ordem_chegada):
        if index + 1 == num:
            num_ganhador = num
    
    print('Teste {}'.format(num_caso_teste))
    print(num_ganhador)

    num_caso_teste = num_caso_teste + 1