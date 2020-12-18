import random
class MainEngine:
    def __init__(self):
        a=0

    def validate_inputs(self, lower_bound, upper_bound):
        result = True
        if lower_bound > upper_bound:
            result = False
        return result

    def find_random_number(self, lower_bound, upper_bound):
        return random.randint(int(lower_bound), int(upper_bound))
