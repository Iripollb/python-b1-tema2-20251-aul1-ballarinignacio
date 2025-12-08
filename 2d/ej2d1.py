"""
Enunciado:
Implementa una función 'convert_kg_to_lb' que reciba como parámetro un valor
numérico llamado 'kg' que corresponde al valor que se desea convertir de 
kilogramos a libras.

El valor introducido no puede ser menor o igual que '0', si se introduce un
valor menor o igual a '0' se debe crear un ValueError. El valor introducido
debe ser de type numérico de manera que si se introduce otro valor que no sea
numérico se deberá crear un TypeError.

Parámetros:
kg = Valor numérico que representa a los kilogramos para convertir a libras.

Ejemplo:
    Entrada: 50
    Salida: 110.23

    Entrada: 0
    Salida: ValueError

    Entrada: 'abc'
    Salida: TypeError

"""


def kg_to_lb(kg):   
    if not isinstance(kg, (int, float)):   # Compruebo si kg es int o float y si NO es número hace:
        raise TypeError("The value must be numeric") # Lanzo un error de tipo si no es número

    if kg <= 0:      # Comprueo si el valor es menor o igual a 0
        raise ValueError("The value must be greater than 0")  # Lanzo un error de valor si es inválido

    pounds = kg * 2.20462  # Convierto kilogramos a libras (1 kg = 2.20462 lb)
    return round(pounds, 2)   # Devuelvo el resultado redondeado a 2 decimales



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script
# print(kg_to_lb(50))
