"""
Enunciado:
Una tienda tiene una promoción que aplica el descuento del 10% a los productos
cuyo valor numérico sea par. Para ello se requiere implementar funciones capaces 
de sumar una lista de valores pares y retornar dicha suma.

Implementa las funciones 'sum_even_numbers_in_list_while(list_numbers)', 
'sum_even_numbers_in_list_for(list_numbers)' y
'sum_even_numbers_in_list_do_while(list_numbers)' en donde su parámetro
sea una lista de números y utilice un bucle 'WHILE', 'FOR' y 'DO WHILE', respectivamente,
para su implementación. Todas las funciones deben retornar la suma de los números pares.

Parámetros:
    list_numbers (List): lista de precios que se desea sumar

Ejemplo:
    Entrada:
    shopping_list = [10, 449, 33, 44, 188, 640]
    sum_even_numbers_in_list_while(shopping_list)
    sum_even_numbers_in_list_for(shopping_list)
    sum_even_numbers_in_list_do_while(shopping_list)

    Salida:
    En los 3 casos el resultado es 882, que es la suma de 10, 44, 188 y 640. 

"""


def sum_even_numbers_in_list_while(list_numbers):
    # Write here your code
    total = 0 # Inicializo total a 0 ( suma de numeros )
    i = 0 # indice para la lista
    
    while i < len(list_numbers): # mientras indice esté dentro de lista hacer:
        if list_numbers[i] % 2 == 0: # si i es par:
            total += list_numbers[i] # sumo al acumulador
        i += 1 # pasa al siguinte indice
        
    return total # devuelvo las suma de pares



def sum_even_numbers_in_list_for(list_numbers):
    # Write here your code
    total = 0 # inicializo en cero 
    
    for number in list_numbers: # RECORRE CADA NUMERO De LA LISTA
        if number % 2 == 0: # Si es par: 
            total += number #Lo sumo al acumulaor
            
    return total # devueve la suma



def sum_even_numbers_in_list_do_while(list_numbers):
    # Write here your code
    total = 0
    i = 0
    
    if len(list_numbers) == 0: # si la lista está vacia 
        return 0 # devuelve cero
    
    while True: # bucle que no para hasta llegar al break
        if list_numbers[i] % 2 == 0: # si el valor actual es par:
            total += list_numbers[i] # se pone en el acumulador
        
        i += 1# sigue o suma 1 posicion al siguiente valor
        
        if i >= len(list_numbers):# si no hay mas elementos: 
            break # sal del bucle
            
    return total # resueltado de suma



# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# shopping_list = [10, 449, 33, 44, 188, 640]
# print(sum_even_numbers_in_list_while(shopping_list))
# print(sum_even_numbers_in_list_for(shopping_list))
# print(sum_even_numbers_in_list_do_while(shopping_list))
