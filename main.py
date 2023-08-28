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

    while palavra != "sair":
        palavra = input("\nDigite uma palavra ou digite \"sair\" para encerrar o simulador:\n")

        if palavra != "sair":
            lerInstrucoes()

            if len(instrucoes) != 0:
                simulador(palavra)
            else:
                print("\nNão há registros suficientes para iniciar o simulador!")
        else:
            print("\nO simulador foi encerrado!")


if __name__ == "__main__":
    main()
