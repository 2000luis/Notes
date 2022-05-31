#dictionaries
houses = {"Luis":"la verga","Anthony":"el wey"}

#Asi es como agregas otro elemento un dictionarie
houses["jaque"]="her"

#asi es como llamas un elemento de un dictionarie
print(houses["jaque"])

j={'luis':1,'juan':4,'sara':3,}
print(list(j))
#Te sale los keys en una lista
#['luis', 'juan', 'sara']

print(j.keys())
#Te regresa lo mismo que list los nombre de los keys
#['luis', 'juan', 'sara']

print(j.values())
#Te regresa los valores de los keys
#[1,4,3]


print(j.items())
#Esta forma te regresa un tipo de tuple como una lista pero con tuples a dentro
#[('luis',1) ('juan',4) ('sara',3)]


for keyllave,valuevalor in j.items():
    print(keyllave,valuevalor)
    
#['luis', 'juan', 'sara']
#dict_values([1, 4, 3])
#dict_keys(['luis', 'juan', 'sara'])
#dict_items([('luis', 1), ('juan', 4), ('sara', #3)])
#luis 1
#juan 4
#sara 3

#dict() dicionario vacio
