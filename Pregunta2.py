"""Utilizando la función del punto 1, realizar otra función que reciba de 
parámetro una lista de números y devuelva sólo aquellos que son primos en 
otra lista"""

def es_primo(numero):
    if numero < 2:  
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def obtener_primos(lista_numeros):
    primos = []
    for numero in lista_numeros:
        if es_primo(numero):
            primos.append(numero)
    return primos

numeros = [2, 3, 4, 5, 6, 7, 8, 9, 10]
primos = obtener_primos(numeros)
print("Números primos:", primos)


