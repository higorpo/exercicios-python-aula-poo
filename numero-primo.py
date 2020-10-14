number = int(input())

isPrimeNumber = True

if number != 1:
    for i in range(number):
        resto = number % (i + 1)
        if resto == 0:
            if (i+1) != 1 and (i+1) != number:
                isPrimeNumber = False
                break
else:
    isPrimeNumber = False
    
print(isPrimeNumber)