automato = open("automato.txt")
linhas = len(open("automato.txt").readlines())

inicial = automato.readline().rstrip('\n').split(" ")
simbolos = automato.readline().rstrip('\n').split(" ")
estados = automato.readline().rstrip('\n').split(" ")
finais = automato.readline().rstrip('\n').split(" ")

instrucoes = []
for x in range(linhas-4):
    instrucoes.append(automato.readline().rstrip('\n').split(" "))

palavra = ""
if linhas > 4:
    while palavra != "sair":
        palavra = input("\nDigite uma palavra ou digite \"sair\" para encerrar o simulador:\n")

        if palavra != "sair":
            atual = inicial[0]

            situacao = True
            for x in palavra:
                for y in instrucoes:
                    if x in simbolos:
                        if atual == y[0] and x == y[2]:
                            atual = y[1]
                            break
                    else:
                        situacao = False
                        break

            if situacao and atual in finais:
                print("\nPalavra aceita!")
            else:
                print("\nPalavra não aceita!")
    else:
        print("\nO simulador foi encerrado!")
else:
    print("\nNão há registros suficientes para iniciar o simulador!")
