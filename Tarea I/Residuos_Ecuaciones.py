def Residuos_Ecuaciones_SS(obj_utilidad,obj_producion,parametros,guess, Flag_trabajo=False):
    if type(parametros)!= dict or type(guess) != dict:
        raise("Tanto los parametros como los guess inicial deben ser entregados como diccionarios")
    
    # Sin trabajo el sistema tiene 6 ecuaciones (Productivdad de EE es 1 dado la forma funcional):
    if Flag_trabajo=False:
        #Ecuacion de euler (debo cambiar porque la derivada de c a veces depende solo de C y otras tambien de L)
        obj_utilidad.derivada_c(guess["Consumo_ss"]) = parametros["Beta"]* guess["Tasa_Interes_ss"] *obj_utilidad.derivada_c(guess["Consumo"])
        # Restriccion del individuo
        guess["Consumo_ss"]+ guess["Capital_ss"] = (1-guess["Impuesto_ss"])guess["Salario_ss"]+ guess["Tsa_Interes_ss"]*guess["Salario_ss"]
        # Prd. mg del capital
        obj_utilidad.derivada_k() = guess["Tasa_Interes_ss"]- parametros["delta"]
        # Balance de gobierno
        guess["Gobierno_ss"]=guess_["Impuesto_ss"]*guess_["Salario_ss"]
        #Vaciamiento de mercado
        obj_producion.get_valor() = guess["Consumo_ss"] + Guess["Gobierno_ss"]+ parametros["delta"]*guess["Capital_SS"]
        guess["gobierno"] = parametros["g_barra"]* obj_produccion.get_valor()