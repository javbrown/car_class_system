

class Tyre:
    # User-facing properties:
    #   position: string
    #   pressure: string
    #   tread: string
    #   date: string
    #   history: []

    def __init__(self, position, pressure, tread, date):
        self.position = position
        self.pressure = pressure
        self.tread = tread
        self.date = date
        self.history = [{
            'pressure': pressure,
            'tread': tread,
            'date': date,
        }]

    def add_reading(self, pressure, tread, date):
        update = {
            'pressure': pressure,
            'tread': tread,
            'date': date
        }
        self.history.append(update)

