U = str (input("Do you want to convert celsius or farenheit?"))
T = float (input ("Temperature"))
resultado = 0
def conversor():
    if U == "celsius":
        resultado = T  *9/5+32
        print("The temperature is" + float(resultado)+"Fº")
    else: 
        resultado = T*5/9-32
        print("The temperature is" + float(resultado)+"Cº")
conversor()


