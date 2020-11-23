from collections import Counter

casos_de_teste = int(input())

print('\n')

for i in range(casos_de_teste):
    especies = []
    
    while True:
        try:
            especie = input()

        except EOFError:
            break

        if especie.strip() == '':
            break
            
        especies.append(especie)
    
    especies_count = Counter(especies)
    total_counts = 0

    for value in especies_count.values():
        total_counts += value

    for item, value in especies_count.items():
        print('{} {:.4f}'.format(item, (value / total_counts) * 100))
