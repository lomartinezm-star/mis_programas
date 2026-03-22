import math

def area_circulo(radio):
    """
    Calcula el área de un círculo.

    Args:
        radio (float): Radio del círculo.

    Returns:
        float: Área calculada.
    """
    return math.pi * radio ** 2

#**************************************************


def es_primo(n):
    """
    Determina si un número es primo.

    Args:
        n (int): Número a evaluar.

    Returns:
        bool: True si es primo, False en caso contrario.
    """
    if n <= 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

#**************************************************


def factorial(n):
    """
    Calcula el factorial de un número.

    Args:
        n (int): Número entero.

    Returns:
        int: Factorial de n.
    """
    resultado = 1

    for i in range(1, n + 1):
        resultado *= i

    return resultado

#**************************************************

def fibonacci(n):
    """
    Genera los primeros n números de Fibonacci.

    Args:
        n (int): Cantidad de números.

    Returns:
        list: Lista con la secuencia de Fibonacci.
    """
    secuencia = []
    a, b = 0, 1

    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b

    return secuencia

#**************************************************

def celsius_a_fahrenheit(c):
    """
    Convierte grados Celsius a Fahrenheit.

    Args:
        c (float): Temperatura en Celsius.

    Returns:
        float: Temperatura en Fahrenheit.
    """
    return (c * 9/5) + 32

#**************************************************

def maximo(lista):
    """
    Obtiene el valor máximo de una lista sin usar max().

    Args:
        lista (list): Lista de números.

    Returns:
        int/float: Valor máximo.
    """
    max_val = lista[0]

    for num in lista:
        if num > max_val:
            max_val = num

    return max_val