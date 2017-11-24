class Electrodomestico:

    def __init__(self,precio, color, consumo, peso):
        self.precio = precio
        self.color = color
        self.consumo = consumo
        self.peso = peso


    #Comprobador de color
    def comprobarColor(self, color):
        if(color == "blanco")
            self.color="blanco"
        elif(color == "negro")
            self.color="negro"
        elif (color == "rojo")
            self.color = "rojo"
        elif(color == "azul")
            self.color="azul"
        elif(color == "gris")
            self.color="gris"
        else:
            self.color="blanco"

    #Comprobador del consumo energético
    def comprobarConsumoEnergetico(self, consumo):
        if(consumo=="F")
            self.consumo="F"
            return 10
        elif(consumo=="A")
            self.consumo="A"
            return 1000
        elif (consumo == "B")
            self.consumo = "B"
            return 80
        elif (consumo == "C")
            self.consumo = "C"
            return 60
        elif (consumo == "D")
            self.consumo = "D"
            return 50
        elif (consumo == "E")
            self.consumo = "E"
            return 30
        else:
            self.consumo="F"
            return 10

    #Comprobador del peso
    def pesoPrecio(self, peso):
        if (peso <= 19)
            return 10
        elif(peso>=20 and peso<=49)
            return 50
        elif(peso>=50 and peso<=79)
            return 80
        elif(peso>=80)
            return 100

    #Comprobador precio final
    def precioFinal(self):
        preciofinal = (self.comprobarConsumoEnergetico(self.consumo)+self.pesoPrecio(self.peso)+self.precio)
        return preciofinal



    #lavadora

class Lavadora(Electrodomestico):

        def __init__(self, carga):
            super.precio=self.precio
            super.color=self.color
            super.consumo=self.consumo
            super.peso=self.peso
            self.carga= carga
            Electrodomestico.comprobarConsumoEnergetico(self.consumo)

        def getCarga(self):
            return self.carga

        def comprobarCarga(self):
            if(carga>30)
                return 50
            else
                return 0

        def precioFinal(self):
            preciofinal = (self.comprobarCarga()+ Electrodomestico.comprobarConsumoEnergetico() + self.precio)
            return preciofinal

class Television(Electrodomestico):

    def __init__(self, resolucion, fourK):
        super.precio = self.precio
        super.color = self.color
        super.consumo = self.consumo
        super.peso = self.peso
        self.resolucion = resolucion
        self.fourK = fourK

    def getResolucion(self, resolucion):
        return resolucion

    def getFourK(self, fourK):
        return fourK

    def precioFinal(self):
        if(self.resolucion>40 and self.fourK==False)
            preciofinal = ((Electrodomestico.comprobarConsumoEnergetico() + self.precio)*0.3)
            return preciofinal
        elif(self.resolucion>40 and self.fourK==True)
            preciofinal = ((Electrodomestico.comprobarConsumoEnergetico() + self.precio +50)*0.3)
            return preciofinal
        elif(self.resolucion<40 and self.fourK==True)
            preciofinal =(Electrodomestico.comprobarConsumoEnergetico() + self.precio + 50)
            return preciofinal
        else
            preciofinal = (Electrodomestico.comprobarConsumoEnergetico() + self.precio)
            return preciofinal





