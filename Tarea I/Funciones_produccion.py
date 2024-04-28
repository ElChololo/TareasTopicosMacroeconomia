
class Funcion_Produccion():

    def __init__(self,parametros):
        '''En parametros sólo estará alfa'''
        self.__parametros=parametros

    def get_valor(self,A,K,L):
        alpha= self.__parametros
        return A* (K**(alpha)) * (L**(1-alpha))

    def derivada_k(self,A,K,L):
        alpha=self.__parametros
        return A* alpha * K**(alpha-1) * L**(1-alpha)
    
    def derivada_l(self,A,K,L):
        alpha=self.__parametros
        return A* (1-alpha) * K**(alpha) * L**((-1) * alpha)

