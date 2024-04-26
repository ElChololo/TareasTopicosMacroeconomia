def Produccion_Cobb_Douglas(A,K,L,alpha):
    return A* (K**(alpha)) * (L**(1-alpha))

def Derivada_Prod_Cobb_Douglas_K(A,K,L,alpha):

    return A* alpha * K**(alpha-1) * L**(1-alpha)

def Derivada_Prod_Cobb_Douglas_L(A,K,L,alpha):
    return A* (1-alpha) * K**(alpha) * L**((-1) * alpha)
class Funcion_Produccion():

    def __init__(self,parametros,flag=True):
        if type(parametros) != dict:
            raise("Los parametros de la funcion de utilidad deben ser entregados como un diccionario")
        self.__parametros={}
        for keys in parametros:
            self.__parametros[keys]=parametros[keys]

        self.__valor = Produccion_Cobb_Douglas
        self.__derivada_k = Derivada_Prod_Cobb_Douglas_K
        if flag ==False:
            self.__derivada_l = Derivada_Prod_Cobb_Douglas_L
        

    def get_valor(self,*args):
        return self.__valor(args)

    def derivada_k(self,*args):
        return self.__derivada_k(args)
    
    def derivada_l(self,*args):
        return self.__derivada_l(args)

