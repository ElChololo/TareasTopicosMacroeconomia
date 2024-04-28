# Definimos los parámetros del modelo
from RBC_C_S_Prod_Gob_2shocks import *
parametros={"alpha":0.3,"beta":0.96,"sigma":2,"phi":1,"psi":1,"delta":0.01,"ro_a":0.75,"ro_g":0.75,"g_bar":0.2,"sigma_prd":1,"sigma_g":1}

## Creamos los objetos que contienen los modelos con las 3 funciones de utilidad
modelo_inelastic_labor=RBC_C_S_K_Prod_Gob_2shocks(parametros)

## Obtenemos los estados estacionarios
#Para el caso de la utilidad con trabajo inelastico sé su EE
R_ss=1/parametros["beta"]
K_ss=((R_ss+1-parametros["delta"])/(parametros["alpha"]))**(1/(parametros["alpha"]-1))
G_ss=parametros["g_bar"]*K_ss**(parametros["alpha"])
C_ss = K_ss**(parametros["alpha"])-G_ss-parametros["delta"]*K_ss
impuesto_ss= G_ss/(C_ss+K_ss*(1-parametros["delta"])+G_ss)
salario_ss=(C_ss+K_ss*(1-parametros["delta"]))/(1-impuesto_ss)
guess_inicial={"Consumo_ss":C_ss,"Capital_ss":K_ss,"Trabajo_ss":1,"Tasa_Interes_ss":R_ss,"Impuesto_ss":impuesto_ss, "Salario_ss":salario_ss, "Gobierno_ss":G_ss}
print("Estado Estacionario",guess_inicial)
guess_aprox={k:v+0.05 for k,v in guess_inicial.items()}
ss=modelo_inelastic_labor.estado_estacionario(guess_aprox)
print(guess_inicial)
print(ss)
## Caso trabajo CRRA
#modelo_CRRA_separable=RBC_C_S_K_Prod_Gob_2shocks(parametros,utilidad="CRRA separable")
# Tambien sé el EE de manera análitica
#R_ss=1/parametros["beta"]
#K_part_L = (1/parametros["beta"] -1 + parametros["delta"]/(parametros["alpha"]))**(1/(parametros["alpha"]-1))
#W_ss= (1-parametros["alpha"])* ((1/parametros["beta"]-1+parametros["delta"])/(parametros["alpha"]))**(parametros["alpha"]/(parametros["alpha"]-1))
#impuesto_ss= (K_part_L**(parametros["alpha"])*parametros["g_bar"] )/W_ss
#C_part_L= K_part_L**(parametros["alpha"]) * (1-parametros["g_bar"]) - parametros["delta"]* K_part_L
#L_ss = (((W_ss*(1-impuesto_ss)+1)/((1-impuesto_ss)*parametros["psi"])) \
#        / \
#        (K_part_L**(parametros["alpha"])* (1-parametros["g_bar"])-parametros["delta"]*K_part_L)) \
#        **(1/(parametros["phi"]+parametros["psi"]))
#C_ss = C_part_L * L_ss
#K_ss = K_part_L * L_ss
#G_ss= parametros["g_bar"]*K_ss**(parametros["alpha"])*L_ss**(1-parametros["alpha"])
#guess_inicial = {"Consumo_ss":C_ss,"Capital_ss":K_ss,"Trabajo_ss":L_ss,"Tasa_Interes_ss":R_ss,"Impuesto_ss":impuesto_ss, "Salario_ss":W_ss, "Gobierno_ss":G_ss}
#modelo_CRRA_separable.estado_estacionario(guess_inicial)