import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Say My Name", "R&B")
        self.song2 = Song("What Do You Mean", "Pop")

    def test_song_has_a_genre(self):
        self.assertEqual("Pop", self.song2.genre)

    
