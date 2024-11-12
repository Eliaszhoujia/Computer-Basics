#Declaración de variables
C = float(input("Cantidad prestada"))

#Tipo de interés
while True:
    t_i = input("¿Qué tipo de interés quiere aplicar (Simple/Compuesto)?")
    if t_i == "Simple":
        i = float(input("Tasa de interés"))
        ta = float(input("Tiempo en años"))
        def i_s():
            return i/100 * C * ta + C
        Vf = i_s() 
        print("El valor final es", round(Vf, 2))
        break
    elif t_i == "Compuesto":
        i = float(input("Tasa de interés"))
        ta = float(input("Tiempo en años"))
        def i_c():
            return (i/100 + 1) ** ta * C
        Vf = i_c()
        print("El valor final es", (round(Vf, 2)))
        break
    else:
        print("Por favor, ingrese 'Simple' o 'Compuesto' como tipo de interés")
    
