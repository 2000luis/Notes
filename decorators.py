
na  = input("insert nombre: ")
def anunciamiento(otro):
    def funcionEnVolvente():
        print("hola")
        otro()
        print("como estas?")
    return funcionEnVolvente


@anunciamiento
def nombre():
    print(na)

nombre()