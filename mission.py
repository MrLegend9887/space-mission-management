from datetime import datetime

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