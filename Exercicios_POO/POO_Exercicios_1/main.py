from calculadora import executar_calculadora
from palindromo import executar_verificador_palindromo
from fatorial import executar_fatorial
from conversor_temp import executar_conversor_temp
from matrizes import executar_analisador_matriz
from manipulacao import executar_manipulacao
from gerenciamento import executar_gerenciamento
from agenda import executar_agenda

def exibir_menu_principal():
    print("\n--- Menu Principal de Exercícios de POO ---")
    print("1. Calculadora Simples (1.1)")
    print("2. Verificador de Palíndromos (1.2)")
    print("3. Cálculo de Fatorial (Recursivo) (1.3)")
    print("4. Conversor de Temperaturas (1.4)")
    print("5. Operações com Matrizes (2.1 e 2.2)")
    print("6. Manipulação de Objetos e Referências (3.1 e 3.2)")
    print("7. Sistema de Gerenciamento de Funcionários (4.1)")
    print("8. Agenda de Contatos (4.2)")
    print("0. Sair")
    print("------------------------------------------")

def main():
    while True:
        exibir_menu_principal()
        opcao = input("Digite o número da opção desejada: ")

        if opcao == '1':
            print("\nExecutando: Calculadora Simples...")
            executar_calculadora()
        elif opcao == '2':
            print("\nExecutando: Verificador de Palíndromos...")
            executar_verificador_palindromo()
        elif opcao == '3':
            print("\nExecutando: Cálculo de Fatorial...")
            executar_fatorial()
        elif opcao == '4':
            print("\nExecutando: Conversor de Temperaturas...")
            executar_conversor_temp()
        elif opcao == '5':
            print("\nExecutando: Operações com Matrizes...")
            executar_analisador_matriz()
        elif opcao == '6':
            print("\nExecutando: Manipulação de Objetos e Referências...")
            executar_manipulacao()
        elif opcao == '7':
            print("\nExecutando: Sistema de Gerenciamento de Funcionários...")
            executar_gerenciamento()
        elif opcao == '8':
            print("\nExecutando: Agenda de Contatos...")
            executar_agenda()
        elif opcao == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()