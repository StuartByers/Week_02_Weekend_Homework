class Room:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        
        self.guests = []
        self.songs = []

    def add_guest(self, guest):
        if len(self.guests) < self.capacity:
            self.guests.append(guest)
    
    def remove_guest(self, guest):
        self.guests.remove(guest)

    def add_song_to_room(self, song):
        self.songs.append(song)

    def remove_song_from_room(self, song):
        self.songs.remove(song)