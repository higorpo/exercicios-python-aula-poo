cpf = input()

if cpf == "11111111111":
    print("False")
    quit()

cpf = cpf.replace('.', '').replace('-', '')

digitosVerificadores = [cpf[-2], cpf[-1]]

# Verifica se o primeiro digito verificador esta correto
soma = 0
counter = 10
for numero in cpf[0:-2]:
    soma += int(numero) * counter
    counter -= 1

if soma * 10 % 11 != int(digitosVerificadores[0]):
    print("False")
    quit()
    
# Verifica se o segundo digito verificador esta correto
soma = 0
counter = 11
for numero in cpf[0:-1]:
    soma += int(numero) * counter
    counter -= 1

if soma * 10 % 11 != int(digitosVerificadores[1]):
    print("False")
    quit()
    
print("True")