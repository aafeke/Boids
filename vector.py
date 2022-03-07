import time

initiated = False
start = 0


class vector:
    def __init__(self, greatness=0, angle=0):
        self.vector[0] = greatness
        self.vector[1] = angle


    @classmethod
    def set_time(cls):
        vector.start = time.time()

    @classmethod
    def get_time(cls):
        return time.time() - vector.start
