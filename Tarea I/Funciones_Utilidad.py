def Imagen_Trabajo_Inelastico(obj_utilidad,C):
    sigma=obj_utilidad.parametros["sigma"]
    return ( C[0]**(1-sigma) )/ (1 - sigma)

def Derivada_Trabajo_Inelastico_C(obj_utilidad,C):
    '''También se utilizada para la derivada con respecto a C de la utilidad CRRA'''
    sigma=obj_utilidad.parametros["sigma"]
    return (C[0]**(-1*sigma))

def Imagen_CRRA_Separable(obj_utilidad,*args):
    sigma,phi,psi=obj_utilidad.parametros["sigma"],obj_utilidad.parametros["phi"],obj_utilidad.parametros["psi"]
    C=args[0][0]
    L=args[0][1]
    return (C**(1-sigma))/(1-sigma)-psi * (L**(1+phi))/(1+phi)

def Derivada_L_CRRA_Separable(obj_utilidad,L):
    L=L[0]
    phi,psi=obj_utilidad.parametros["phi"],obj_utilidad.parametros["psi"]
    return (-1)* psi * (L**(phi))

def Utilidad_No_Separable(obj_utilidad,*args):
    C=args[0][0]
    L=args[0][1]
    sigma,phi,psi=obj_utilidad.parametros["sigma"],obj_utilidad.parametros["phi"],obj_utilidad.parametros["psi"]
    return (1)/(1-sigma) * (C-psi*(L**(1+phi))/(1+phi))**(1-sigma)

def Derivada_Utilidad_No_Separable_C(obj_utilidad,*args):
    C=args[0][0]
    L=args[0][1]
    sigma,phi,psi=obj_utilidad.parametros["sigma"],obj_utilidad.parametros["phi"],obj_utilidad.parametros["psi"]
    return (C-psi * (L**(1+phi))/(1+phi))**((-1)*sigma)

def Derivada_Utilidad_No_Separable_L(obj_utilidad,*args):
    C=args[0][0]
    L=args[0][1]
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
            self.parametros={"sigma":kwargs["sigma"]}
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


## Testeo
u_1= Funciones_Utilidad(sigma=2)
u_1.get_valor(u_1,5)
u_1.derivada_c(u_1,5)
u_2= Funciones_Utilidad(tipo="Aversion al Riesgo Constante",sigma=2,phi=2,psi=2)
u_2.get_valor(u_2,2,2)
u_2.derivada_c(u_2,2)
u_2.derivada_l(u_2,2)
u_3= Funciones_Utilidad(tipo="No separable",sigma=2,phi=2,psi=2)
u_3.get_valor(u_2,2,2)
u_3.derivada_c(u_3,2,2)
u_3.derivada_l(u_3,2,2)