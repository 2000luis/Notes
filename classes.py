class Point():
    def __init__(o, x,y) :
        o.ValorX=x
        o.ValorY=y
#Para inciar la clase se crea un tipo constructor como en javascript  que se llama __init__ se especifica el this como self o con cualquier nombre pero se necesita

       
valorX = input("Inserta el valor de x: ")
valorY = input("Inserta el valor de Y: ")
        
punto = Point(valorX,valorY)

print()
print(f"Este es el valor x: {punto.ValorX}")
print(f"Este es el valor y: {punto.ValorY}")
