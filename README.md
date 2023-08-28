# Simulador de AFN e AFD

Simulador de Autômatos Finitos Determinísticos e Não-Determinísticos, desenvolvido para a disciplina de Complexidade de Algoritmos e Análise de Desempenho da Universidade La Salle em Canoas - RS.

### 📋 Pré-requisitos

Antes de começar, verifique se você atendeu aos seguintes requisitos:
* Você instalou o interpretador [`Python`](https://www.python.org/);

## ⚙️ Funcionamento

O simulador funciona através da leitura de um arquivo ".txt" contendo as instruções para o autômato, onde: a primeira linha representa o estado inicial; a segunda linha representa o alfabeto; a terceira linha representa todos os estados; a quarta linha representa os estados finais; e as linhas a partir da quinta representam as instruções. 

### 🔩 Função lerInstrucoes()

Responsável por ler todas as linhas de instruções dentro do arquivo ".txt" e inserir, através de um laço de repetição, essas instruções em um array "instrucoes".

### 🔩 Função converter()

Percorre o array de instruções procurando o símbolo "&", o que irá contestar a existência de um autômato finito não-determinístico. Caso encontre, ele irá substituir a referida linha por uma com origem igual a cada uma das letras do alfabeto, bem como o destino equivalente. Desta forma, o autômato será convertido para um autômato finito determinístico.

### 🔩 Função simulador()

Percorre cada um dos caracteres da palavra inserida, comparando com as instruções e vendo, portanto, se há instruções válidas para o caracter inserido. Além disso, ele verifica se a letra inserida existe no alfabeto. Após os testes, a função printa resposta positiva ou negativa quanto a validação da palavra.

### 🔩 Função main()

Através de um laço de repetição, recebe a palavra do usuário e filtra conforme três casos: para input _"converter"_, irá invocar a função **converter()** para início da conversão entre AFN e AFD; para input _"sair"_ irá encerrar o simulador; e para qualquer outro caso, será considerado uma palavra a ser validada, invocando, portanto, a função **simulador()**.
