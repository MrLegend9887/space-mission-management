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

    VALID_STATUSES = ["planned","active","completed"]

    VALID_TRANSITIONS = {
    "planned": ["active"],
    "active": ["completed"],
    "completed": []
    }

    
    def __init__(self, mission_id, mission_name, launch_date, destination, status):
        self.mission_id = mission_id
        self.mission_name = mission_name
        self.launch_date = launch_date
        self.destination = destination
        self.status = status
        self.astronauts = []

    def add_astronaut(self, astronaut):
        found = False
        for astro in self.astronauts:
            if  astronaut.astronaut_id == (astro.astronaut_id):
                found = True 
                print("Cannot Add Duplicates")
        if not found:
            self.astronauts.append(astronaut)
            print(f"Added Succesfully")
        
        # if astronaut in self.astronauts:
        #     print("Astronaut Already Exists")
        # else:
        #     self.astronauts.append(astronaut)
        
    def remove_astronaut_by_id(self):
            found = False
            search_id = input("Enter a valid astronauts ID: ")
            for astronaut in self.astronauts:
                if  search_id.lower() == (astronaut.astronaut_id).lower():
                    found = True 
                    self.astronauts.remove(astronaut)
                    break
            if not found:
                print(f"No astronaut found with the ID {search_id}.")

    def find_astronaut_by_id(self):
        found = False
        search_id = input("Enter a valid astronauts ID: ")
        for astronaut in self.astronauts:
            if  search_id.lower() == (astronaut.astronaut_id).lower():
                found = True 
                return astronaut
        if not found:
            print(f"No astronaut found with the ID {search_id}.")
    
    def display_mission_details(self):
        print("===== Mission Details =====")
        print(f"Mission ID       : {self.mission_id}")
        print(f"Mission Name     : {self.mission_name}")
        print(f"Launch Date      : {self.launch_date}")
        print(f"Destination      : {self.destination}")
        print(f"Status           : {self.status}")
        print(f"Astronauts:-")
        for astronaut in self.astronauts:
            print(f"-{astronaut.astronaut_id} : {astronaut.name}")
        print("=============================")

    def update_status(self, new_status):
        new_status = new_status.lower()

        if new_status in self.VALID_STATUSES:
            if new_status in self.VALID_TRANSITIONS[self.status]:
                self.status = new_status
            else:
                print(f"status cannot be changed to {new_status} ")
        else:
            print("Invalid Status")

# dummy astronauts
astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
astronaut2 = Astronaut("AST002","Buzz Aldrin","20-01-1930","USA",178,"Pilot")
astronaut3 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")

# dummy mission
mission1 = Mission("MSN001","Mission Mangal","12-08-2025","Mars","planned")

# adding astronauts to a mission 
mission1.add_astronaut(astronaut1)
mission1.add_astronaut(astronaut2)


mission1.add_astronaut(astronaut3)