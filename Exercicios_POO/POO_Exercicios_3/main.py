
from notas import executar_problema1
from bhaskara import executar_problema2
from menor_de_tres import executar_problema3
from plano_telefonia import executar_problema4
from troco_falta import executar_problema5
from glicose import executar_problema6
from dardo import executar_problema7
from conversor_temperatura import executar_problema8
from lanchonete import executar_problema9
from multiplos import executar_problema10
from aumento_salarial import executar_problema11
from duracao_jogo import executar_problema12
from coordenadas_cartesianas import executar_problema13


def exibir_menu_trabalho3():
    print("\n--- Menu: Exercícios do Trabalho POO 3 ---")
    print("1. Problema 'Notas Finais'")
    print("2. Problema 'Fórmula de Bhaskara'")
    print("3. Problema 'Menor de Três'")
    print("4. Problema 'Plano de Telefonia'")
    print("5. Problema 'Troco ou Falta'")
    print("6. Problema 'Medidor de Glicose'")
    print("7. Problema 'Lançamento de Dardo'")
    print("8. Problema 'Conversor de Temperatura'")
    print("9. Problema 'Lanchonete'")
    print("10. Problema 'Múltiplos'")
    print("11. Problema 'Aumento Salarial'")
    print("12. Problema 'Duração do Jogo'")
    print("13. Problema 'Coordenadas Cartesianas'")
    print("0. Sair")
    print("------------------------------------------")

def main():
    while True:
        exibir_menu_trabalho3()
        opcao = input("Digite o número da opção desejada (1-13 ou 0 para sair): ")

        if opcao == '1':
            executar_problema1()
        elif opcao == '2':
            executar_problema2()
        elif opcao == '3':
            executar_problema3()
        elif opcao == '4':
            executar_problema4()
        elif opcao == '5':
            executar_problema5()
        elif opcao == '6':
            executar_problema6()
        elif opcao == '7':
            executar_problema7()
        elif opcao == '8':
            executar_problema8()
        elif opcao == '9':
            executar_problema9()
        elif opcao == '10':
            executar_problema10()
        elif opcao == '11':
            executar_problema11()
        elif opcao == '12':
            executar_problema12()
        elif opcao == '13':
            executar_problema13()
        elif opcao == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

        input("\nPressione Enter para continuar...") # Pausa para o usuário ver a saída

if __name__ == "__main__":
    main()