# VARIÁVEIS
automato = open("automato.txt")
instrucoes = []

inicial = automato.readline().rstrip('\n').split(" ")
simbolos = automato.readline().rstrip('\n').split(" ")
estados = automato.readline().rstrip('\n').split(" ")
finais = automato.readline().rstrip('\n').split(" ")


# FUNÇÃO PARA LEITURA DAS INTRUÇÕES
def lerInstrucoes():
    for x in range(len(open("automato.txt").readlines())-4):
        instrucoes.append(automato.readline().rstrip('\n').split(" "))


# FUNÇÃO QUE CONVERTE AFN PARA AFD
def converter():
    convertido = False

    for x in instrucoes:
        if x[2] == "&":
            convertido = True

            for y in simbolos:
                instrucoes.insert(instrucoes.index(x), [x[0], x[1], y])

            instrucoes.pop(instrucoes.index(x))

    if convertido:
        print("\nO autômato foi convertido com sucesso.\n", instrucoes)
    else:
        print("\nO autômato já é finito determinístico.")


# FUNÇÃO PARA INICIAR O SIMULADOR
def simulador(palavra):
    atual = inicial[0]
    cont = 0

    situacao = True
    for x in palavra:
        cont = 0

        for y in instrucoes:
            if x in simbolos or x == "&":
                if atual == y[0] and x == y[2]:
                    atual = y[1]
                    cont = 1
                    break
            else:
                situacao = False
                break

    if situacao and cont > 0 and atual in finais:
        print("\nPalavra aceita!")
    else:
        print("\nPalavra não aceita!")


# FUNÇÃO MAIN
def main():
    palavra = ""

    while palavra.lower() != "sair":
        palavra = input("\nDigite uma palavra para simular, \"converter\" para converter de AFN para AFD ou digite \"sair\" para encerrar o simulador:\n")

        lerInstrucoes()

        if palavra.lower() == "converter":
            converter()
        elif palavra.lower() != "sair":
            if len(instrucoes) != 0:
                simulador(palavra)
            else:
                print("\nNão há registros suficientes para iniciar o simulador!")
        else:
            print("\nO simulador foi encerrado!")


if __name__ == "__main__":
    main()
