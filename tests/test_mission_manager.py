import unittest
from main import MissionManager, Mission


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

if __name__ == "__main__":
    unittest.main()