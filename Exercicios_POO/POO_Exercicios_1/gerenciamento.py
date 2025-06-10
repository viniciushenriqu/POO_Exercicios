class Funcionario:
    def __init__(self, nome, id_func, salario, departamento):
        self.nome = nome
        self.id = id_func
        self.salario = salario
        self.departamento = departamento

    def __str__(self):
        return (f"ID: {self.id}, Nome: {self.nome}, Salário: R${self.salario:.2f}, "
                f"Departamento: {self.departamento}")

class Gerenciamento:
    def __init__(self):
        self.funcionarios = []

    def cadastrar_funcionario(self):
        print("\n--- Cadastro de Novo Funcionário ---")
        nome = input("Nome: ")
        while True:
            try:
                id_func = int(input("ID: "))
                if any(f.id == id_func for f in self.funcionarios):
                    print("ID já existente. Por favor, insira um ID único.")
                    continue
                break
            except ValueError:
                print("ID inválido. Digite um número inteiro.")
        while True:
            try:
                salario = float(input("Salário: R$"))
                if salario < 0:
                    raise ValueError
                break
            except ValueError:
                print("Salário inválido. Digite um número positivo.")
        departamento = input("Departamento: ")

        novo_funcionario = Funcionario(nome, id_func, salario, departamento)
        self.funcionarios.append(novo_funcionario)
        print(f"Funcionário '{nome}' cadastrado com sucesso!")

    def calcular_total_salarios_departamento(self):
        departamento_alvo = input("\nDigite o nome do departamento para calcular o total de salários: ")
        total_salarios = 0
        encontrado = False
        for func in self.funcionarios:
            if func.departamento.lower() == departamento_alvo.lower():
                total_salarios += func.salario
                encontrado = True
        if encontrado:
            print(f"Total de salários no departamento '{departamento_alvo}': R${total_salarios:.2f}")
        else:
            print(f"Nenhum funcionário encontrado no departamento '{departamento_alvo}'.")


    def listar_todos_funcionarios(self):
        print("\n--- Lista de Todos os Funcionários ---")
        if not self.funcionarios:
            print("Nenhum funcionário cadastrado ainda.")
            return
        for func in self.funcionarios:
            print(func)

def executar_gerenciamento(): 
    gerenciador = Gerenciamento()

    while True:
        print("\n--- Menu de Gerenciamento de Funcionários ---")
        print("1. Cadastrar Funcionário")
        print("2. Calcular Total de Salários por Departamento")
        print("3. Listar Todos os Funcionários")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            gerenciador.cadastrar_funcionario()
        elif opcao == '2':
            gerenciador.calcular_total_salarios_departamento()
        elif opcao == '3':
            gerenciador.listar_todos_funcionarios()
        elif opcao == '4':
            print("Saindo do sistema de gerenciamento de funcionários.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    executar_gerenciamento() 