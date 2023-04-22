
print("---------------------------------")
print("-------------EJERCICIO 4---------")
print("---------------------------------")

N = int(input("Digite un numero: "))

Factorial = 1
i = 1

if (N != 0):
    for i in range (1, N+1):
        Factorial = Factorial * i

print("El numero factorial es: " + str(Factorial))
