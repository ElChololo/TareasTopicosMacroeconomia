import numpy as np

def res_Ec_Euler(obj_utilidad,C,C_prime,beta,tasa_interes):
    valor = obj_utilidad.derivada_c(obj_utilidad,C) - beta*obj_utilidad.derivada_c(obj_utilidad,C_prime)*tasa_interes
    return valor

def res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K):
    valor = K_prime+C-(1-impuesto)*salario*trabajo+tasa_interes*K
    return valor

def prod_mg_capital(obj_produccion,A,K,L,tasa_interes,delta):
    valor= obj_produccion.derivada_k(obj_produccion,A,K,L)-tasa_interes-delta
    return valor

def prod_mg_trabajo(obj_produccion,A,K,L,salario):
    valor= obj_produccion.derivada_l(A,K,L) - salario
    return valor

def bal_gobierno(G,impuesto,salario,L):
    valor= G-impuesto*salario*L
    return valor
def res_vac_mercado(obj_produccion,A,C,G,K_prime,delta,K,L):
    valor=obj_produccion.get_valor(obj_produccion,A,K,L) - C- G- +K_prime - (1-delta)*K
    return valor
def shock_gobierno(obj_produccion,A,K,L,G,ro_g,g_bar,G_rez,sigma_g,epsilon_g):
    valor= np.log(G)-(1-ro_g)*np.log(g_bar*obj_produccion.valor(obj_produccion,A,K,L))+ro_g*np.log(G_rez)+sigma_g*epsilon_g
    return valor
def shock_gobierno_ss(obj_produccion,G_ss,A_ss,K_ss,L_ss,g_bar):
    valor = G_ss - g_bar*obj_produccion.get_valor(obj_produccion,A_ss,K_ss,L_ss)
    return valor