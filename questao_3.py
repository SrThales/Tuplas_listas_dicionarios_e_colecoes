#O objetivo do código abaixo é exercitar a criação e manipulação de matrizes
#O intuito é percorrer e somar todos os elementos da seguinte matriz

import numpy as np

total = 0

matriz = np.array([[3, 4, 1],
                   [3, 1, 5]])

for i in range(0,2): 
    for j in range(0,3):
        aux1 = matriz[i][j]
        total = total + aux1
        print('A linha', i, 'coluna', j, 'tem valor:', matriz[i][j])
        
        
print('A soma dos elementos da matriz é:', total)