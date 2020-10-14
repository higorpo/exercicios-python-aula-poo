qtdNomes = int(input())

qtdMarias = 0
for i in range(qtdNomes):
    nome = input().split()
    
    if "Maria" in nome:
        qtdMarias += 1
        
print(qtdMarias)