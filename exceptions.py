import sys
try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("\n Error: Debe ser un numero ")
    sys.exit(1)   
try:
    result = x/y
except ZeroDivisionError:
    print("\n Error: No puedes dividir por 0") 
    sys.exit(1)   
print(f"el resultado es : {result}")