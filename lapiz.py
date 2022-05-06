class Lapiz():
    def __init__(self, marca, modelo,dureza,color):
        self.marca = marca
        self.modelo = modelo
        self.dureza = dureza
        self.color = color

    def __str__(self):
        return f"{self.marca}, {self.modelo}, {self.dureza}, {self.color}"


lapiz = Lapiz("STAEDLER", "Mars Lumograph Charcoal 100C", "H", "gris")
print(lapiz)
        
