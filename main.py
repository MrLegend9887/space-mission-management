class Astronaut:

    def __init__(self, astronaut_id, name, dob, country, height, specialization):
        self.astronaut_id = astronaut_id
        self.name = name
        self.dob = dob
        self.country = country
        self.height = height
        self.specialization = specialization
        self.assigned_mission = None
    
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

    VALID_TRANSITIONS = {"planned": ["active"], "active": ["completed"], "completed": [] }
    MAX_ASTRONAUTS = 5

    
    def __init__(self, mission_id, mission_name, launch_date, destination, status):
        self.mission_id = mission_id
        self.mission_name = mission_name
        self.launch_date = launch_date
        self.destination = destination
        self.status = status
        self.astronauts = []

    def add_astronaut(self, astronaut):
        if astronaut.assigned_mission is not None:
            print(f"Astronaut is already assigned to {astronaut.assigned_mission.mission_id}")
            return
        for astro in self.astronauts:
            if  astronaut.astronaut_id == astro.astronaut_id:
                print("Cannot Add Duplicates")
                return
        if len(self.astronauts) >= self.MAX_ASTRONAUTS:
            print(f"Maximum Capacity reached for {self.mission_name}")
        else:
            self.astronauts.append(astronaut)
            astronaut.assigned_mission = self
            print(f"Added Successfully")

    def remove_astronaut_by_id(self):
            found = False
            search_id = input("Enter a valid astronauts ID: ")
            for astronaut in self.astronauts:
                if  search_id.lower() == (astronaut.astronaut_id).lower():
                    found = True 
                    self.astronauts.remove(astronaut)
                    astronaut.assigned_mission = None
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

    def update_name(self, new_name):
        new_name = new_name.strip()
        if new_name == "":
            print("Enter A Valid Mission Name")
            return
        self.mission_name = new_name

    def update_destination(self, new_destination):
        new_destination = new_destination.strip()
        if new_destination == "":
            print("Enter A Valid Destination Name")
            return
        self.destination = new_destination      

class MissionManager:   
    
    def __init__(self):
        self.missions = []

    def add_mission(self, mission):
        for miss in self.missions:
            if  mission.mission_id == miss.mission_id:
                print("Cannot Add Duplicates")
                return
        self.missions.append(mission)
        print(f"Added Successfully")
        
    def find_mission_by_id(self):
        
        search_id = input("Enter a valid Mission ID: ")
        for mission in self.missions:
            if  search_id.lower() == (mission.mission_id).lower(): 
                return mission
        print(f"No Mission found with the ID {search_id}.")
        
    def display_all_missions(self):
        for mission in self.missions:
            mission.display_mission_details()
            
    def remove_mission_by_id(self, search_id):
        for mission in self.missions:
            if mission.mission_id.lower() == search_id.lower():
                for astronaut in mission.astronauts:
                    astronaut.assigned_mission = None
                self.missions.remove(mission) 
                return           
        print("Enter A Valid Mission ID")
                
        
# dummy astronauts
astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
astronaut2 = Astronaut("AST002","Buzz Aldrin","20-01-1930","USA",178,"Pilot")
astronaut3 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")

# dummy mission
mission1 = Mission("MSN001","Mission Mangal","12-08-2025","Mars","planned")
mission2 = Mission("MSN002","Lunar Gateway","15-06-2027","Moon","planned")

# TEST 
mission1.update_name("Artemis II")
mission1.update_destination("Moon")

print(mission1.mission_name)
print(mission1.destination)