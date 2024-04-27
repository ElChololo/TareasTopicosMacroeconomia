# Definimos los parámetros del modelo
from RBC_C_S_Prod_Gob_2shocks import *
parametros={"alpha":0.3,"beta":0.96,"sigma":2,"phi":1,"psi":1,"delta":0.01,"ro_a":0.75,"ro_g":0.75,"g_bar":0.2,"sigma_prd":1,"sigma_g":1}

## Creamos los objetos que contienen los modelos con las 3 funciones de utilidad
modelo_inelastic_labor=RBC_C_S_K_Prod_Gob_2shocks(parametros)

## Obtenemos los estados estacionarios
modelo_inelastic_labor.estado_estacionario()
