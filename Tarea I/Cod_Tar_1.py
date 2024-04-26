from math import log10
def Utilidad_derivada_C(X,L):
    return 0

def UtiliUtilidad_derivada_L(C,L):
    return 0

def Pregunta_2(Controles,Controles_rezagados,Controles_futuros,shocks,parametros):
    #Aislamos cada variable
    C,K,L,G,A,tasa_interes,Gobierno,Y = Controles
    epsilon_g,epsilon_a=schocks[0],shocks[1]
    C_rezagado,K_rezagado,A_rezagado,Gobierno_rezagado = Controles_rezagados
    C_futuro,K_futuro,L_futuro,A_rezagado = Controles_futuros
    # Aislamos los parametros
    alpha,beta,delta,ro_g,var_g,ro_a,var_a,g_pib
    # Ecuaciones:

    #Ecuación de Euler
    Res_1=Utilidad_derivada_C(C,L)-beta*Utilidad_derivada_C(C_futuro,L_futuro)
    # Oferta laboral
    Res_2=-1*Utilidad_derivada_C(C,L)*(1-tau)*salario-Utilidad_derivada_L(C,L)
    # Recursos agregados
    Res_3=K_futuros + C - (1-tau)*salario*L-(1+tasa_interes)*K_futuro
    # Uso de Capital
    Res_4=A*alpha*K**(alpha-1)*L**(alpha-)-tasa_interes-delta
    # Uso de trabajo
    Res_5=A*K**(alpha)*(alpha-1)*L**(-1*alpha)-salario
    # Restricción Gobierno
    Gobierno=tau*salario*L
    # Movimiento shocks
    Res_6=log10(Gobierno)-(1-ro_g)*log10(g_pib*Y)-ro_g*log10(Gobierno_rezagado)-var_g*epsilong_g
    Res_7= log10(A) -ro_a*log10(A_rezagado)+var_a*epsilon_a
    #Consumo Agregado
    Res_8=Y-C-G-K_futuro+(1-delta)*K
    return np.hstack(Res_1,Res_2,Res_3,Res_4,Res_5,Res_6,Res_7,Res_8)
    