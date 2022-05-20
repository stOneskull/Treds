from room import Room


class World:
    def __init__(self):
        rooms = {room: None for room in range(40)}
        rooms[5] = rooms[15] = rooms[25] = rooms[35] = 'hall'
        rooms[0] = rooms[10] = rooms[20] = rooms[30] = 'corner'

        for room in rooms:
            if rooms[room] is None:
                rooms[room] = Room({'name': 'room' + str(room)})

        halls = {hall: Room({'name': 'hall' + str(hall)}) for hall in range(4)}

        self.rooms = rooms
        self.halls = halls
