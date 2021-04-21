import singletondb

class Implementation:
    # Instancia de singleton
   
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

    def mexicoProxy(self): return self.__implementation.mexico()
    def canadaProxy(self): return self.__implementation.canada()
    def ustadoUnidosProxy(self): return self.__implementation.estadosUnidos()

