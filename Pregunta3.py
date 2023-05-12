
"""Crear una función que convierta entre grados Celsius, Farenheit y Kelvin
Convertir a farenheit : (°C × 9/5) + 32 = °F
Convertir a Kelvin: °C + 273.15 = °K
Debe recibir 3 parámetros: el valor, la medida de origen y la medida de 
destino"""

def convert_temperature(value, source_unit, target_unit):
    if source_unit == 'Celsius':
        if target_unit == 'Fahrenheit':
            result = (value * 9/5) + 32
            return result
        elif target_unit == 'Kelvin':
            result = value + 273.15
            return result
        else:
            print("Unidad de destino no válida.")
    elif source_unit == 'Fahrenheit':
        if target_unit == 'Celsius':
            result = (value - 32) * 5/9
            return result
        elif target_unit == 'Kelvin':
            result = (value + 459.67) * 5/9
            return result
        else:
            print("Unidad de destino no válida.")
    elif source_unit == 'Kelvin':
        if target_unit == 'Celsius':
            result = value - 273.15
            return result
        elif target_unit == 'Fahrenheit':
            result = (value * 9/5) - 459.67
            return result
        else:
            print("Unidad de destino no válida.")
    else:
        print("Unidad de origen no válida.")

# Ejemplo de uso
valor_origen = 25
unidad_origen = 'Celsius'
unidad_destino = 'Fahrenheit'

resultado = convert_temperature(valor_origen, unidad_origen, unidad_destino)
print(f"{valor_origen} {unidad_origen} equivale a {resultado} {unidad_destino}")

