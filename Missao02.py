# Missão 2: O Sistema Eleitoral Secreto 📝 

# O grêmio estudantil da escola realiza votações para decidir melhorias e inovações, mas o vírus desativou a verificação de elegibilidade para votar! Sua tarefa é criar um programa que pergunte a idade do usuário e informe se ele pode votar (mínimo: 16 anos).

idade = int(input('Digite a sua idade: '))

if idade >= 16:
    print('Você já pode votar!')
else:
    print('Você ainda não pode votar!')