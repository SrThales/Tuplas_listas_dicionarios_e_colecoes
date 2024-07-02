#O objetivo deste código é exercitar os conhecimentos a respeito da criação e manipulação de 
#listas
#A ideia do código é solicitar 5 inteiros, armazena-los em uma lista e somar todos os inteiros
#utilizando estruturas de repetição

l1 = [0, 1, 2, 3, 4]
total = 0

for i in range (0, 5):
    print('Digite o número de posição', i, ':')
    l1[i] = int(input(''))
    

print('Os inteiros na lista são:', l1)

for j in range (0, 5):
    total = total + l1[j]
    
print('E o valor da soma de todos os inteiros é:', total)
