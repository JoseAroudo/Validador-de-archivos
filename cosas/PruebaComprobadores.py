import re

codigo = r'^[A-Za-z0-9]{2}$'
firstValidation = re.compile(codigo)

palabras = r'^[A-Za-zÁÉÍÓÚáéíóúÑñÜü .-]+$'
pal = re.compile(palabras)

Fecha = r'^\d{2}-\d{2}-\d{4}$'
fechaValidation = re.compile(Fecha)


Lista = ['p3', 'PAPA CRIOLLA', '5000', '02/10/2025']

print(bool(firstValidation.match(Lista[0]))) #upper opcional, isalpha si solo hay letras sin espacios
print(len(Lista[1])<=50 and bool(pal.match(Lista[1])) and Lista[1].isupper()) #upper opcional
print(len(Lista[2])<=10 and Lista[2].isdigit()) # verificar si es un numero de 4 digitos
print(len(Lista[3])==10 and Lista[3].count('-')==2 and bool(fechaValidation.match(Lista[3]))) # verificar formato de fecha