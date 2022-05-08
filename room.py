class Room:

    def __init__(self, details):
        self.paint(details)

    def __repr__(self, name='76'):
        return self.name or name

    def paint(self, details):
        for attr, val in details.items():
            setattr(self, attr, val)

