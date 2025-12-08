"""
Enunciado:
Implementa la función 'calculate_max_and_min' que reciba como parámetro una
lista de números 'list_numbers', se deben considerar los casos en los que los
datos que se encuentran dentro de la lista sean de type string o que la lista
se encuentre vacía. 

Adicionalmente, la función debe ir imprimiendo cual es el número menor y el
número mayor según va avanzando en la lista siempre y cuando este sea distinto
al anterior resultado simulando la depuración por trazas.

Y finalmente, retornar un valor del número menor y del número mayor.

Parámetros:
list_numbers: Lista de números.

Ejemplo:
    Entrada: 
        [10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55]
    Salida:
        'Greater:' 200
        'Lesser: ' -55.55

    Entrada:
        ['Hello', 1, 5, -20, 55.5]
    Salida:
        TypeError

    Entrada:
        []
    Salida:
        ValueError



"""

def calculate_max_and_min(list_numbers): 
    if not list_numbers:  # Compruebo si la lista está vacía
        raise ValueError("The list is empty")  # Lanzo un error si la lista no tiene elementos

    for element in list_numbers: 
        if isinstance(element, str): # Compruebo si algún elemento es de tipo string
            raise TypeError("The list contains a string value")# Lanzo un error de tipo si encuentra un string

    min_value = list_numbers[0]   # Inicializao el mínimo con el primer valor de la lista
    max_value = list_numbers[0]    # Inicializo el máximo con el primer valor de la lista

    for number in list_numbers:   # Recorro los números de la lista uno a uno
        if number < min_value:    # Compruebo si el número actual es menor que el mínimo
            min_value = number      # Actualizo el valor mínimo
            print("Lesser:", min_value) # Imprimo el nuevo mínimo (traza de depuración)

        if number > max_value:    # Compruebo si el número actual es mayor que el máximo
            max_value = number     # Actualizo el valor máximo
            print("Greater:", max_value)  # Imprimo el nuevo máximo (traza de depuración)

    return min_value, max_value  # Devuelv0 el mínimo y el máximo encontrados


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# print(
#     "\nResult: ", calculate_max_and_min([10, 5.1, 0, -2, 31, 55, 70, -10, 200, -55.55])
# )
