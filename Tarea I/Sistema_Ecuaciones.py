import numpy as np

def res_Ec_Euler(obj_utilidad,C,C_prime,beta,tasa_interes):
    valor = obj_utilidad.derivada_c(C) - beta*obj_utilidad.derivada_c(C_prime)*tasa_interes
    return valor

def res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K):
    valor = K_prime+C-(1-impuesto)*salario*trabajo+tasa_interes*K
    return valor

def prod_mg_capital(obj_produccion,K,tasa_interes,delta):
    valor= obj_produccion.derivada_k(K)-tasa_interes-delta
    return valor

def prod_mg_trabajo(obj_produccion,L,salario):
    valor= obj_produccion.derivada_l(L) - salario
    return valor

def bal_gobierno(G,impuesto,salario,L):
    valor= G-impuesto*salario*L
    return valor
def res_vac_mercado(obj_produccion,C,G,K_prime,delta,K):
    valor=obj_produccion.get_valor() - C- G- +K_prime - (1-delta)*K
    return valor
def shock_gobierno(G,ro_g,g_bar,Y,G_rez,sigma_g,epsilon_g):
    valor= np.log(G)-(1-ro_g)*np.log(g_bar*Y)+ro_g*np.log(G_rez)+sigma_g*epsilon_g
    return valor