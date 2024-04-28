import numpy as np

from Ecuaciones_sistema import *


def Residuos_Ecuaciones_SS(obj_utilidad,obj_produccion,parametros,guess, Flag_trabajo=False):
    if type(parametros)!= dict or type(guess) != dict:
        raise("Tanto los parametros como los guess inicial deben ser entregados como diccionarios")
    #Sabemos que en estado estacionario, el valor de la productividad estára en su media incondicional
    # Para esta tarea, la forma funcional es fija y da como resultado una media incondicional de 1
    A_ss=1
    #parametros
    beta,delta,g_bar = parametros["beta"],parametros["delta"],parametros["g_bar"]
    # Sin trabajo el sistema tiene 6 ecuaciones (Productivdad de EE es 1 dado la forma funcional):
    if Flag_trabajo==False:
        #Ecuacion de euler 

        #Variables
        C,C_prime,tasa_interes,K_prime,K = guess["Consumo_ss"],guess["Consumo_ss"],guess["Tasa_Interes_ss"],guess["Capital_ss"],guess["Capital_ss"]
        impuesto,salario,G,trabajo=guess["Impuesto_ss"],guess["Salario_ss"],guess["Gobierno_ss"],1


        res_ec_euler= res_Ec_Euler(obj_utilidad,C,C_prime,trabajo,trabajo,beta,tasa_interes) 
        # Restriccion del individuo
        resi_rest_indv=  res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K)
        # Prd. mg del capital
        res_prd_mg_k=prod_mg_capital(obj_produccion,A_ss,K,trabajo,tasa_interes,delta)
        # Balance de gobierno
        res_bal_gob = bal_gobierno(G,impuesto,salario,trabajo)
        #Vaciamiento de mercado
        res_vac_mer=res_vac_mercado(obj_produccion,A_ss,C,G,K_prime,delta,K,trabajo)
        #Shock de Gobierno
        res_shock_gob=shock_gobierno_ss(obj_produccion,G,A_ss,K,trabajo,g_bar)
        # Computamos el vector de residuos
        return np.array([res_ec_euler,resi_rest_indv,res_prd_mg_k,res_bal_gob,res_vac_mer,res_shock_gob])
    else:
        #Caso de funciones con trabajo, se añaden 2 ecuaciones adicionales: oferta laboral y prd_mg_K
        
        C,C_prime,tasa_interes,K_prime,K = guess["Consumo_ss"],guess["Consumo_ss"],guess["Tasa_Interes_ss"],guess["Capital_ss"],guess["Capital_ss"]
        impuesto,salario,G,L,L_prime=guess["Impuesto_ss"],guess["Salario_ss"],guess["Gobierno_ss"],guess["Trabajo_ss"],guess["Trabajo_ss"]
        #Ec_Euler
        res_ec_euler= res_Ec_Euler(obj_utilidad,C,C_prime,L,L_prime,beta,tasa_interes)
        #Oferta_laboral
        res_of_lab =res_oferta_laboral(obj_utilidad,C,L,impuesto,salario)
        # Restriccion del individuo
        resi_rest_indv=  res_rest_indv(K_prime,C,impuesto,salario,L,tasa_interes,K)
        # Prd. mg del capital
        res_prd_mg_k=prod_mg_capital(obj_produccion,A_ss,K,L,tasa_interes,delta)
        #prd_mg del capital
        res_prd_mg_l=prod_mg_trabajo(obj_produccion,A_ss,K,L,salario)
        # Balance de gobierno
        res_bal_gob = bal_gobierno(G,impuesto,salario,L)
        #Vaciamiento de mercado
        res_vac_mer=res_vac_mercado(obj_produccion,A_ss,C,G,K_prime,delta,K,L)
        #Shock de Gobierno
        res_shock_gob=shock_gobierno_ss(obj_produccion,G,A_ss,K,L,g_bar)
        # Computamos el vector de residuos
        return np.array([res_ec_euler,res_of_lab,resi_rest_indv,res_prd_mg_k,res_prd_mg_l,res_bal_gob,res_vac_mer,res_shock_gob])