
from terreno import executar_terreno
from retangulo import executar_retangulo
from idades import executar_idades
from soma import executar_soma
from troco import executar_troco
from circulo import executar_circulo
from pagamento import executar_pagamento
from consumo import executar_consumo
from medidas import executar_medidas
from duracao import executar_duracao


def exibir_menu_estrutura_sequencial():
    print("\n--- Menu de Exercícios de Estrutura Sequencial ---")
    print("1 Problema 'terreno'")
    print("2 Problema 'retangulo'")
    print("3 Problema 'idades'")
    print("4 Problema 'soma'")
    print("5 Problema 'troco'")
    print("6 Problema 'circulo'")
    print("7 Problema 'pagamento'")
    print("8 Problema 'consumo'")
    print("9 Problema 'medidas'")
    print("10 Problema 'duracao'")
    print("0. Sair")
    print("--------------------------------------------------")

def main():
    while True:
        exibir_menu_estrutura_sequencial()
        opcao = input("Digite o número da opção desejada (ex: 2.1, 2.10 ou 0 para sair): ")

        if opcao == '1':
            print("\nExecutando: Problema 'terreno'...")
            executar_terreno()
        elif opcao == '2':
            print("\nExecutando: Problema 'retangulo'...")
            executar_retangulo()
        elif opcao == '3':
            print("\nExecutando: Problema 'idades'...")
            executar_idades()
        elif opcao == '4':
            print("\nExecutando: Problema 'soma'...")
            executar_soma()
        elif opcao == '5':
            print("\nExecutando: Problema 'troco'...")
            executar_troco()
        elif opcao == '6':
            print("\nExecutando: Problema 'circulo'...")
            executar_circulo()
        elif opcao == '7':
            print("\nExecutando: Problema 'pagamento'...")
            executar_pagamento()
        elif opcao == '8':
            print("\nExecutando: Problema 'consumo'...")
            executar_consumo()
        elif opcao == '9':
            print("\nExecutando: Problema 'medidas'...")
            executar_medidas()
        elif opcao == '10':
            print("\nExecutando: Problema 'duracao'...")
            executar_duracao()
        elif opcao == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

        input("\nPressione Enter para continuar...") 

if __name__ == "__main__":
    main()