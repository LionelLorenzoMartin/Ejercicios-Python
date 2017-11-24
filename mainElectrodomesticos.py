import electrodomesticos

ob1 = electrodomesticos.Electrodomestico(50,"negro","C",50)
ob2 = electrodomesticos.Electrodomestico(900,"gris","F",30)
ob3 = electrodomesticos.Electrodomestico(23,"azul","A",78)
ob4 = electrodomesticos.Electrodomestico(6000,"blanco","B",10)
ob5 = electrodomesticos.Lavadora(400,"blanco","A",30,40)
ob6 = electrodomesticos.Lavadora(300,"gris","A",30,45)
ob7 = electrodomesticos.Lavadora(200,"gris","F",20,10)
ob8 = electrodomesticos.Television(1000,"negro","A",20,36,False)
ob9 = electrodomesticos.Television(1300,"negro","B",30,42,True)
ob10 = electrodomesticos.Television(1250,"negro","C",25,40,True)

lista=[ob1, ob2, ob3, ob4, ob5, ob6, ob7, ob8, ob9, ob10]

totalElectrodomesticos = 0
totalTelevisiones = 0
totalLavadoras = 0
for i in lista:
    totalElectrodomesticos = totalElectrodomesticos + i.precioFinal()
    if type(i) is electrodomesticos.Lavadora:
        totalLavadoras = totalLavadoras + i.precioFinal()
    elif type(i) is electrodomesticos.Television:
        totalTv = totalTv + i.precioFinal()

print ("Numero de electrodomesticos: "+str(totalElectrodomesticos))
print ("Numero de lavadoras: "+str(totalLavadoras))
print("Numero de televisiones: "+str(totalTelevisiones))
exit(0)
