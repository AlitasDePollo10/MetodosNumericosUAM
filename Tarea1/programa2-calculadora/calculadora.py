print("CALCULADORA")
print("1. Suma")
print("2. Resta")
print("3. Multiplicacion")
print("4. Division")

opcion = input("Seleccion la operacion a realizar: ").strip()

try:
    a = float(input("Primer numero: "))
    b = float(input("Segundo numero: "))
    
    if opcion == '1':
        resultado = a + b
        print(f"Resultado ={resultado:.17f}")
    elif opcion == '2':
        resultado = a - b
        print(f"Resultado = {resultado:.17f}")
    elif opcion == '3':
        resultado = a * b
        print(f"Resultado = {resultado:.17f}")
    elif opcion == '4':
        if b == 0:
            print("No es posible dividir entre cero")
        else:
            resultado = a / b
            print(f"Resultado = {resultado:.17f}")
    else:
        print("Opcion no valida.")
except ValueError:
    print("Numeros no validos")
    