from typing import AsyncIterable

#la clase Flight() recibe un argumento que es la capacidad de el vuelo y se inicaliza un list vacia donde se guardaran los nombre de los pasajeros
# esta clase cuenta con dos funciones mas aparte de el constructor
class Flight():
    def __init__(self, capacity):
        self.capacidad = capacity
        self.pasajeros =[]
    
# esta funcion llama a la funcion asientos_disponibes para ver si todavia hay asientos y si no regresa un falso y regresa un mensaje que ya no hay asientos
#pero si hay asientos se agrega el nombre que insertas en esta funcion y despues deuelve un true
    def añadir_pasajero(self, name):
        if not self.asientos_disponibes():
            print("_____________________________________________")
            print("Sin asientos disponibles")
            
            return False
        self.pasajeros.append(name)
        return True

#esta funcion regresa la resta de la capacidad con el numero de pasajeros que ya estan en la list de self.pasajeros       
    def asientos_disponibes(self):
        return self.capacidad - len(self.pasajeros)
    

#este le pregunta al usuario para cuantos alcanza y lo guarda en una variable
AsiDis = int(input("capacidad: "))        
#vuelo = Flight(3)

# vuelo es una variable que recibe la clase Flight() con el numero de capacidad que tiene el vuelo
vuelo = Flight(AsiDis)

#personas = ["luis","pablo","merary", "juan"]
# esta es la lista donde se guardaran los nombres de los pasajeros de el usuario va a agregar
personas = []

#esta variable le va a preguntar a usuario de cuantos viajero van haber
viajeros = int(input("Numero de viajeros: "))
print()

# este loop tomara la variable viajeros para saber cuantas veces debe de preguntar el nombre de los usuarios para despues añadirlo a la lista de personas 
for viajero in range(viajeros):
    nombres=input("nombre de viajero: ")
    print()
    personas.append(nombres)


#este loop tomara la lista de los nombres de las personas que quieran viajar
for person in personas:
    
    #aqui se pasa el primer nombre de la lista personas a la funcion añadir_pasajero de la variable de vuelo que contiene la clase Flight() con la capacidad
    success = vuelo.añadir_pasajero(person)
    
    #mientras la variable de success siga regresando true es estara imprimiendo el nombre de el pasajero que ya tiene lugar y estara abordo
    if success:
        print(f"El pasajero {person} estara abordo. \n")
    
    #pero si regresa un false es por que ya estan llenos todos los asientos y imprimira este mensaje con el nombre de todos los viajeros que no alcanzaron lugar
    else:
        print("_____________________________________________")
        print(f" El pasajero {person} ya no alcanzo asiento ")