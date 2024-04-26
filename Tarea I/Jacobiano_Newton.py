from Residuos_Ecuaciones import *
def Jacobiano_Newton()
    # Debemos calcular las derivadas de cada ecuacion
    # Debemos respetar un orden, para el caso sin trabajo será:
    # C,K,R,Impuesto,G,W,
    #Ec euler
    delta_x=10**(-8)
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
                  (prod_mg_capital(obj_produccion,K,tasa_interes,delta)- prod_mg_capital(obj_produccion,K,tasa_interes,delta) ) / delta_x,
                  (prod_mg_capital(obj_produccion,K,tasa_interes,delta)- prod_mg_capital(obj_produccion,K,tasa_interes,delta) ) / delta_x,
                  0,
                  0,
                  0]
                  
    jac_bal_gob= [ 0,
                  0,
                  0,
                  (bal_gobierno(G,impuesto+delta_x,salario,L)- bal_gobierno(G,impuesto,salario,L) ) / delta_x,
                  (bal_gobierno(G+delta_x,impuesto,salario,L)- bal_gobierno(G,impuesto,salario,L) ) / delta_x,
                  (bal_gobierno(G,impuesto,salario+delta_x,L)- bal_gobierno(G,impuesto,salario,L) ) / delta_x

    ]

    jac_vac_mer= [ (res_vac_mercado(obj_produccion,C+delta_x,G,K_prime,delta,K) - res_vac_mercado(obj_produccion,C,G,K_prime,delta,K) ) /delta_x,
                  0,
                  (res_vac_mercado(obj_produccion,C,G,K_prime+delta_x,delta,K+delta_x) - res_vac_mercado(obj_produccion,C,G,K_prime,delta,K) ) /delta_x,
                  0,
                  0,
                  0,
                  0
    ]

    jac_shock_gob= [ 0,
                    ( shock_gobierno(G,ro_g,g_bar,Y,G_rez,sigma_g,epsilon_g) - shock_gobierno(G,ro_g,g_bar,Y,G_rez,sigma_g,epsilon_g)) / delta_x,
                    0,
                    0
                    ( shock_gobierno(G+delta_x,ro_g,g_bar,Y,G_rez,sigma_g,epsilon_g) - shock_gobierno(G,ro_g,g_bar,Y,G_rez,sigma_g,epsilon_g)) / delta_x,
                    0
    ]

    #Creamos una matriz donde cada fila representa las derivadas
    jacobiano=np.array([[jac_ec_euler],
                        [jac_rest_ind],
                        [jac_prd_mg_K],
                        [jac_bal_gob],
                        [jac_vac_mer],
                        [jac_shock_gob]])
    return jacobiano