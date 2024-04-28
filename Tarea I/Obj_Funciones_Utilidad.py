class Trabajo_Inelastico():
    def __init__(self,sigma):
        self.__parametros=sigma
        self.tipo="Utilidad con trabajo inelástico L=1"
    def get_valor(self,C):
        sigma= self.__parametros
        valor = C**(1-sigma) / (1-sigma)
        return valor
    def derivada_C(self,C):
        sigma=self.__parametros
        valor = C**((-1)*sigma)
        return valor




class CRRA_separable():
    def __init__(self,sigma,phi,psi):
        self.__parametros={"sigma":sigma,"phi":phi,"psi":psi}
        self.tipo="Utilidad CRRA separable"

    def get_valor(self,C,L):
        sigma,phi,psi=self.__parametros["sigma"],self.__parametros["phi"],self.__parametros["psi"]
        valor = ( C**(1-sigma) / (1-sigma) ) - psi* (L**(1+phi))/(1+phi)
        return valor
    def derivada_C(self,C):
        sigma=self.__parametros["sigma"]
        return C**((-1)*sigma)
    def derivada_L(self,L):
        phi,psi=self.__parametros["phi"],self.__parametros["sigma"]
        valor = (-1)*psi*(L**phi)
        return valor
    

class GHH_nonseparable():
    def __init__(self,sigma,phi,psi):
        self.__parametros={"sigma":sigma,"phi":phi,"psi":psi}
        self.tipo="Utilidad GHH nonseparable"

    def get_valor(self,C,L):
        sigma,phi,psi=self.__parametros["sigma"],self.__parametros["phi"],self.__parametros["psi"]
        valor = (1)/(1-sigma) * (C- psi * (L**(1+phi))/(1+phi))**(1-sigma)
        return valor
    def derivada_C(self,C,L):
        sigma,phi,psi=self.__parametros["sigma"],self.__parametros["phi"],self.__parametros["psi"]
        valor = (C-psi* (L**(1+phi))/(1+phi)) ** ((-1)*sigma)
        return valor
    def derivada_L(self,C,L):
        sigma,phi,psi=self.__parametros["sigma"],self.__parametros["phi"],self.__parametros["psi"]
        valor = (C-psi* (L**(1+phi))/(1+phi)) ** ((-1)*sigma) * ((-1)*psi * L**(phi) )
        return valor