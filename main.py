from datetime import datetime

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

    def remove_astronaut_by_id(self,search_id):
            for astronaut in self.astronauts:
                if  search_id.lower() == (astronaut.astronaut_id).lower():
                    self.astronauts.remove(astronaut)
                    astronaut.assigned_mission = None
                    return
            return None

    def find_astronaut_by_id(self, search_id):
        for astronaut in self.astronauts:
            if  search_id.lower() == (astronaut.astronaut_id).lower():
                return astronaut
        return None
    
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

    def update_launch_date(self, new_launch_date):
        try:
            datetime.strptime(new_launch_date, "%d-%m-%Y")
            self.launch_date = new_launch_date
        except ValueError:
            print("Invalid Date")
        

class MissionManager:   
    
    def __init__(self):
        self.missions = []
        self.astronauts = []

    def add_mission(self, mission):
        for miss in self.missions:
            if  mission.mission_id == miss.mission_id:
                print("Cannot Add Duplicates")
                return
        self.missions.append(mission)
        print(f"Added Successfully")
        
    def find_mission_by_id(self, search_id):
        
        for mission in self.missions:
            if  search_id.lower() == (mission.mission_id).lower(): 
                return mission
        print(f"No Mission found with the ID {search_id}.")
        return None
        
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
        
    def update_mission_destination(self, mission_id, new_destination):
        mission = self.find_mission_by_id(mission_id)
        if mission == None:
            return
        mission.update_destination(new_destination)
        
    def update_mission_status(self, mission_id, new_status):
        mission = self.find_mission_by_id(mission_id)
        if mission == None:
            return
        mission.update_status(new_status)

    def update_mission_name(self, mission_id, new_name):
        mission = self.find_mission_by_id(mission_id)
        if mission == None:
            return
        mission.update_name(new_name)
        
    def update_mission_launch_date(self, mission_id, new_launch_date):
        mission = self.find_mission_by_id(mission_id)
        if mission == None:
            return
        mission.update_launch_date(new_launch_date)        
        
    def find_missions_by_destination(self, destination):
        found_mission = []
        for mission in self.missions:
            if mission.destination.lower() == destination.lower():
                found_mission.append(mission)
        return found_mission
    
    def find_missions_by_status(self, status):
        found_mission = []
        for mission in self.missions:
            if mission.status.lower() == status.lower():
                found_mission.append(mission)
        return found_mission
    
    def get_mission_count(self):
        return len(self.missions)
    
    def get_mission_count_by_status(self, status):
        return len(self.find_missions_by_status(status))

    def get_mission_summary(self):
        
        summary = {
            "total" : self.get_mission_count(),
            "planned" : self.get_mission_count_by_status("planned"),
            "active" : self.get_mission_count_by_status("active"),
            "completed" : self.get_mission_count_by_status("completed")
        }
        return summary 
    
    def get_total_astronauts(self):
        count = 0
        for mission in self.missions:
            count += len(mission.astronauts)
        return count
    
    def get_astronaut_count_by_mission(self, mission_id):
        mission = self.find_mission_by_id(mission_id)
        if mission is not None:
            count = len(mission.astronauts)
            return count
        else:
            return
        
    def find_astronaut_by_id(self, astronaut_id):
        for astronaut in self.astronauts:
            if astronaut.astronaut_id.lower() == astronaut_id.lower():
                return astronaut
        return None
        
    def get_astronaut_mission(self, astronaut_id):
        astronaut = self.find_astronaut_by_id(astronaut_id)
        if astronaut is not None:
            return astronaut.assigned_mission
        else:
            return None
        
    def get_mission_crew(self, mission_id):
        mission = self.find_mission_by_id(mission_id)
        if mission is not None:
            crew = mission.astronauts 
            return crew
        else:
            return
        
    def get_available_seats(self, mission_id):
        mission = self.find_mission_by_id(mission_id)
        if mission is not None:
            available_seats = mission.MAX_ASTRONAUTS - len(mission.astronauts)
            return available_seats
        else:
            return
        
    def is_mission_ready(self, mission_id):
        mission = self.find_mission_by_id(mission_id)
        if mission is not None and mission.status == "planned" and len(mission.astronauts) > 0:
            return True
        else:
            return False 
        
    def can_assign_astronaut(self, astronaut_id, mission_id):
        astronaut = self.find_astronaut_by_id(astronaut_id)
        mission = self.find_mission_by_id(mission_id)
        return (
            astronaut is not None
            and mission is not None
            and self.is_astronaut_available(astronaut_id)
            and self.get_available_seats(mission_id) > 0
            )
        
    def assign_astronaut_to_mission(self, astronaut_id, mission_id):
        can_assign = self.can_assign_astronaut(astronaut_id, mission_id)
        if can_assign:
            astronaut = self.find_astronaut_by_id(astronaut_id)
            mission = self.find_mission_by_id(mission_id)
            mission.add_astronaut(astronaut)
            return True
        else:
            return False
        
    def unassign_astronaut_from_mission(self, astronaut_id, mission_id):
        astronaut = self.find_astronaut_by_id(astronaut_id)
        mission = self.find_mission_by_id(mission_id)
        if astronaut is not None and mission is not None and astronaut in mission.astronauts:
            mission.remove_astronaut_by_id(astronaut_id)
            return True
        else:
            return False
        
    def is_mission_full(self, mission_id):
        available_seat = self.get_available_seats(mission_id)
        if available_seat is not None and available_seat == 0:
            return True
        elif available_seat is None:
            return None
        else:
            return False
        
    def get_mission_occupancy(self,mission_id):
        mission = self.find_mission_by_id(mission_id)
        if mission is not None:
            return len(mission.astronauts) / mission.MAX_ASTRONAUTS * 100
        else:
            return None
        
    def get_mission_report(self, mission_id):
        mission = self.find_mission_by_id(mission_id)
        if mission is not None:
            return {
                "mission_id" : mission.mission_id,
                "mission_name" : mission.mission_name,
                "status" : mission.status,
                "destination" : mission.destination,
                "astronaut_count" : self.get_astronaut_count_by_mission(mission_id),
                "available_seats" : self.get_available_seats(mission_id),
                "occupancy" : self.get_mission_occupancy(mission_id),
                "ready" : self.is_mission_ready(mission_id),
            }
        else:
            return None
        
    def get_missions_by_destination_report(self, destination):
        missions = self.find_missions_by_destination(destination)
        all_missions = []
        for mission in missions:
            all_missions.append(self.get_mission_report(mission.mission_id))
        return all_missions
        
    def get_mission_crew_report(self, mission_id):
        astronauts = self.get_mission_crew(mission_id)
        all_astronauts = []
        if astronauts is not None:
            for astronaut in astronauts:
                report = {"astronaut_id" : astronaut.astronaut_id,
                        "name": astronaut.name,
                        "country": astronaut.country,
                        "specialization": astronaut.specialization, 
                        }
                all_astronauts.append(report)
            return all_astronauts
        return None
        
    def get_mission_status_report(self, status):
        missions = self.find_missions_by_status(status)
        all_missions = []
        for mission in missions:
            all_missions.append(self.get_mission_report(mission.mission_id))
        return all_missions
        
    def get_mission_dashboard(self):
        summary = self.get_mission_summary()
        return{
            "total_missions" : summary["total"],
            "planned_missions" : summary["planned"],
            "active_missions" : summary["active"],
            "completed_missions" : summary["completed"],
            "total_astronauts" : self.get_total_astronauts()
        }
        
    def register_astronaut(self, astronaut):
        for astro in self.astronauts:
            if  astronaut.astronaut_id == astro.astronaut_id:
                return False
        self.astronauts.append(astronaut)
        return True
        
    def is_astronaut_available(self, astronaut_id):
        astronaut = self.find_astronaut_by_id(astronaut_id)
        if astronaut is None:
            return False
        elif astronaut.assigned_mission is None:
            return True
        else:
            return False  
        
# dummy astronauts
astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
astronaut2 = Astronaut("AST002","Buzz Aldrin","20-01-1930","USA",178,"Pilot")

# dummy mission
mission1 = Mission("MSN001","Mission Mangal","12-08-2025","Mars","planned")
mission2 = Mission("MSN002","Lunar Gateway","15-06-2027","Moon","planned")
mission3 = Mission("MSN003","Mission Mangal","12-08-2025","Mars","planned")

mission1.add_astronaut(astronaut1)
mission1.add_astronaut(astronaut2)
# CLASS CALLING
mission_manager = MissionManager()

# mission manager
mission_manager.add_mission(mission1)
mission_manager.add_mission(mission2)
mission_manager.add_mission(mission3)
mission_manager.register_astronaut(astronaut1)

# TEST
print(mission_manager.is_astronaut_available("AST001"))
print(mission_manager.is_astronaut_available("AST999"))