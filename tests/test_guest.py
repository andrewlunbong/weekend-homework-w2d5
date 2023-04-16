import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest ("Andrew", 100)
        self.guest2 = Guest ("Tim", 150)
    
    def test_guess1_has_a_name(self):
        self.assertEqual("Andrew", self.guest1.name)

    def test_guess2_wallet(self):
        self.assertEqual(150, self.guest2.wallet)
        





