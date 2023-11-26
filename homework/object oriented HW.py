class Animal(): # assigns "Animal" Class to be called throughout the program 
    def __init__(self, animal_species="unknown", age=0, threat_level="peaceful", hunger_level=0): # assings the attributes for species age threat and hunger
        self.animal_species = animal_species
        self.age = age
        self.threat_level = threat_level
        self.hunger_level = hunger_level
        
    def setSpecies(self):
        name = input("What species of animal? ") # asks for animal species and returns as string
        return name
    def setAge(self):
        age = input("What is the age of the animal? ") # asks for animal age and returns as int 
        return age
    def setHunger_level(self):
        hunger = int(input("What is the animals hunger level (1-10)? ")) # asks for animal hunger level as int
        loop = True
        while loop == True:
            if hunger < 1 or hunger > 10: # validates that hunger level is between 1 and 10 
                hunger = int(input("What is the animals hunger level (1-10)? "))
            else:
                loop = False
        return int(hunger) # returns value for hunger as int
    def changeThreat_level(self,hungerLevel):
        threat = ""
        if hungerLevel <= 3: # checks value of hunger and assigns "threat" as required
            threat = "Peaceful"
        elif hungerLevel <= 7:
            threat = "Narky"
        elif hungerLevel <=10:
            threat = "Aggressive"
        return threat

cat = Animal("",0,"",0) # Insatiates object cat

species=cat.setSpecies() # sets "species" as returned value from setSpecies function
cat.animal_species = species       

age=cat.setAge() # sets "age" as returned value from setAge function
cat.age = age

hunger=cat.setHunger_level() # sets "hunger" as returned value from setHUnger_level function
cat.hunger_level = hunger

threat=cat.changeThreat_level(hunger) # sets "threat" as returned value from changeThreat_level function
cat.threat_level = threat

print("Animal Species: ", cat.animal_species,"\nAnimal Age: ",cat.age,"\nAnimal Hunger Level:",cat.hunger_level,"\nAnimal Threat Level: ",cat.threat_level) # prints all attribues assigned to cat 