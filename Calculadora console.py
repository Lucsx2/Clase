def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("No se puede dividir por 0")
    return x / y

def Square_root(x):
    if x < 0:
        raise ValueError("No se puede escribir la raiz cuadrada de un numero negativo.")
    return x ** 0.5

def calculator():
    print("Elige una operacion:")
    print("1.suma")
    print("2.resta")
    print("3.multiplicacion")
    print("4.Division")
    print("5.Raiz cuadrada")

    option = int(input("Elige uno"))

    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa el segundo numero: "))
    
    if option == 1:
        result = add(num1, num2)
    if option == 2:
        result = subtract(num1, num2)
    if option == 3:
        result = multiply(num1, num2)
    if option == 4:
        result = divide(num1, num2)
    if option == 5:
        result = Square_root(num1)
    else:
        raise ValueError("Opcion invalida")

    print(f"Resultado: {result}")

if __name__ == "__main__":
    calculator()