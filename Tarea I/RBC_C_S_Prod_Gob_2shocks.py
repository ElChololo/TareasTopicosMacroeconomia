from Funciones_Utilidad import Funciones_Utilidad

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
            self.__parametros[key] = parametros[key]
            if key in ["sigma","psi","phi"]:
                self.__parametros_utilidad[key] =parametros[key]

        # Construimos un objeto que guardara el valor de la utilidad y sus derivadas
        self.__obj_utilidad = Funciones_Utilidad(utilidad,**self.__parametros_utilidad)

        # Construismos un objeto que guardara el valor de la produccion y sus utilidades
        if utilidad == "Trabajo Inelastico":
            self.__obj_produccion = Funcion_Produccion(self.__parametros["alpha"])
            self.__trabajo= False
        else:
            self.__obj_produccion = Funcion_Produccion(self.__parametros["alpha"],flag=False)
            self.__trabajo= True

    def estado_estacionario(self,guess_inicial={"Consumo_ss":1,"Capital_ss":1,"Trabajo_ss":1,"Tasa_Interes_ss":1,"Impuesto_ss":1, "Salario_ss":1, "Gobierno_ss":1}):
        ''' Este metodo se encargará de resolver el estado estacionario del modelo. Será generalizado, por lo que para 
        cualquier forma funcional de la utilidad, deberá encontrar el estado estacionario. Utilizará el método de newton
        para resolver el sistema de ecuaciones'''
        if type(guess_inicial) !=dict:
            raise("Se debe entregar un diccionario con los valores iniciales para computar el estado estacionario")
        if self.__trabajo == False:
            # en este mundo habrán 7 ecuaciones y 7 incógnitas, lo primero será armaslas. Para ello necesitamos un guess inicial


            
            #En este caso, no necesitamos Trabajo en EE:
            guess_inicial.pop("Trabajo_ss","No hay trabajo EE")
            # Con estos guess debemos armar los valores que toman las ecuaciones del modelo del tipo F(x) = 0
            valores_res = Residuos_Ecuaciones_SS(self.__obj_utilidad,self.__obj_produccion,self.__parametros,guess_inicial,self.__trabajo)
            # Ahora computamos el jacobiano de la expresión
            jacobiano = Jacobiano_Newton(self.__obj_utilidad,self.__obj_produccion,self.__parametros,guess_inicial,self.__trabajo)
            array_guess = np.array(list(guess_inicial.values()))
            #Realizamos el metodo de newton
            guess_up = array_guess + np.linalg.inv(jacobiano) @ valores_res

            # debiese converger en 1 sola iteración para el caso sin trabajo
            return guess_up
