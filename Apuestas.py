import random as rd

print("---Bienvenido a CHO HAN---")
print("Usted empieza jugando con 10$ en su billetera")
billetera = 10
gana = 0
apuesta = int(input("Ingrese apuesta: "))

while apuesta > billetera:
    print("La cantidad ingresada es mayor a su saldo")
    apuesta = int(input("Ingrese apuesta: "))
while apuesta <= billetera:
    respuesta = input("Adivine, par o impar??: ")
    dado1 = rd.randint(1,6)
    dado2 = rd.randint(1,6)
    total = dado1 + dado2
    resto = total % 2
    print("Salio " +str(total))
    if resto == 0 and respuesta == "par":
        print("Ronda ganada!")
        billetera+=apuesta
        print("Este es su saldo actual " +str(billetera) + "$!")
        gana+=1
    elif resto != 0 and respuesta == "impar":
        print("Ronda ganada!")
        billetera+=apuesta
        print("Este es su saldo actual " +str(billetera) + "$!")
    
        gana+=1
    
    else:
        print("Ronda perdida!")
        billetera-=apuesta
        print("Este es su saldo actual " + str(billetera) + "$!")
    if billetera == 0:
        print("El juego ha terminado, te has quedado sin saldo!")
        break
    
    
    continuar = input("Desea seguir jugando?(Si/No): ")
    if continuar == "no":
        print("Ganaste " +str(gana) + " partida(s) y tu saldo fue de " +str(billetera) + "$!")
        print("Gracias por participar!")
        
        break
    else:
        apuesta = int(input("Ingrese apuesta: "))