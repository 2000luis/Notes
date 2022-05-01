# input and print

# name = input("Insert tu nombre : ")
# print("hello, "+name)
# print(f"hello, {name} ")



# Conditions

# num = input("Numero: ")
# n=int(num)
# if n > 0:
#     print("num es positivo")
# elif n < 0:
#     print("num is negative")
# else:
#     print("num is zero")
    
    
    
# secuencias

# nombre = "harry"
# print(nombre[0])

# # list en python
# names= ["harry", "ron"]
# print(names)
# print(names[0])

# # esto agrega otro cosa a la lista
# names.append("Draco")
# names.append(8)

# esto sortea los objetos en la lista en orden alfabeticamente
#names.sort()
# para que sorte la lista debe de ser puros str
#print(names)


#sets
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