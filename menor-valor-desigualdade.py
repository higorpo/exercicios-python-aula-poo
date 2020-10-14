# Calcular o menor número inteiro positivo x tal que x! > x^10

x = 1

def fatorial(number):
    n = 1  
    while (number > 1):  
      n = n * number  
      number = number - 1
      
    return n

while True:
    if fatorial(x) > x ** 10:
        break
    else:
        x += 1
        
print(x)