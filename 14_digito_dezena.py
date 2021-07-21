# Descobre o digito das dezenas
numero = input("Digite um número inteiro:")
resto_centena = int(numero) % 100  # O resultado é um número menor que 100
dezena = resto_centena // 10 # O resultado é a quantidade de dezenas inteiras
print("O dígito das dezenas é", dezena)
