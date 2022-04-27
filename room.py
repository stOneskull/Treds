class Room:
    rooms = {room:None for room in range(40)}
    pointer = 0

    def __init__(self, num, details):
        Room.rooms[num] = self
        paint(self, details)

    def __repr__(self):
        return self.name

