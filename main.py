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

class Mission:

    def __init__(self, mission_id, mission_name, launch_date, destination, status):
        self.mission_id = mission_id
        self.mission_name = mission_name
        self.launch_date = launch_date
        self.destination = destination
        self.status = status
        self.astronauts = []

    def add_astronaut(self, astronaut):
        self.astronauts.append(astronaut)

    def find_astronaut_by_id(self):
        found = False
        search_id = input("Enter a valid astronauts ID: ")
        for astronaut in self.astronauts:
            if  search_id.lower() == (astronaut.astronaut_id).lower():
                found = True 
                return astronaut
        if not found:
            print(f"No astronaut found with the ID {search_id}.")

astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
astronaut2 = Astronaut("AST002","Buzz Aldrin","20-01-1930","USA",178,"Pilot")
mission1 = Mission("MSN001","Mission Mangal","12-08-2025","Mars","Completed")
mission1.add_astronaut(astronaut1)
mission1.add_astronaut(astronaut2)

foundcandidate = mission1.find_astronaut_by_id()
foundcandidate.display_details()