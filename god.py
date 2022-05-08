from room import Room


class God:

    def __init__(self):
        self.eye = 0
        self.make_world()

    def make_world(self):
        rooms = {room: None for room in range(40)}
        rooms[5] = rooms[15] = rooms[25] = rooms[35] = 'hall'
        rooms[0] = rooms[10] = rooms[20] = rooms[30] = 'corner'
        for room in rooms:
            if rooms[room] is None:
                rooms[room] = Room({'name': room})
        halls = {hall: Room({'name': 'hall'+str(hall)}) for hall in range(4)}
        self.rooms = rooms
        self.halls = halls
