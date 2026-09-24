from astronaut import Astronaut
from mission import Mission
from mission_manager import MissionManager     
        
# dummy astronauts
astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
astronaut2 = Astronaut("AST002","Buzz Aldrin","20-01-1930","USA",178,"Pilot")
astronaut3 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")

# dummy mission
mission1 = Mission("MSN001","Mission Mangal","12-08-2025","Mars","planned")
mission2 = Mission("MSN002","Lunar Gateway","15-06-2027","Moon","planned")
mission3 = Mission("MSN003","Mission Mangal","12-08-2025","Mars","planned")

# CLASS CALLING
mission_manager = MissionManager()

# mission manager
mission_manager.add_mission(mission1)
mission_manager.add_mission(mission2)