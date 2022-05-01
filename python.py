# input and print

name = input("Insert tu nombre : ")
print("hello, "+name)
print(f"hello, {name} ")



# Conditions

num = input("Numero: ")
n=int(num)
if n > 0:
    print("num es positivo")
elif n < 0:
    print("num is negative")
else:
    print("num is zero")
    
    
    
# secuencias

nombre = "harry"
print(nombre[0])

# list en python
names= ["harry", "ron"]
print(names)
print(names[0])

# esto agrega otro cosa a la lista
names.append("Draco")
names.append(8)

# esto sortea los objetos en la lista en orden alfabeticamente
#names.sort()
# para que sorte la lista debe de ser puros str
print(names)
