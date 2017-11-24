import Persona

print("Nombre: ")
nombre=str(input())
print("Edad: ")
edad=int(input())
print("DNI:")
DNI=input()
print("Sexo: ")
sexo=str(input())
print("Peso: ")
peso=float(input())
print("Altura: ")
altura=float(input())

ob1=Persona.Persona(nombre,edad,DNI,sexo,peso,altura)
res=ob1.calcularIMC(ob1.peso, ob1.altura)
if res==-1:
    print("Come maricon")
elif res==0:
    print("Tas perfecto illo")
elif res==1:
    print("Menos panceta cabron")

exit(0)

