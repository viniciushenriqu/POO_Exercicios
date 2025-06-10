import random

class AnalisadorMatriz:
    def criar_matriz(self, linhas, colunas):
        matriz = []
        print("Preencha a matriz:")
        for i in range(linhas):
            linha = []
            for j in range(colunas):
                while True:
                    try:
                        valor = int(input(f"Digite o valor para a posição [{i}][{j}]: "))
                        linha.append(valor)
                        break
                    except ValueError:
                        print("Entrada inválida. Digite um número inteiro.")
            matriz.append(linha)
        return matriz

    def encontrar_maior_menor(self, matriz):
        if not matriz or not matriz[0]:
            return None, None 

        maior = matriz[0][0]
        menor = matriz[0][0]

        for linha in matriz:
            for elemento in linha:
                if elemento > maior:
                    maior = elemento
                if elemento < menor:
                    menor = elemento
        return maior, menor

    def exibir_matriz(self, matriz):
        if not matriz:
            print("Matriz vazia.")
            return
        for linha in matriz:
            print(linha)

    def somar_diagonais(self, matriz_quadrada):
        if not matriz_quadrada:
            return 0, 0
        n = len(matriz_quadrada)
        if any(len(linha) != n for linha in matriz_quadrada):
            raise ValueError("A matriz não é quadrada.")

        soma_principal = 0
        soma_secundaria = 0

        for i in range(n):
            soma_principal += matriz_quadrada[i][i]
            soma_secundaria += matriz_quadrada[i][n - 1 - i]
        return soma_principal, soma_secundaria

def executar_analisador_matriz(): 
    analisador = AnalisadorMatriz()

    print("--- Exercício 2.1: Maior e Menor Elemento ---")
    while True:
        try:
            m = int(input("Digite o número de linhas da matriz: "))
            n = int(input("Digite o número de colunas da matriz: "))
            if m <= 0 or n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Dimensões inválidas. Por favor, digite números inteiros positivos.")

    matriz_usuario = analisador.criar_matriz(m, n)
    print("\nMatriz criada:")
    analisador.exibir_matriz(matriz_usuario)

    maior_elemento, menor_elemento = analisador.encontrar_maior_menor(matriz_usuario)
    if maior_elemento is not None:
        print(f"O maior elemento na matriz é: {maior_elemento}")
        print(f"O menor elemento na matriz é: {menor_elemento}")
    else:
        print("Não foi possível encontrar maior/menor elemento (matriz vazia).")

    print("\n--- Exercício 2.2: Soma das Diagonais de uma Matriz Quadrada ---")
    while True:
        try:
            ordem_n = int(input("Digite a ordem (n) da matriz quadrada: "))
            if ordem_n <= 0:
                raise ValueError
            break
        except ValueError:
            print("Ordem inválida. Por favor, digite um número inteiro positivo.")

    matriz_quadrada_usuario = analisador.criar_matriz(ordem_n, ordem_n)
    print("\nMatriz quadrada criada:")
    analisador.exibir_matriz(matriz_quadrada_usuario)

    try:
        soma_principal, soma_secundaria = analisador.somar_diagonais(matriz_quadrada_usuario)
        print(f"Soma da Diagonal Principal: {soma_principal}")
        print(f"Soma da Diagonal Secundária: {soma_secundaria}")
    except ValueError as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    executar_analisador_matriz() 