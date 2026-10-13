class Car:
    def __init__(self):
        self.list_of_tyres = []

    def add_tyre(self, tyre):
        self.list_of_tyres.append(tyre)

    def list_tyre_pos_and_readings(self):
        if self.list_of_tyres == []:
            return []
        
        ans = ''
        for tyre in self.list_of_tyres:
            ans += f'{tyre.position} - pressure: {tyre.pressure}, tread: {tyre.tread}, date: {tyre.date}\n'

        return ans