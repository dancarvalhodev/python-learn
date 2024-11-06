nome = 'Daniel Carvalho'
altura = 1.82
peso = 98
imc = ... # (placeholder, chama elypsis e ele não gera erros no código)
imc = peso / altura ** 2

# o fzinho significa f-strings ou formatação de strings, evita print com + ou ,
linha_1 = f"{nome} tem {altura:.2f} de altura,"
linha_2 = f"pesa {peso} quilos e seu IMC é"
linha_3 = f"{imc:.2f}"

print(linha_1)
print(linha_2)
print(linha_3)
