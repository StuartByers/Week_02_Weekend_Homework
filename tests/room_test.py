import unittest

from src.room import Room
from src.guest import Guest
from src.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room("Karaoke Room 1", 5)
        self.room_2 = Room("Karaoke Room 2", 10)

        self.guest_1 = Guest("Guest 1")
        self.guest_2 = Guest("Guest 2")

        self.song_1 = Song("Song Title 1")
        self.song_2 = Song("Song Title 2")

    def test_rooms_have_names(self):
        self.assertEqual("Karaoke Room 1", self.room_1.name)
        self.assertEqual("Karaoke Room 2", self.room_2.name)

    def test_rooms_have_capacities(self):
        self.assertEqual(5, self.room_1.capacity)
        self.assertEqual(10, self.room_2.capacity)

    def test_guests_have_names(self):
        self.assertEqual("Guest 1", self.guest_1.name)
        self.assertEqual("Guest 2", self.guest_2.name)
    
    def test_can_add_guest(self):
        self.assertEqual(0, len(self.room_1.guests))
        self.room_1.add_guest(self.guest_1)
        self.assertEqual(1, len(self.room_1.guests))

    def test_can_remove_guests(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_guest(self.guest_2)
        self.assertEqual(2, len(self.room_1.guests))
        self.room_1.remove_guest(self.guest_2)
        self.assertEqual(1, len(self.room_1.guests))

    def test_can_add_song(self):
        self.assertEqual(0, len(self.room_1.songs))
        self.room_1.add_song_to_room(self.song_1)
        self.assertEqual(1, len(self.room_1.songs))

    def test_can_remove_song(self):
        self.room_1.add_song_to_room(self.song_1)
        self.room_1.add_song_to_room(self.song_2)
        self.assertEqual(2, len(self.room_1.songs))
        self.room_1.remove_song_from_room(self.song_1)
        self.assertEqual(1, len(self.room_1.songs))