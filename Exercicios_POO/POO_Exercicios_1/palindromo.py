class VerificadorPalindromo:
    def eh_palindromo(self, texto):
        texto_limpo = "".join(filter(str.isalnum, texto)).lower()
        return texto_limpo == texto_limpo[::-1]

def executar_verificador_palindromo(): 
    verificador = VerificadorPalindromo()
    palavra = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")

    if verificador.eh_palindromo(palavra):
        print(f"'{palavra}' é um palíndromo.")
    else:
        print(f"'{palavra}' não é um palíndromo.")

if __name__ == "__main__":
    executar_verificador_palindromo() 