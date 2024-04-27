def Imagen_Trabajo_Inelastico(obj_utilidad,C):
    sigma=obj_utilidad.parametros
    return ( C[0]**(1-sigma) )/ (1 - sigma)

def Derivada_Trabajo_Inelastico_C(obj_utilidad,C):
    sigma=obj_utilidad.parametros
    return (C[0]**(-1*sigma))

def Imagen_CRRA_Separable(obj_utilidad,C,L):
    sigma,phi,psi=obj_utilidad.parametros["sigma"],obj_utilidad.parametros["phi"],obj_utilidad.parametros["psi"]
    return (C**(1-sigma))/(1-sigma)-psi * (L**(1+phi))/(1+phi)

def Derivada_L_CRRA_Separable(obj_utilidad,L):
    phi,psi=obj_utilidad.parametros["phi"],obj_utilidad.parametros["psi"]
    return (-1)* psi * (L**(phi))

def Utilidad_No_Separable(obj_utilidad,C,L):
    sigma,phi,psi=obj_utilidad.parametros["sigma"],obj_utilidad.parametros["phi"],obj_utilidad.parametros["psi"]
    return (1)/(1-sigma) * (C-psi*(L**(1+phi))/(1+phi))**(1-sigma)

def Derivada_Utilidad_No_Separable_C(obj_utilidad,C,L):
    sigma,phi,psi=obj_utilidad.parametros["sigma"],obj_utilidad.parametros["phi"],obj_utilidad.parametros["psi"]
    return (C-psi * (L**(1+phi))/(1+phi))**((-1)*sigma)

def Derivada_Utilidad_No_Separable_L(obj_utilidad,C,L):
    sigma,phi,psi=obj_utilidad.parametros["sigma"],obj_utilidad.parametros["phi"],obj_utilidad.parametros["psi"]
    return (C-psi * (L**(1+phi))/(1+phi))**((-1)*sigma) * (-1)*psi * (L**(phi))
class Funciones_Utilidad():

    def __init__(self,tipo="Trabajo Inelastico", **kwargs):
        self.funciones_admitidas=["Trabajo Inelastico", "Aversion al Riesgo Constante","No separable"]
        if tipo not in self.funciones_admitidas:
            raise("La función de utilidad especificada debe ser de los siguientes tres tipos:\n Trabajo Inelastico \n Aversion al Riesgo Constante \n No separable.\n")
        if tipo=="Trabajo Inelastico":
            self.__imagen=Imagen_Trabajo_Inelastico
            self.__derivada_c= Derivada_Trabajo_Inelastico_C
            self.parametros=kwargs["sigma"]
        elif tipo =="Aversion al Riesgo Constante":
            self.__imagen = Imagen_CRRA_Separable
            self.__derivada_c=Derivada_Trabajo_Inelastico_C
            self.__derivada_l = Derivada_L_CRRA_Separable
            self.parametros ={"sigma":kwargs["sigma"],"phi":kwargs["phi"],"psi": kwargs["psi"]}
        else:
            self.__imagen = Utilidad_No_Separable
            self.__derivada_c= Derivada_Utilidad_No_Separable_C
            self.__derivada_l= Derivada_Utilidad_No_Separable_L
            self.parametros ={"sigma":kwargs["sigma"],"phi":kwargs["phi"],"psi": kwargs["psi"]}
    
    def get_valor(self,obj_utilidad,*args):
        '''MUY IMPORTANTE, COMO ESTOY USANDO *args, todos los argumentos que les estoy pasando a la función están llegando como tuplas!'''
        valor=self.__imagen(obj_utilidad,args)
        return valor

    def derivada_c(self,obj_utilidad,*args):
        return self.__derivada_c(obj_utilidad,args)
    
    def derivada_l(self,obj_utilidad,*args):
        return self.__derivada_l(obj_utilidad,args)


