class Persona:

    def __init__(self,nombre, edad, DNI, sexo, peso, altura):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.DNI = DNI
        self.peso = peso
        self.altura = altura

    def calcularIMC(self, peso, altura):
        self.peso = peso
        self.altura = altura
        altura = altura/100
        imc = (peso / (altura * altura))
        print(imc)
        if (imc < 18.5):
            return -1
        elif (imc >= 18.5 and imc <= 24.99):
            return 0
        elif (imc > 25):
            return 1
        return imc

    def mayorDeEdad(self, edad):
        self.edad = int(input("Introduce tu edad: "))
        if (edad < 18):
            return False
        else:
            return True

    def introducirSexo(self, sexo):
        self.sexo = input(input("Introduce tu sexo: "))
        if (sexo != "M" | sexo != "H"):
            print("Error, Introduce(M o H)")
            self.sexo = "M"
        print(sexo)
        return sexo

    def generarDni(self, dni):
        import random
        self.dni = print(random.randint(0, 9), 8)
        print(dni)
        return dni