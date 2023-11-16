#!/usr/bin/env python3
# Class Attributes and Methods 

class Pet:
    total_pets =0
    
    def __init__(self,name, age, breed, temperament, image_url):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament
        self.image_url = image_url
        
        self.increment_pets()
    
    # 6✅. Create a class method increase_pets that will increment total_pets
        # replace Pet.total_pets += 1 in __init__ with increase_pets()
    @classmethod
    def increment_pets(cls, increment=1):
        cls.total_pets += increment
        #cls keyword refers to class

    def print_pet_details(self):
        print(f'''
             name:{self.name}
              age:{self.age}
              breed:{self.breed}
              tempermant:{self.temperament}
              image_url:{self.image_url}
        ''')




