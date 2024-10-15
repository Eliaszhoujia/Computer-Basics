m = float (input("Introduce the Kg for the operation"))
v = float (input("Introduce the velocity in m/s for the operation"))
def energía_cinética():
    return  1/2 * m * v ** 2
resultado = energía_cinética()
print("The kinetic energy is:"+ str(resultado) + "J" )