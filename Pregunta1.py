"""Crear una función que reciba un número como parámetro y devuelva si True 
si es primo y False si no lo es."""

def es_primo(numero):
    if numero < 2:  
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = 17
if es_primo(numero):
    print(f"{numero} es un número primo")
else:
    print(f"{numero} no es un número primo")


