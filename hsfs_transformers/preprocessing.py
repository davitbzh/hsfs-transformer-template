# Min-Max scaling
class MinMaxScaler:
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def scale(self, value):
        return (value - self.min_value) / (self.max_value - self.min_value)
