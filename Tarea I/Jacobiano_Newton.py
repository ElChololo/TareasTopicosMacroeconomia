from Residuos_Ecuaciones import *
def Jacobiano_Newton(obj_utilidad,obj_produccion,parametros,guess,trabajo):
    # Debemos calcular las derivadas de cada ecuacion
    # Debemos respetar un orden, para el caso sin trabajo será:
    # C,K,R,Impuesto,W,G
    #Ec euler
    delta_x=1e-6
    A_ss=1
    beta,delta,g_bar = parametros["beta"],parametros["delta"],parametros["g_bar"]
    C,C_prime,tasa_interes,K_prime,K = guess["Consumo_ss"],guess["Consumo_ss"],guess["Tasa_Interes_ss"],guess["Capital_ss"],guess["Capital_ss"]
    impuesto,salario,G = guess["Impuesto_ss"],guess["Salario_ss"],guess["Gobierno_ss"]
    if trabajo==False:
        trabajo=1
        jac_ec_euler=  [(res_Ec_Euler(obj_utilidad,C+delta_x,C+delta_x,trabajo,trabajo,beta,tasa_interes)- res_Ec_Euler(obj_utilidad,C,C_prime,trabajo,trabajo,beta,tasa_interes)) / delta_x,
                        0,
                        (res_Ec_Euler(obj_utilidad,C,C_prime,trabajo,trabajo,beta,tasa_interes+delta_x)- res_Ec_Euler(obj_utilidad,C,C_prime,trabajo,trabajo,beta,tasa_interes)) / delta_x,
                        0,
                        0,
                        0]
        jac_rest_ind = [(res_rest_indv(K_prime,C+delta_x,impuesto,salario,trabajo,tasa_interes,K)-res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K) )/delta_x,
                        (res_rest_indv(K_prime+delta_x,C,impuesto,salario,trabajo,tasa_interes,K+delta_x)-res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K) )/delta_x,
                        (res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes+delta_x,K)-res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K) )/delta_x,
                        (res_rest_indv(K_prime,C,impuesto+delta_x,salario,trabajo,tasa_interes,K)-res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K) )/delta_x,
                        (res_rest_indv(K_prime,C,impuesto,salario+delta_x,trabajo,tasa_interes,K)-res_rest_indv(K_prime,C,impuesto,salario,trabajo,tasa_interes,K) )/delta_x,
                        0
                        ]
        
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
                    (bal_gobierno(G,impuesto,salario+delta_x,trabajo)- bal_gobierno(G,impuesto,salario,trabajo) ) / delta_x,
                    (bal_gobierno(G+delta_x,impuesto,salario,trabajo)- bal_gobierno(G,impuesto,salario,trabajo) ) / delta_x
                    
        ]

        jac_vac_mer= [ (res_vac_mercado(obj_produccion,A_ss,C+delta_x,G,K_prime,delta,K,trabajo) - res_vac_mercado(obj_produccion,A_ss,C,G,K_prime,delta,K,trabajo) ) /delta_x,
                    (res_vac_mercado(obj_produccion,A_ss,C,G,K_prime+delta_x,delta,K+delta_x,trabajo) - res_vac_mercado(obj_produccion,A_ss,C,G,K_prime,delta,K,trabajo) ) /delta_x,
                    0,
                    0,
                    0,
                    (res_vac_mercado(obj_produccion,A_ss,C,G+delta_x,K_prime,delta,K,trabajo) - res_vac_mercado(obj_produccion,A_ss,C,G,K_prime,delta,K,trabajo) ) /delta_x
        ]
        jac_shock_gob= [ 0,
                        (shock_gobierno_ss(obj_produccion,G,A_ss,K+delta_x,trabajo,g_bar) -shock_gobierno_ss(obj_produccion,G,A_ss,K,trabajo,g_bar)) / delta_x,
                        0,
                        0,
                        0,
                        ( shock_gobierno_ss(obj_produccion,G+delta_x,A_ss,K,trabajo,g_bar) - shock_gobierno_ss(obj_produccion,G,A_ss,K,trabajo,g_bar)) / delta_x
        ]

        #Creamos una matriz donde cada fila representa las derivadas
        jacobiano=np.array([jac_ec_euler,jac_rest_ind,jac_prd_mg_K,jac_bal_gob,jac_vac_mer,jac_shock_gob])
        return jacobiano
    else:
        #Convención de orden de la matriz guess_inicial: C,K,L,r,t,W,G
        L,L_prime=guess["Trabajo_ss"],guess["Trabajo_ss"]
        jac_ec_euler=[(res_Ec_Euler(obj_utilidad,C+delta_x,C_prime+delta_x,L,L_prime,beta,tasa_interes) - res_Ec_Euler(obj_utilidad,C,C_prime,L,L_prime,beta,tasa_interes) )/ delta_x,
                      0,
                      (res_Ec_Euler(obj_utilidad,C,C_prime,L+delta_x,L_prime+delta_x,beta,tasa_interes) - res_Ec_Euler(obj_utilidad,C,C_prime,L,L_prime,beta,tasa_interes) )/ delta_x,
                    (res_Ec_Euler(obj_utilidad,C,C_prime,L,L_prime,beta,tasa_interes+delta_x) - res_Ec_Euler(obj_utilidad,C,C_prime,L,L_prime,beta,tasa_interes) )/ delta_x,
                    0,
                    0,
                    0
        ]
        jac_ec_oferta_laboral=[(res_oferta_laboral(obj_utilidad,C+delta_x,L,impuesto,salario) - res_oferta_laboral(obj_utilidad,C,L,impuesto,salario)) / delta_x,
                               0,
                               (res_oferta_laboral(obj_utilidad,C,L+delta_x,impuesto,salario) - res_oferta_laboral(obj_utilidad,C,L,impuesto,salario)) / delta_x,
                               0,
                               (res_oferta_laboral(obj_utilidad,C,L,impuesto+delta_x,salario) - res_oferta_laboral(obj_utilidad,C,L,impuesto,salario)) / delta_x,
                               (res_oferta_laboral(obj_utilidad,C,L,impuesto,salario+delta_x) - res_oferta_laboral(obj_utilidad,C,L,impuesto,salario)) / delta_x,
                               0
        ]
        jac_rest_ind=[(res_rest_indv(K_prime,C+delta_x,impuesto,salario,L,tasa_interes,K)  - res_rest_indv(K_prime,C,impuesto,salario,L,tasa_interes,K)) / delta_x,
                     (res_rest_indv(K_prime+delta_x,C,impuesto,salario,L,tasa_interes,K+delta_x)  - res_rest_indv(K_prime,C,impuesto,salario,L,tasa_interes,K)) / delta_x,
                     (res_rest_indv(K_prime,C,impuesto,salario,L+delta_x,tasa_interes,K)  - res_rest_indv(K_prime,C,impuesto,salario,L,tasa_interes,K)) / delta_x,
                     (res_rest_indv(K_prime,C,impuesto,salario,L,tasa_interes+delta_x,K)  - res_rest_indv(K_prime,C,impuesto,salario,L,tasa_interes,K)) / delta_x,
                     (res_rest_indv(K_prime,C,impuesto+delta_x,salario,L,tasa_interes,K)  - res_rest_indv(K_prime,C,impuesto,salario,L,tasa_interes,K)) / delta_x,
                     (res_rest_indv(K_prime,C,impuesto,salario+delta_x,L,tasa_interes,K)  - res_rest_indv(K_prime,C,impuesto,salario,L,tasa_interes,K)) / delta_x,
                     0


        ]   
        jac_prd_mg_K=[0,
                      (prod_mg_capital(obj_produccion,A_ss,K+delta_x,L,tasa_interes,delta)-prod_mg_capital(obj_produccion,A_ss,K,L,tasa_interes,delta)) / delta_x,
                      (prod_mg_capital(obj_produccion,A_ss,K,L+delta_x,tasa_interes,delta)-prod_mg_capital(obj_produccion,A_ss,K,L,tasa_interes,delta)) / delta_x,
                      (prod_mg_capital(obj_produccion,A_ss,K,L,tasa_interes+delta_x,delta)-prod_mg_capital(obj_produccion,A_ss,K,L,tasa_interes,delta)) / delta_x,
                      0,
                      0,
                      0

        ] 
        jac_prd_mg_L=[0,
                      (prod_mg_trabajo(obj_produccion,A_ss,K+delta_x,L,salario) - prod_mg_trabajo(obj_produccion,A_ss,K,L,salario)) / delta_x,
                      (prod_mg_trabajo(obj_produccion,A_ss,K,L+delta_x,salario) - prod_mg_trabajo(obj_produccion,A_ss,K,L,salario)) / delta_x,
                      0,
                      0,
                      (prod_mg_trabajo(obj_produccion,A_ss,K,L,salario+delta_x) - prod_mg_trabajo(obj_produccion,A_ss,K,L,salario)) / delta_x,
                      0

        ]
        jac_bal_gob=[0,
                     0,
                     (bal_gobierno(G,impuesto,salario,L+delta_x) - bal_gobierno(G,impuesto,salario,L)) / delta_x,
                     0,
                     (bal_gobierno(G,impuesto+delta_x,salario,L) - bal_gobierno(G,impuesto,salario,L)) / delta_x,
                     (bal_gobierno(G,impuesto,salario+delta_x,L) - bal_gobierno(G,impuesto,salario,L)) / delta_x,
                     (bal_gobierno(G+delta_x,impuesto,salario,L) - bal_gobierno(G,impuesto,salario,L)) / delta_x

        ]
        jac_vac_mer=[(res_vac_mercado(obj_produccion,A_ss,C+delta_x,G,K_prime,delta,K,L) - res_vac_mercado(obj_produccion,A_ss,C,G,K_prime,delta,K,L)) / delta_x,
                     (res_vac_mercado(obj_produccion,A_ss,C,G,K_prime+delta_x,delta,K+delta_x,L) - res_vac_mercado(obj_produccion,A_ss,C,G,K_prime,delta,K,L)) / delta_x,
                     (res_vac_mercado(obj_produccion,A_ss,C,G,K_prime,delta,K,L+delta_x) - res_vac_mercado(obj_produccion,A_ss,C,G,K_prime,delta,K,L)) / delta_x,
                     0,
                     0,
                     0,
                     (res_vac_mercado(obj_produccion,A_ss,C,G+delta_x,K_prime,delta,K,L) - res_vac_mercado(obj_produccion,A_ss,C,G,K_prime,delta,K,L)) / delta_x

        ]
        jac_shock_gob=[0,
                        (shock_gobierno_ss(obj_produccion,G,A_ss,K+delta_x,L,g_bar)-shock_gobierno_ss(obj_produccion,G,A_ss,K,L,g_bar)) / delta_x,
                       (shock_gobierno_ss(obj_produccion,G,A_ss,K,L+delta_x,g_bar)-shock_gobierno_ss(obj_produccion,G,A_ss,K,L,g_bar)) / delta_x,
                       0,
                       0,
                       0,
                       (shock_gobierno_ss(obj_produccion,G+delta_x,A_ss,K,L,g_bar)-shock_gobierno_ss(obj_produccion,G,A_ss,K,L,g_bar)) / delta_x

        ]
        jacobiano=np.array([jac_ec_euler,jac_ec_oferta_laboral,jac_rest_ind,jac_prd_mg_K,jac_prd_mg_L,jac_bal_gob,jac_vac_mer,jac_shock_gob])
        return jacobiano