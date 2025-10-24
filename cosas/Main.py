'''import os
p = os.path.join(os.path.dirname(__file__), 'ventas1.txt'); print(open(p, 'r', encoding='utf-8').read())'''


import os
from numpy import array

p = os.path.join(os.path.dirname(__file__), 'ventas1.txt')

ListAnswers:array = []

with open(p, 'r', encoding='utf-8') as f: [ListAnswers.append(line) for line in f]

print(ListAnswers)
print('---')

for respuestas in ListAnswers:
    lista_respuestas = respuestas.rstrip('\n').split(',')
    #print(lista_respuestas)
    #print('***')
    for campos in lista_respuestas:
        lista_campos = campos.split('\t')
        print(f'nombre {lista_campos[0]}: {lista_campos[1:]}')
        print('final de lista campos')
        


# si no se coloca bien el \t no separa las columnas, lo mismo hace con \n
