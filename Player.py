class Player:
    def __init__(self, kalaha=0, start_position=None):
        if start_position is None:
            self.array = [6, 6, 6, 6, 6, 6]
        else:
            self.array = list(start_position)
        self.bean_count = kalaha
