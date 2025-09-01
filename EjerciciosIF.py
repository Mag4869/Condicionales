#Miguel Galindo


#Operaciones logicas

A= float(input ("Ingresa tu primer numero :"))
B= float(input ("Ingrese tu segundo numero :"))
print("En esta linea, se trabajara el comparativo <")
if(A<B):
    print (f"El primer numero {A} si es menor que el segundo numero {B}")
else:
    print ("No se cumple este condicional entre el primer y segundo numero")
print("En esta linea, se trabajara el comparativo <")
if(A>B):
    print (f"El primer numero {A} si es mayor que el segundo numero {B}")
else:
    print ("No se cumple este condicional entre el primer y segundo numero")
print("En esta linea, se trabajara el comparativo =")
if(A==B):
    print ("Ambos numeros si son iguales")
else:
    print ("Los numeros no son iguales")
print("En esta linea, se trabajara el comparativo menor o igual")
if(A<=B):
    if (A<B):
        print(f"El primer numero {A} si es menor que el segundo numero {B}")
    if (A==B):
        print(f"El primer numero {A} es igual que el segundo numero {B}")
else:
    print (f"El primer numero {A} no es menor o igual que el segundo numero {B}")
    print("En esta linea, se trabajara el comparativo mayor o igual")
if(A>=B):
    if (A>B):
        print(f"El primer numero {A} si es mayor que el segundo numero {B}")
    if (A==B):
        print(f"El primer numero {A} es igual que el segundo numero {B}")
else:
    print (f"El primer numero {A} no es mayor o igual que el segundo numero {B}")
    print("En esta linea, se trabajara el comparativo diferente")
if(A!=B):
    print("Los numeros si son diferes")
else:
    print("Los dos numeros son iguales")