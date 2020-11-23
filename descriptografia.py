alfabeto = input()
alfabeto_cifragem = input()
mensagem = input()

mensagem_descriptografada = ""


for i in mensagem:
    if i not in alfabeto_cifragem:
        mensagem_descriptografada = mensagem_descriptografada + i
        continue

    for j in zip(alfabeto, alfabeto_cifragem):
        if i == j[1]:
            mensagem_descriptografada = mensagem_descriptografada + j[0] 

print(mensagem_descriptografada)
