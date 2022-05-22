from room import Room


class World:
    def __init__(self):
        rooms = {room: None for room in range(40)}
        for i in range(5,40,5):
            rooms[i] = Room({'name':'hall'+str(i)})
        for i in range(0,40,10):
            rooms[i] = Room({'name':'corner'+str(i)})

        for room in rooms:
            if rooms[room] is None:
                rooms[room] = Room({'name': 'room' + str(room)})

        halls = {hall: Room({'name': 'hall' + str(hall)}) for hall in range(4)}

        self.rooms = rooms
        self.halls = halls
