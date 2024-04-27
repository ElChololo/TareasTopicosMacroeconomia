def Produccion_Cobb_Douglas(obj_produccion,A,K,L):
    alpha=obj_produccion.parametros
    return A* (K**(alpha)) * (L**(1-alpha))

def Derivada_Prod_Cobb_Douglas_K(obj_produccion,A,K,L):
    alpha=obj_produccion.parametros
    return A* alpha * K**(alpha-1) * L**(1-alpha)

def Derivada_Prod_Cobb_Douglas_L(A,K,L,alpha):
    return A* (1-alpha) * K**(alpha) * L**((-1) * alpha)
class Funcion_Produccion():

    def __init__(self,parametros,flag=True):
        '''En parametros sólo estará alfa'''
        self.__valor = Produccion_Cobb_Douglas
        self.__derivada_k = Derivada_Prod_Cobb_Douglas_K
        self.parametros=parametros
        if flag ==False:
            self.__derivada_l = Derivada_Prod_Cobb_Douglas_L
        

    def get_valor(self,obj_produccion,A,K,L):
        return self.__valor(obj_produccion,A,K,L)

    def derivada_k(self,obj_produccion,A,K,L):
        return self.__derivada_k(obj_produccion,A,K,L)
    
    def derivada_l(self,obj_produccion,*args):
        return self.__derivada_l(obj_produccion,args)

