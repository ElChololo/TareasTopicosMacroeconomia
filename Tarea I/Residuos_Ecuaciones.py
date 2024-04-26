import numpy as np

from Sistema_Ecuaciones import *


def Residuos_Ecuaciones_SS(obj_utilidad,obj_producion,parametros,guess, Flag_trabajo=False):
    if type(parametros)!= dict or type(guess) != dict:
        raise("Tanto los parametros como los guess inicial deben ser entregados como diccionarios")
    
    # Sin trabajo el sistema tiene 6 ecuaciones (Productivdad de EE es 1 dado la forma funcional):
    if Flag_trabajo==False:
        #Ecuacion de euler (debo cambiar porque la derivada de c a veces depende solo de C y otras tambien de L)
        res_ec_euler= res_Ec_Euler(obj_utilidad,C,C_prime,beta,tasa_interes)
        # Restriccion del individuo
        res_rest_indv=  res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K)
        # Prd. mg del capital
        res_prd_mg_k=obj_utilidad.derivada_k() - guess["Tasa_Interes_ss"]+ parametros["delta"]
        # Balance de gobierno
        res_bal_gob = bal_gobierno(G,impuesto,salario,L)
        #Vaciamiento de mercado
        res_vac_mer=res_vac_mercado(obj_produccion,C,G,K_prime,delta,K)
        #Shock de Gobierno
        res_shock_gob=shock_gobierno(G,ro_g,g_bar,Y,G_rez,sigma_g,epsilon_g)
        # Computamos el vector de residuos
        return np.array([res_ec_euler,res_rest_indv,res_prd_mg_k,res_bal_gob,res_vac_mer,res_shock_gob])