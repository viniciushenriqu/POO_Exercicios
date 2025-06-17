class Lanchonete:
    def __init__(self):
        self.menu = {
            1: 5.00,  
            2: 3.50,  
            3: 4.80,  
            4: 8.90,  
            5: 7.32   
        }

    def calcular_valor_total(self, codigo, quantidade):
        if codigo in self.menu:
            preco_unitario = self.menu[codigo]
            return preco_unitario * quantidade
        else:
            return None 

def executar_problema9():
    print("\n--- Problema 9: Lanchonete ---")
    while True:
        try:
            codigo = int(input("Codigo do produto comprado: "))
            if codigo not in [1, 2, 3, 4, 5]:
                print("Código de produto inválido. Por favor, digite um código de 1 a 5.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para o código.")

    while True:
        try:
            quantidade = int(input("Quantidade comprada: "))
            if quantidade <= 0:
                print("Quantidade deve ser positiva. Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro para a quantidade.")

    lanchonete = Lanchonete()
    valor_total = lanchonete.calcular_valor_total(codigo, quantidade)

    if valor_total is not None:
        print(f"Valor a pagar: R$ {valor_total:.2f}")
    else:
        print("Código de produto inválido.")

if __name__ == "__main__":
    executar_problema9()