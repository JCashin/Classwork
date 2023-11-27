class Fruit():
    def __init__(self, colour="unknown", size="unknown", taste="unknown"):
        self.colour = colour
        self.size = size 
        self.taste = taste
    
    def print_description(self):
        print("The fruit has the Colour: ",self.colour,"\nSize: ",self.size,"\nTaste: ",self.taste)

class Tropical(Fruit):
    def __init__(self,colour,size,taste):
        super().__init__(taste="Sweet")

class Citrus(Fruit):
    def __init__(self, bitter_level="unknown"):
        super().__init__("Sour")
        self.bitter_level = bitter_level
    
    def print_description(self):
        print("The fruit has the Colour: ",self.colour,"\nSize: ",self.ize,"\nTaste: ",self.taste,"\nBitter Level: ",self.bitter_level)

mango = Tropical("Red","Medium","")
mango.print_description()

