# if / elif      / else
# se / se não se / se não
entrada = input('Você quer "entrar" ou "sair"? ')

# somente um dos blocos será executado

if entrada == 'entrar': # pode existir sozinho
    print("Você entrou no sistema")
elif entrada == 'sair': # depende de um if antes e pode se repetir N vezes
    print("Você saiu do sistema")
else: # sempre a última opção
    print("Você não digitou nem entrar e nem sair")

print('Fora dos blocos')