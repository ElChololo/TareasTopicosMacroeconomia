def Imagen_Trabajo_Inelastico(C,sigma):
    return ( C**(1-sigma) )/ (1 - sigma)

def Derivada_Trabajo_Inelastico_C(C,sigma):
    return (C**(-1*sigma))

def Imagen_CRRA_Separable(C,sigma,L,phi,psi):
    return (C**(1-sigma))/(1-sigma)-psi * (L**(1+phi))/(1+phi)

def Derivada_L_CRRA_Separable(L,phi,psi):
    return (-1)* psi * (L**(phi))

def Utilidad_No_Separable(C,sigma,L,phi,psi):
    return (1)/(1-sigma) * (c-psi*(L**(1+phi))/(1+phi))**(1-sigma)

def Derivada_Utilidad_No_Separable_C(C,sigma,L,psi,phi):
    return (C-psi * (L**(1+phi))/(1+phi))**((-1)*sigma)

def Derivada_Utilidad_No_Separable_L():
    return (C-psi * (L**(1+phi))/(1+phi))**((-1)*sigma) * (-1)*psi * (L**(phi))
class Funciones_Utilidad():

    def __init__(self,tipo="Trabajo Inelastico", **kargs):
        self.funciones_admitidas=["Trabajo Inelastico", "Aversion al Riesgo Constante","No separable"]
        if tipo not in self.funciones_admitidas:
            raise("La función de utilidad especificada debe ser de los siguientes tres tipos:\n Trabajo Inelastico \n Aversion al Riesgo Constante \n No separable.\n")
        if tipo="Trabajo Inelastico":
            self.__imagen=Imagen_Trabajo_Inelastico
            self.__derivada_c= Derivada_Trabajo_Inelastico_C
        elif tipo ="Aversion al Riesgo Constante":
            self.__imagen = Imagen_CRRA_Separable
            self.__derivada_c=Derivada_Trabajo_Inelastico_C
            self.__derivada_l = Derivada_L_CRRA_Separable
        else:
            self.__imagen = Utilidad_No_Separable
            self.__derivada_c= Derivada_Utilidad_No_Separable_C
            self.__derivada_l= Derivada_Utilidad_No_Separable_L
    
    def get_valor(self,*args,**kargs):
        valor=self.__imagen(*args)
        return valor

    def derivada_c(self,*args):
        return self.__derivada_c(*args)
    
    def derivada_l(self,*args):
        return self.__derivada_l(*args)


