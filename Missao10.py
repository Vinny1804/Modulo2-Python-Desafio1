# Missão 10: Contando Letras 🔄

# O sistema precisa contar quantas letras há em um nome.
# ➡️ Crie uma função que receba um nome e diga quantas letras esse nome tem.
# ➡️ Exemplo: contar_letras("Ana")
# ➡️ Saída:" O nome Ana tem 3 letras"

def contar_letras():
    nome = str(input('Digite seu nome: '))
    qtd_letras = len(nome)
    print(f'O nome {nome} têm {qtd_letras} letras')

contar_letras()
