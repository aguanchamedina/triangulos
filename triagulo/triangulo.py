#Determinar si dados tres numeros a, b, c verificar si puede formar los lados de un triangulo 

print("-------------------------")
print("--------TRIANGULO--------")
print("-------------------------")

#INPUT
A=int(input("ingrese lado a: "))
B=int(input("ingrese lado b: "))
C=int(input("ingrese lado c: "))

if (A+B) >C and (A+C) >B and  (B+C)>A: 
    print("Si se forma un triangulo. ")
else: print ("No se forma un triangulo. ")

#FIN 



