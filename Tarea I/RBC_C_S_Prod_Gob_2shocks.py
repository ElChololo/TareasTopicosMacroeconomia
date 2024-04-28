from Obj_Funciones_Utilidad import *

from Funciones_produccion import Funcion_Produccion

from Residuos_Ecuaciones import Residuos_Ecuaciones_SS

from Jacobiano_Newton import *

import numpy as np
class RBC_C_S_K_Prod_Gob_2shocks:
    def __init__(self,parametros,utilidad="Trabajo Inelastico"):
        if type(parametros)!=dict:
            raise("Para inicializar la clase, se deben entregar los parámetros en un diccionario")
        # Almacenamos los parametros del modelo
        self.__parametros={}
        self.__parametros_utilidad={}
        for key in parametros.keys():
            # Filtramos los parametros de utilidad de los parametros del modelo
            if key in ["sigma","psi","phi"]:
                self.__parametros_utilidad[key] =parametros[key]
            else:
                self.__parametros[key] = parametros[key]
        self.__tipo_utilidad=utilidad
        # Construimos un objeto que guardara el valor de la utilidad y sus derivadas, dependiendo del tipo de utilidad
        if utilidad=="Trabajo Inelastico":
            self.__obj_utilidad= Trabajo_Inelastico(self.__parametros_utilidad["sigma"])
        elif utilidad=="CRRA separable":
            self.__obj_utilidad= CRRA_separable(self.__parametros_utilidad["sigma"],self.__parametros_utilidad["phi"],self.__parametros_utilidad["psi"])
        elif utilidad== "GHH nonseparable":
            self.__obj_utilidad =GHH_nonseparable(self.__parametros_utilidad["sigma"],self.__parametros_utilidad["phi"],self.__parametros_utilidad["psi"])
        # Creamos un objeto para almacenar la función de producción
        self.__obj_produccion=Funcion_Produccion(self.__parametros["alpha"])

    def estado_estacionario(self,guess_inicial={"Consumo_ss":1,"Capital_ss":1,"Trabajo_ss":1,"Tasa_Interes_ss":1,"Impuesto_ss":1, "Salario_ss":1, "Gobierno_ss":1}):
        ''' Este metodo se encargará de resolver el estado estacionario del modelo. Será generalizado, por lo que para 
        cualquier forma funcional de la utilidad, deberá encontrar el estado estacionario. Utilizará el método de newton
        para resolver el sistema de ecuaciones'''
        if type(guess_inicial) !=dict:
            raise("Se debe entregar un diccionario con los valores iniciales para computar el estado estacionario")
        
        # Cuando la función de utilidad es con trabajo inelástico, cambia el número de ecuaciones del modelo
        if self.__tipo_utilidad=="Trabajo Inelastico":
            self.__trabajo=False
        else:
            self.__trabajo=True
       
        
        if self.__trabajo == False:
            #Implementamos el algoritmo de newton, para ello, necesito la primera iteración
            #Convención de orden de la matriz guess_inicial: C,K,r,t,W,G

            # Dado el guess debemos armar los valores que toman las ecuaciones del modelo del tipo F(x) = 0
            valores_res = Residuos_Ecuaciones_SS(self.__obj_utilidad,self.__obj_produccion,self.__parametros,guess_inicial,self.__trabajo)
            # Ahora computamos el jacobiano de la expresión
            jacobiano = Jacobiano_Newton(self.__obj_utilidad,self.__obj_produccion,self.__parametros,guess_inicial,self.__trabajo)
            #Botamos el trabajo
            guess_inicial.pop("Trabajo_ss","No hay trabajo en el guess inicial")
            # Armo el guess inicial como array
            array_guess = np.array(list(guess_inicial.values()))
            print("Iteración 0\n")
            print(array_guess)
            # Realizo el paso del algoritmo
            guess_up = array_guess - np.linalg.inv(jacobiano) @ valores_res
            print(guess_up)
            # Este será mi nuevo guess,debo armarlo como diccionario:
            guess_inicial={"Consumo_ss":guess_up[0],"Capital_ss":guess_up[1],"Trabajo_ss":1,"Tasa_Interes_ss":guess_up[2],"Impuesto_ss":guess_up[3], "Salario_ss":guess_up[4], "Gobierno_ss":guess_up[5]}
            #ahora debo imponer la restriccion de convergencia
            
            iteracion=0
            while np.abs(np.linalg.norm(array_guess)-np.linalg.norm(guess_up))>1e-6:
                valores_res = Residuos_Ecuaciones_SS(self.__obj_utilidad,self.__obj_produccion,self.__parametros,guess_inicial,self.__trabajo)
                jacobiano = Jacobiano_Newton(self.__obj_utilidad,self.__obj_produccion,self.__parametros,guess_inicial,self.__trabajo)
                guess_inicial.pop("Trabajo_ss","No hay trabajo en el guess inicial")
                array_guess = np.array(list(guess_inicial.values()))
                guess_up = array_guess - np.linalg.inv(jacobiano) @ valores_res
                guess_inicial={"Consumo_ss":guess_up[0],"Capital_ss":guess_up[1],"Trabajo_ss":1,"Tasa_Interes_ss":guess_up[2],"Impuesto_ss":guess_up[3], "Salario_ss":guess_up[4], "Gobierno_ss":guess_up[5]}
                iteracion+=1
                print("Iteracion: {}\n".format(iteracion))
                print(array_guess)
                print(guess_up)
                if iteracion >1000:
                    break
            return guess_up
        else:
            #Convención de orden de la matriz guess_inicial: C,K,L,r,t,W,G
            ## Caso de las funciones utilidad con trabajo
            valores_res = Residuos_Ecuaciones_SS(self.__obj_utilidad,self.__obj_produccion,self.__parametros,guess_inicial,self.__trabajo)
            # Ahora computamos el jacobiano de la expresión
            jacobiano = Jacobiano_Newton(self.__obj_utilidad,self.__obj_produccion,self.__parametros,guess_inicial,self.__trabajo)
            # Armo el guess inicial como array
            array_guess = np.array(list(guess_inicial.values()))
            print("Iteración 0\n")
            print(array_guess)
            # Realizo el paso del algoritmo
            guess_up = array_guess - np.linalg.inv(jacobiano) @ valores_res
            # Este será mi nuevo guess,debo armarlo como diccionario:
            guess_inicial={"Consumo_ss":guess_up[0],"Capital_ss":guess_up[1],"Trabajo_ss":guess_up[2],"Tasa_Interes_ss":guess_up[3],"Impuesto_ss":guess_up[4], "Salario_ss":guess_up[5], "Gobierno_ss":guess_up[6]}
            #ahora debo imponer la restriccion de convergencia
            print(guess_up)
            iteracion=0
            while np.abs(np.linalg.norm(array_guess)-np.linalg.norm(guess_up))>1e-2:

                valores_res = Residuos_Ecuaciones_SS(self.__obj_utilidad,self.__obj_produccion,self.__parametros,guess_inicial,self.__trabajo)
                jacobiano = Jacobiano_Newton(self.__obj_utilidad,self.__obj_produccion,self.__parametros,guess_inicial,self.__trabajo)
                array_guess = np.array(list(guess_inicial.values()))
                guess_up = array_guess - np.linalg.inv(jacobiano) @ valores_res
                guess_inicial={"Consumo_ss":guess_up[0],"Capital_ss":guess_up[1],"Trabajo_ss":1,"Tasa_Interes_ss":guess_up[2],"Impuesto_ss":guess_up[3], "Salario_ss":guess_up[4], "Gobierno_ss":guess_up[5]}
                iteracion+=1
                print("Iteracion: {}\n".format(iteracion))
                print(array_guess)
                print(guess_up)
                if iteracion >1000:
                    break
            return guess_up