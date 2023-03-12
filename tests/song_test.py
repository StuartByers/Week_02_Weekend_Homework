import unittest

from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("Song Title 1")
        self.song_2 = Song("Song Title 2")

    def test_songs_have_names(self):
        self.assertEqual("Song Title 1", self.song_1.name)
        self.assertEqual("Song Title 2", self.song_2.name)