class Cell:
    def __init__(self):
        pass

    def set_state(self, state):
        if state == 'ON':
            self.state = True
        elif state == 'OFF':
            self.state = False
        else:
            raise Exception

    
    def alt_state(self):
        try:
            self.state = not self.state
        except AttributeError:
            print("No state associated yet. Please, declare a state ('ON', 'OFF') using the .set_state method")
    

    def snap(self):
        pass


    def print_state(self):
        try:
            if self.state:
                print('ON')
            else:
                print('OFF')
        except AttributeError:
            print("No state associated yet. Please, declare a state ('ON', 'OFF') using the .set_state method")
