#O código a seguir tem o objetivo de exercitar o conceito de dicionários
#O objetivo é receber nomes digitados pelo usuário, atribuir valores a eles e retornar uma
#média

nome = ''
nota = 0
caderneta = {}
novo_aluno = {}
total = 0


for i in range(0, 3):
    print('Digite o nome do aluno de posição', i, 'no dicionário:')
    nome = (input())
    print('Agora digite a sua nota:')
    nota = int(input())
    novo_aluno[nome] = nota
    caderneta.update(novo_aluno)
    
print('Os nomes dos alunos e suas respectivas notas são:', caderneta)


for valor in caderneta.values():
    total = total + valor

print('A média entre as notas dos alunos é:', total/3)
    