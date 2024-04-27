def Produccion_Cobb_Douglas(alpha,A,K,L):
    return A* (K**(alpha)) * (L**(1-alpha))

def Derivada_Prod_Cobb_Douglas_K(alpha,A,K,L):
    return A* alpha * K**(alpha-1) * L**(1-alpha)

def Derivada_Prod_Cobb_Douglas_L(alpha,A,K,L):
    return A* (1-alpha) * K**(alpha) * L**((-1) * alpha)
class Funcion_Produccion():

    def __init__(self,parametros,flag=True):
        '''En parametros sólo estará alfa'''
        self.__valor = Produccion_Cobb_Douglas
        self.__derivada_k = Derivada_Prod_Cobb_Douglas_K
        self.parametros=parametros
        if flag ==False:
            self.__derivada_l = Derivada_Prod_Cobb_Douglas_L
        

    def get_valor(self,A,K,L):
        alpha= self.parametros
        return self.__valor(A,K,L)

    def derivada_k(self,A,K,L):
        alpha=self.parametros
        return self.__derivada_k(alpha,A,K,L)
    
    def derivada_l(self,A,K,L):
        alpha=self.parametros
        return self.__derivada_l(alpha,A,K,L)

