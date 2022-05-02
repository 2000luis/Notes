# asi se importa una funcion de otro file 
from square import square

#la funcion esta en el file square.py
for i in range(11):
    print(f"el cuadrado de {i} es {square(i)} ")