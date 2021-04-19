import singletondb

class Implementation:
    # Instancia de singleton
    # Revisa si ya hay una instancia, crea o no la instancia
    def mexico(self):
       #cambio de la base de datos/tabla a MX
       #Abre conexion 
       #Consigue el codigo postal 
        return "Implementation.f()"
    def estadosUnidos(self):
        #Cambio de la base de datos/tabla a EEUU
        #Abre conexion 
        #Consigue el codigo postal 
        return "Implementation.g()"
    def canada(self):
        #cambio de la base de datos/tabla CA
        #Abre conexion 
        #Consigue el codigo postal 
        return "Implementation.h()"

class Proxy:
    def __init__(self):
        self.__implementation = Implementation()

    def f(self): return self.__implementation.f()
    def g(self): return self.__implementation.g()
    def h(self): return self.__implementation.h()

