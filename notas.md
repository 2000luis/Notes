list: secuencias de varios valores
===

names= ["harry", "ron"] 

tuple: secuencias de lista que no son mutalbes
===
coordinateX=10.0
coordinatey=20.0

coordinate = (10.0,20.0)

set: una collection de valores unicos
===

#agregamos un set vacio
s = set()

#Agregamos valores a ese set 
print()
s.add(1)
s.add(2)
s.add(3)
#Si agregamos otro tres no aparecera en el set porque no se pueden repetir valores en un set
s.add(3)
s.add("hola")

print(s)

#para remover algo de un set se usa el la funcion 

s.remove(3)
print(s)

# Y para determinar cuantos elementos hay en el set o en cualquier cosa 

#len(s)

#los usaremos a dentro de un str

print(f"the length of the set is {len(s)} elements long . ")

dict: collection de key=vaules 
===