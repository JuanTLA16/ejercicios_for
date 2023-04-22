print("------------------------------------------")
print("--------------EJERCICIO 1-----------------")
print("------------------------------------------")

N = int(input("Digite un numero entero: "))

Pares = 0
Impares = 0


while (N != 0):

    for i in range (1):

        if ( N % 2 == 0):
           print("El numero es PAR. ")
           Pares = Pares + 1

        else:
            print("El numero es IMPAR. ")
            Impares = Impares + 1


        N = int(input("Digite un numero entero: "))


print("La cantidad de numero PARES en total son: " + str(Pares))
print("La cantidad de numeros IMPARES en total son: " + str(Impares))

