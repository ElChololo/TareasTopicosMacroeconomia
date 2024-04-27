from Residuos_Ecuaciones import *
def Jacobiano_Newton(obj_utilidad,obj_produccion,parametros,guess,trabajo):
    # Debemos calcular las derivadas de cada ecuacion
    # Debemos respetar un orden, para el caso sin trabajo será:
    # C,K,R,Impuesto,G,W,
    #Ec euler
    delta_x=10**(-8)
    if trabajo==False:
        alpha,beta,sigma,delta,g_bar = parametros["alpha"],parametros["beta"],parametros["sigma"],parametros["delta"],parametros["g_bar"]
        C,C_prime,tasa_interes,K_prime,K = guess["Consumo_ss"],guess["Consumo_ss"],guess["Tasa_Interes_ss"],guess["Capital_ss"],guess["Capital_ss"]
        impuesto,salario,G,trabajo=guess["Impuesto_ss"],guess["Salario_ss"],guess["Gobierno_ss"],1
        A_ss=1
        jac_ec_euler=  [(res_Ec_Euler(obj_utilidad,C+delta_x,C+delta_x,beta,tasa_interes)- res_Ec_Euler(obj_utilidad,C,C_prime,beta,tasa_interes)) / delta_x,
                        0,
                        (res_Ec_Euler(obj_utilidad,C,C_prime,beta,tasa_interes+delta_x)- res_Ec_Euler(obj_utilidad,C,C_prime,beta,tasa_interes)) / delta_x,
                        0,0,0]
        jac_rest_ind = [(res_rest_indv(K_prime,C+delta_x,impuesto,salario,trabajo,tasa_interes,K)-res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K) )/delta_x,
                        (res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K+delta_x)-res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K) )/delta_x,
                        (res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes+delta_x,K)-res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K) )/delta_x,
                        (res_rest_indv(K_prime,C,impuesto+delta_x,salario,trabajo,tasa_interes,K)-res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K) )/delta_x,
                        0,
                        (res_rest_indv(K_prime,C,impuesto,salario+delta_x,trabajo,tasa_interes,K)-res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K) )/delta_x]
        
        jac_prd_mg_K=[ 0,
                    (prod_mg_capital(obj_produccion,A_ss,K+delta_x,trabajo,tasa_interes,delta)- prod_mg_capital(obj_produccion,A_ss,K,trabajo,tasa_interes,delta) ) / delta_x,
                    (prod_mg_capital(obj_produccion,A_ss,K,trabajo,tasa_interes+delta_x,delta)- prod_mg_capital(obj_produccion,A_ss,K,trabajo,tasa_interes,delta) ) / delta_x,
                    0,
                    0,
                    0]
                    
        jac_bal_gob= [ 0,
                    0,
                    0,
                    (bal_gobierno(G,impuesto+delta_x,salario,trabajo)- bal_gobierno(G,impuesto,salario,trabajo) ) / delta_x,
                    (bal_gobierno(G+delta_x,impuesto,salario,trabajo)- bal_gobierno(G,impuesto,salario,trabajo) ) / delta_x,
                    (bal_gobierno(G,impuesto,salario+delta_x,trabajo)- bal_gobierno(G,impuesto,salario,trabajo) ) / delta_x

        ]

        jac_vac_mer= [ (res_vac_mercado(obj_produccion,A_ss,C+delta_x,G,K_prime,delta,K,trabajo) - res_vac_mercado(obj_produccion,A_ss,C,G,K_prime,delta,K,trabajo) ) /delta_x,
                    0,
                    (res_vac_mercado(obj_produccion,A_ss,C,G,K_prime+delta_x,delta,K+delta_x,trabajo) - res_vac_mercado(obj_produccion,A_ss,C,G,K_prime,delta,K,trabajo) ) /delta_x,
                    0,
                    0,
                    0
        ]
        jac_shock_gob= [ 0,
                        (shock_gobierno_ss(obj_produccion,G,A_ss,K+delta_x,trabajo,g_bar) -shock_gobierno_ss(obj_produccion,G,A_ss,K,trabajo,g_bar)) / delta_x,
                        0,
                        0,
                        ( shock_gobierno_ss(obj_produccion,G+delta_x,A_ss,K,trabajo,g_bar) - shock_gobierno_ss(obj_produccion,G,A_ss,K,trabajo,g_bar)) / delta_x,
                        0
        ]

        #Creamos una matriz donde cada fila representa las derivadas
        jacobiano=np.array([jac_ec_euler,jac_rest_ind,jac_prd_mg_K,jac_bal_gob,jac_vac_mer,jac_shock_gob])
        return jacobiano