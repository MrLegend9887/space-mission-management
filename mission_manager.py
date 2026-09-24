from astronaut import Astronaut
from mission import Mission

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
        
    def get_astronaut_report(self, astronaut_id):
        astronaut = self.find_astronaut_by_id(astronaut_id)
        if astronaut is not None:
            if astronaut.assigned_mission is not None:
                assigned_mission = astronaut.assigned_mission.mission_id
            else :
                assigned_mission = None
            return{
                "astronaut_id" : astronaut.astronaut_id,
                "name" : astronaut.name,
                "country" : astronaut.country,
                "specialization" : astronaut.specialization,
                "assigned_mission" : assigned_mission,
            }
        return None
    
    def get_all_astronaut_reports(self):
        all_astronauts = []
        for astronaut in self.astronauts:
            all_astronauts.append(self.get_astronaut_report(astronaut.astronaut_id))
        return all_astronauts
    
    def get_available_astronaut_reports(self):
        all_astronauts = []
        for astronaut in self.astronauts:
            if self.is_astronaut_available(astronaut.astronaut_id):
                all_astronauts.append(self.get_astronaut_report(astronaut.astronaut_id))
        return all_astronauts
            
    def get_assigned_astronaut_reports(self):
        all_astronauts = []
        for astronaut in self.astronauts:
            if not self.is_astronaut_available(astronaut.astronaut_id):
                all_astronauts.append(self.get_astronaut_report(astronaut.astronaut_id))
        return all_astronauts
    
    def get_astronaut_dashboard(self):
        return{
    "total_astronauts": len(self.get_all_astronaut_reports()),
    "available_astronauts": len(self.get_available_astronaut_reports()),
    "assigned_astronauts": len(self.get_assigned_astronaut_reports())
        }
        
    def get_mission_capacity_report(self, mission_id):
        mission = self.find_mission_by_id(mission_id)
        if mission is not None:
            return{
                "mission_id": mission_id,
                "mission_name": mission.mission_name,
                "capacity": mission.MAX_ASTRONAUTS,
                "occupied_seats": self.get_astronaut_count_by_mission(mission_id),
                "available_seats": self.get_available_seats(mission_id),
                "occupancy": self.get_mission_occupancy(mission_id),
                "is_full": self.is_mission_full(mission_id)
            }
        else:
            return None