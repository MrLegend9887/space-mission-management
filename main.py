class Astronaut:
    def __init__(self, astronaut_id, name, dob, country, height, specialization):
        self.astronaut_id = astronaut_id
        self.name = name
        self.dob = dob
        self.country = country
        self.height = height
        self.specialization = specialization
    
    def display_details(self):
        print("===== Astronaut Details =====")
        print(f"ID              : {self.astronaut_id}")
        print(f"Name            : {self.name}")
        print(f"Date of Birth   : {self.dob}")
        print(f"Country         : {self.country}")
        print(f"Height          : {self.height} cm")
        print(f"Specialization  : {self.specialization}")
        print("=============================")
    
    def update_name(self, new_name):
        self.name = new_name
    
    def update_country(self, new_country):
        self.country = new_country

    def update_height(self, new_height):
        self.height = new_height

    def update_specialization(self, new_specialization):
        self.specialization = new_specialization
    

astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
astronaut1.display_details()
astronaut1.update_name("Kalpana Chawla")
astronaut1.update_country("India")
astronaut1.update_height(175)
astronaut1.update_specialization("Commander")
astronaut1.display_details()