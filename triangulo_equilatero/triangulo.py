#Determinar si un triangulo es equilatero, isoceles o escaleno 

print("-------------------------")
print("--------TRIANGULO--------")
print("-------------------------")

#INPUT
A=int(input("ingrese lado a: "))
B=int(input("ingrese lado b: "))
C=int(input("ingrese lado c: "))

#PROCESS
if A==B and B==C:
  print("El triangulo es equilatero. ")
elif A==C or B == C or C==A or A==B:
  print("El triangulo es isoceles. ")
else:
  print("El triangulo escaleno. ")
  
#FIN 