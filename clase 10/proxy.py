import singletondb

class Implementation: 
    #Crea la instancia
    singleton = singletondb()
   
    def mexico(self):
        #Define el Query
        query = "SELECT * FROM postalCodeMexico"
      
       #Consigue el codigo postal y lo regresa 
        return singleton.get_postalCode(query)

    def estadosUnidos(self):
        #Define el Query
        query = "SELECT * FROM postalCodeUSA"
        
       
       #Consigue el codigo postal y lo regresa
        return singleton.get_postalCode(query)

    def canada(self):
        #Define el Query
        query = "SELECT * FROM postalCodeCanada"
        
        #Consigue el codigo postal y lo regresa 
        return singleton.get_postalCode(query)

class Proxy:
    def __init__(self):
        self.__implementation = Implementation()

    def mexicoProxy(self): return self.__implementation.mexico()
    def canadaProxy(self): return self.__implementation.canada()
    def ustadoUnidosProxy(self): return self.__implementation.estadosUnidos()

