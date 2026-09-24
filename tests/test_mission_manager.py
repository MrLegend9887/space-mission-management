import unittest
from main import MissionManager, Mission, Astronaut


class TestMissionManager(unittest.TestCase):

    def test_manager_starts_empty(self):
        manager = MissionManager()

        self.assertEqual(manager.get_mission_count(), 0)

    def test_add_mission_increases_count(self):
        manager = MissionManager()

        mission = Mission(
            "MSN001",
            "Test Mission",
            "12-08-2025",
            "Mars",
            "planned"
        )

        manager.add_mission(mission)
        
        self.assertEqual(manager.get_mission_count(), 1)
        
    def test_duplicate_mission_is_rejected(self):
        manager = MissionManager()
        
        mission1 = Mission(
            "MSN001",
            "Test Mission 1",
            "12-08-2025",
            "Mars",
            "planned"
        )
        mission2 = Mission(
            "MSN001",
            "Test Mission 2",
            "12-08-2026",
            "Moon",
            "active"
        )
        manager.add_mission(mission1)
        manager.add_mission(mission2)
        
        self.assertEqual(manager.get_mission_count(), 1)
        
    def test_remove_mission_decreases_count(self):
        manager = MissionManager()

        mission = Mission(
            "MSN001",
            "Test Mission",
            "12-08-2025",
            "Mars",
            "planned"
        )

        manager.add_mission(mission)
        manager.remove_mission_by_id(mission.mission_id)
        
        self.assertEqual(manager.get_mission_count(), 0)
        
    def test_remove_unknown_mission(self):
        manager = MissionManager()
        
        manager.remove_mission_by_id("MSN999")
        
        self.assertEqual(manager.get_mission_count(), 0)
        
    def test_find_mission_by_id(self):
        manager = MissionManager()
        mission1 = Mission(
            "MSN001",
            "Test Mission",
            "12-08-2025",
            "Mars",
            "planned"
        )
        manager.add_mission(mission1)
        
        mission = manager.find_mission_by_id("MSN001")
        
        self.assertEqual(mission.mission_id, "MSN001")

    def test_find_unknown_mission(self):
        manager = MissionManager()
        
        mission = manager.find_mission_by_id("MSN999")

        self.assertIsNone(mission)

    def test_update_mission_status(self):
        manager = MissionManager()
        mission = Mission(
            "MSN001",
            "Test Mission",
            "12-08-2025",
            "Mars",
            "planned"
        )
        manager.add_mission(mission)
        
        manager.update_mission_status("MSN001", "active")
        
        self.assertEqual(mission.status, "active")

    def test_invalid_mission_status_transition(self):
        manager = MissionManager()

        mission = Mission(
            "MSN001",
            "Test Mission",
            "12-08-2025",
            "Mars",
            "planned"
        )

        manager.add_mission(mission)

        manager.update_mission_status("MSN001", "completed")

        self.assertEqual(mission.status, "planned")

    def test_invalid_mission_status(self):
        manager = MissionManager()
        mission = Mission(
            "MSN001",
            "Test Mission",
            "12-08-2025",
            "Mars",
            "planned"
        )

        manager.add_mission(mission)

        manager.update_mission_status("MSN001", "banana")

        self.assertEqual(mission.status, "planned")
        
    def test_find_missions_by_destination(self):
        manager = MissionManager()
                
        mission1 = Mission(
            "MSN001",
            "Test Mission 1",
            "12-08-2025",
            "Mars",
            "planned"
        )
        mission2 = Mission(
            "MSN002",
            "Test Mission 2",
            "12-08-2026",
            "Moon",
            "active"
        )
        
        manager.add_mission(mission1)
        manager.add_mission(mission2)
        
        self.assertEqual(len(manager.find_missions_by_destination("Mars")), 1)
        
    def test_find_missions_by_status(self):
        manager = MissionManager()
                
        mission1 = Mission(
            "MSN001",
            "Test Mission 1",
            "12-08-2025",
            "Mars",
            "planned"
        )
        mission2 = Mission(
            "MSN002",
            "Test Mission 2",
            "12-08-2026",
            "Moon",
            "active"
        )
        
        manager.add_mission(mission1)
        manager.add_mission(mission2)
        
        self.assertEqual(len(manager.find_missions_by_status("active")), 1)
        
    def test_register_astronaut(self):
        manager = MissionManager()
        astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        
        self.assertTrue(manager.register_astronaut(astronaut1))
        
    def test_duplicate_astronaut_registration(self):
        manager = MissionManager()
        astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        
        manager.register_astronaut(astronaut1)
        result = manager.register_astronaut(astronaut1)
        self.assertFalse(result)
        
    def test_assign_astronaut_to_mission(self):
        manager = MissionManager()
        astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        mission1 = Mission(
            "MSN001",
            "Test Mission 1",
            "12-08-2025",
            "Mars",
            "planned"
        )        
                
        manager.register_astronaut(astronaut1)
        manager.add_mission(mission1)
        
        result = manager.assign_astronaut_to_mission("AST001", "MSN001")
        
        self.assertTrue(result)
        
    def test_assign_already_assigned_astronaut(self):
        manager = MissionManager()
        astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        mission1 = Mission(
            "MSN001",
            "Test Mission 1",
            "12-08-2025",
            "Mars",
            "planned"
        )        
                
        manager.register_astronaut(astronaut1)
        manager.add_mission(mission1)
        manager.assign_astronaut_to_mission("AST001", "MSN001")
        
        result = manager.assign_astronaut_to_mission("AST001", "MSN001")
        
        self.assertFalse(result)
        
    def test_unassign_astronaut_from_mission(self):
        manager = MissionManager()
        astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        mission1 = Mission(
            "MSN001",
            "Test Mission 1",
            "12-08-2025",
            "Mars",
            "planned"
        )        

        manager.register_astronaut(astronaut1)
        manager.add_mission(mission1)
        manager.assign_astronaut_to_mission("AST001", "MSN001")
        
        result = manager.unassign_astronaut_from_mission("AST001", "MSN001")
        
        self.assertTrue(result)
        
    def test_unassign_makes_astronaut_available(self):
        manager = MissionManager()
        astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        mission1 = Mission(
            "MSN001",
            "Test Mission 1",
            "12-08-2025",
            "Mars",
            "planned"
        )        

        manager.register_astronaut(astronaut1)
        manager.add_mission(mission1)
        manager.assign_astronaut_to_mission("AST001", "MSN001")
        manager.unassign_astronaut_from_mission("AST001", "MSN001")
        
        result = manager.is_astronaut_available("AST001")
        
        self.assertTrue(result)
        
    def test_mission_available_seats(self):
        manager = MissionManager()
        mission1 = Mission(
            "MSN001",
            "Test Mission 1",
            "12-08-2025",
            "Mars",
            "planned"
        )        

        manager.add_mission(mission1)        
        
        result = manager.get_available_seats("MSN001")
        
        self.assertEqual(result, 5)
        
    def test_mission_is_full(self):
        manager = MissionManager()
        astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        astronaut2 = Astronaut("AST002","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        astronaut3 = Astronaut("AST003","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        astronaut4 = Astronaut("AST004","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        astronaut5 = Astronaut("AST005","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        mission1 = Mission(
            "MSN001",
            "Test Mission 1",
            "12-08-2025",
            "Mars",
            "planned"
        )
        
        manager.add_mission(mission1)
        manager.register_astronaut(astronaut1)
        manager.register_astronaut(astronaut2)
        manager.register_astronaut(astronaut3)
        manager.register_astronaut(astronaut4)
        manager.register_astronaut(astronaut5)
        manager.assign_astronaut_to_mission("AST001","MSN001")
        manager.assign_astronaut_to_mission("AST002","MSN001")
        manager.assign_astronaut_to_mission("AST003","MSN001")
        manager.assign_astronaut_to_mission("AST004","MSN001")
        manager.assign_astronaut_to_mission("AST005","MSN001")
        
        result = manager.is_mission_full("MSN001")
        
        self.assertTrue(result)

    def test_add_another_when_mission_is_full(self):
        manager = MissionManager()
        astronaut1 = Astronaut("AST001","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        astronaut2 = Astronaut("AST002","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        astronaut3 = Astronaut("AST003","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        astronaut4 = Astronaut("AST004","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        astronaut5 = Astronaut("AST005","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        astronaut6 = Astronaut("AST005","Neil Armstrong","05-08-1930","USA",180,"Pilot")
        mission1 = Mission(
            "MSN001",
            "Test Mission 1",
            "12-08-2025",
            "Mars",
            "planned"
        )
        
        manager.add_mission(mission1)
        manager.register_astronaut(astronaut1)
        manager.register_astronaut(astronaut2)
        manager.register_astronaut(astronaut3)
        manager.register_astronaut(astronaut4)
        manager.register_astronaut(astronaut5)
        manager.register_astronaut(astronaut6)
        manager.assign_astronaut_to_mission("AST001","MSN001")
        manager.assign_astronaut_to_mission("AST002","MSN001")
        manager.assign_astronaut_to_mission("AST003","MSN001")
        manager.assign_astronaut_to_mission("AST004","MSN001")
        manager.assign_astronaut_to_mission("AST005","MSN001")
        manager.assign_astronaut_to_mission("AST006","MSN001")
        
        result = manager.assign_astronaut_to_mission("AST006","MSN001")
        
        self.assertFalse(result)
        
    def test_assign_unknown_astronaut(self):
        manager = MissionManager()
        mission1 = Mission(
            "MSN001",
            "Test Mission 1",
            "12-08-2025",
            "Mars",
            "planned"
        )
        manager.add_mission(mission1)
        
        result = manager.assign_astronaut_to_mission("AST999","MSN001")
        
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()