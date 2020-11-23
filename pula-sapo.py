p, n = [int(i) for i in input().split()]
pulos = [int(i) for i in input().split()]

win = True

for i in range(0, n-1):
    if((pulos[i] - pulos[i+1]) < (-p)): 
        win = False 
    elif((pulos[i] - pulos[i+1]) > p): 
        win = False 

if win:
    print('YOU WIN')
else:
    print('GAME OVER')