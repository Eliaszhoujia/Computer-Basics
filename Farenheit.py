U = input("Do you want to convert celsius or fahrenheit?")

def celsius_to_fahrenheit(T):
    return T * 1.8 + 32
def fahrenheit_to_celsius(T):
    return (T - 32) / 1.8 

if U == "celsius": 
    T = float (input ("Temperature")) 
    resultado =  celsius_to_fahrenheit(T)
    print("The temperature is " + str (resultado) + " Fº")  
elif U == "fahrenheit":
  T = float (input ("Temperature"))
  resultado =  fahrenheit_to_celsius(T)
  print("The temperature is " + str (resultado) + " Cº")
else:
    resultado = 0
    print("Not the right input")