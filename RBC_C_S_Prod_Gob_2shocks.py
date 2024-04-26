from Funciones_Utilidad import Funciones_Utilidad

from Funcion_Produccion import Funcion_Produccion

class RBC_C_S_K_Prod_Gob_2shocks:
    def __init__(self,parametros,utilidad="Trabajo Inelastico"):
        if type(parametros)!=dict:
            raise("Para inicializar la clase, se deben entregar los parámetros en un diccionario")
        # Almacenamos los parametros del modelo
        self.__parametros={}
        for key in parametros.key():
            self.__parametros[key] = parametros[key]
            if key in ["sigma","psi","phi"]:
                self.__parametros_utilidad[key] =parametros[key]

        # Construimos un objeto que guardara el valor de la utilidad y sus derivadas
        self.__obj_utilidad = Funciones_Utilidad(utilidad,self.__parametros_utilidad)

        # Construismos un objeto que guardara el valor de la produccion y sus utilidades
        if utilidad == "Trabajo Inelastico":
            self.__obj_produccion = Funcion_Produccion(self.__parametros["alpha"])
            self.__trabajo= False
        else:
            self.__obj_produccion = Funcion_Produccion(self.__parametros["alpha"],flag=False)
            self.__trabajo= True

    def estado_estacionario(self):
        # Este metodo se encargará de resolver el estado estacionario del modelo. Será generalizado, por lo que para 
        # cualquier forma funcional de la utilidad, deberá encontrar el estado estacionario. Utilizará el método de newton
        # para resolver el sistema de ecuaciones
       if self.__trabajo = False:
            # en este mundo habrán 7 ecuaciones y 7 incógnitas, lo primero será armaslas. Para ello necesitamos un guess inicial
            # Ahora bien, sabemos que en estado estacionario, el valor de la productividad estára en su media incondicional
            # Para esta tarea, la forma funcional es fija y da como resultado una media incondicional de 1
            A_ss=1
            
            guess ={"Consumo_ss":1,"Capital_ss":1,"Tasa_Interes_ss":1,"Impuesto_ss":1, "Salario":1, "Gobierno":1}
            # Con estos guess debemos armar los valores que toman las ecuaciones del modelo del tipo F(x) = 0
