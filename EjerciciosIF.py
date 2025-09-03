#Miguel Galindo


#Operaciones logicas

A= float(input ("Ingresa tu primer numero :"))
B= float(input ("Ingrese tu segundo numero :"))
print (" ")
print("En esta linea, se trabajara el comparativo <")
if(A<B):
    print (f"El numero {A} si es menor que el numero {B}")
else:
    print ("No se cumple este condicional entre el primer y segundo numero")
print (" ")
print("En esta linea, se trabajara el comparativo >")
if(A>B):
    print (f"El  numero {A} si es mayor que el numero {B}")
else:
    print ("No se cumple este condicional entre el primer y segundo numero")
print (" ")
print("En esta linea, se trabajara el comparativo =")
if(A==B):
    print ("Ambos numeros si son iguales")
else:
    print ("Los numeros no son iguales")
print (" ")
print("En esta linea, se trabajara el comparativo menor o igual")
if(A<=B):
    if (A<B):
        print(f"El numero {A} si es menor que el numero {B}")
    if (A==B):
        print(f"El numero {A} es igual que el numero {B}")
else:
    print (f"El numero {A} no es menor o igual que el numero {B}")
print (" ")
print("En esta linea, se trabajara el comparativo mayor o igual")
if(A>=B):
    if (A>B):
        print(f"El numero {A} si es mayor que el numero {B}")
    if (A==B):
        print(f"El numero {A} es igual que el numero {B}")
else:
    print (f"El numero {A} no es mayor o igual que el numero {B}")
print (" ")
print("En esta linea, se trabajara el comparativo diferente")
if(A!=B):
    print("Los numeros si son diferentes")
else:
    print("Los dos numeros son iguales")