class Room:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre
        self.guest = [ ]
        self.song = [] 

    def guest_count(self):
        return len(self.guest)
    
    def song_count(self):
        return len(self.song)
    
    def check_in(self, guest):
        self.guest.append(guest)

    def check_out(self, current_guest):
        self.guest.remove(current_guest)

    def add_song(self, song):
        self.song.append(song)




        

