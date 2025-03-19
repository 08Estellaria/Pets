class Pet(object):
    def __init__(self,name,species,description,age,gender):
        self.name = name
        self.species = species
        self.description = description
        self.age = age
        self.gender = gender

    def get_name(self):
        return self.name
    def get_species(self):
        return self.species
    def get_description(self):
        return self.description
    def get_age(self):
        return self.age
    def get_gender(self):
        return self.gender
    def get_describe(self):
        return self.name,self.species,self.description,self.age,self.gender

    def set_name(self,name):
        self.name = name
    def set_species(self,species):
        self.species = species
    def set_description(self,description):
        self.description = description
    def set_age(self,age):
        self.age = age
    def set_gender(self,gender):
        self.gender = gender 
