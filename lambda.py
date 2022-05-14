personas=[
    {"nombre":"luis", "sexo":"2"},
    {"nombre":"mera", "sexo":"3"},
    {"nombre":"bera", "sexo":"4"},
    {"nombre":"cera", "sexo":"6"}
]

#def help(person):
#    return person["nombre"]
    
#personas.sort(key=help)


#la lambda es lo mismo que si escribiera lo de lambda

personas.sort(key=lambda person: person["sexo"])

print(personas)