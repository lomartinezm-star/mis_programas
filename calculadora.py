def calcular(expr: str):
    """
    Evalúa una expresión aritmética sencilla y devuelve el resultado.
    Sólo se aceptan dígitos, espacios y los operadores + - * / ( ).
    """
    # eliminar espacios
    expr = expr.replace(" ", "")
    # comprobamos que no haya caracteres no permitidos
    permitido = set("0123456789+-*/().")
    if not set(expr) <= permitido:
        raise ValueError("Expresión contiene caracteres no válidos")
    # evaluación “segura”
    return eval(expr, {"__builtins__": None}, {})

def main():
    print("Calculadora: escribe la operación y pulsa ENTER")
    expr = input("Expresión: ")
    try:
        resultado = calcular(expr)
    except Exception as e:
        print("Error:", e)
    else:
        print("Resultado:", resultado)

if __name__ == "__main__":
    main()