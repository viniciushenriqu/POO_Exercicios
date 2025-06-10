class Contato:
    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"

class Agenda:
    def __init__(self, limite_contatos=10):
        self.contatos = []
        self.limite_contatos = limite_contatos

    def adicionar_contato(self):
        if len(self.contatos) >= self.limite_contatos:
            print(f"Limite de {self.limite_contatos} contatos atingido. Não é possível adicionar mais.")
            return

        print("\n--- Adicionar Novo Contato ---")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")

        novo_contato = Contato(nome, telefone, email)
        self.contatos.append(novo_contato)
        print(f"Contato '{nome}' adicionado com sucesso!")

    def listar_contatos(self):
        print("\n--- Lista de Contatos ---")
        if not self.contatos:
            print("Nenhum contato na agenda ainda.")
            return
        for contato in self.contatos:
            print(contato)

    def procurar_contato(self):
        nome_busca = input("\nDigite o nome do contato para procurar: ")
        encontrado = False
        for contato in self.contatos:
            if contato.nome.lower() == nome_busca.lower():
                print(f"\nDetalhes do Contato Encontrado:")
                print(f"Telefone: {contato.telefone}")
                print(f"Email: {contato.email}")
                encontrado = True
                break
        if not encontrado:
            print(f"Contato '{nome_busca}' não encontrado.")

def executar_agenda(): 
    agenda = Agenda()

    while True:
        print("\n--- Menu da Agenda de Contatos ---")
        print("1. Adicionar Contato")
        print("2. Listar Contatos")
        print("3. Procurar Contato")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            agenda.adicionar_contato()
        elif opcao == '2':
            agenda.listar_contatos()
        elif opcao == '3':
            agenda.procurar_contato()
        elif opcao == '4':
            print("Saindo da agenda de contatos.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

if __name__ == "__main__":
    executar_agenda() 