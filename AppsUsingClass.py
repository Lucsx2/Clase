class fruta:
    def __init__(self, name, color, sabor):
        self.name = name
        self.color = color
        self.sabor = sabor
    
    def introducirse(self):
        print("Soy una:", self.name)

a1 = fruta("Banana", "amarillo", "dulce")
a2 = fruta("Pera", "verde", "dulce")

a1.introducirse()
a2.introducirse()

del a1
del a2

#Video usado de referencia para este codigo: https://www.youtube.com/watch?v=wfcWRAxRVBA&t=13s