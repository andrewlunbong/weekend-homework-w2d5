import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room1 = Room("Room one", "R&B")
        self.room2 = Room("Room two", "Pop")
        

    def test_room_has_a_name(self):
        self.assertEqual("Room one", self.room1.name)

    def test_room_have_no_guest(self):
        self.assertEqual(0, self.room1.guest_count())

    def test_room_have_no_song_yet(self):
        self.assertEqual(0, self.room1.song_count())
        
    
    def test_room_can_add_guest(self):
        guest1 = Guest("Andrew", 100)
        guest2 = Guest("Tim", 150)
        self.room1.check_in(guest1)
        self.room2.check_in(guest2)
        self.assertEqual(1, self.room1.guest_count())
        self.assertEqual(1, self.room2.guest_count())

    def test_room_can_remove_guest(self):
        guest1 = Guest("Andrew", 100)
        guest2 = Guest("Tim", 150)
        self.room1.check_in(guest1)
        self.room2.check_in(guest2)
        self.room1.check_out(guest1)
        self.room2.check_out(guest2)
        self.assertEqual(0, self.room1.guest_count())
        self.assertEqual(0, self.room2.guest_count())

    def test_room_has_song(self):
        self.song1 = Song("Say My Name", "R&B")
        self.song2 = Song("What Do You Mean", "Pop")
        self.room1.add_song(self.song1)
        self.room2.add_song(self.song2)
        self.assertEqual(1, self.room1.song_count())
        self.assertEqual(1, self.room2.song_count())

        



