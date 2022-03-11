import time
import math

class vector:
    def __init__(self, greatness=0, angle=0):
        # 0 : greatness
        # 1 : angle (0-359)
        # 2 : x subvector
        # 3 : y subvector

        self.set_greatness(greatness)
        self.vector[1] = angle

    def set_greatness(self, val: float):
        if not val == 0:
            self.vector[0] = val
            self.vector[2] = val * math.cos(self.vector[1])
            self.vector[3] = val * math.sin(self.vector[1])
            # We should get the time in order to
            # calculate the delta time while greatness of the
            # vector != 0
            self.__set_time()
        else:
            self.vector[0] = 0
            self.vector[2] = 0
            self.vector[3] = 0
            self.__reset_time()

    def get_delta(self):
        if self.start_time is not 0:
            return time.time() - self.start_time
        else: pass

    @classmethod
    def vectoral_add(cls, vec1, vec2):
        pass

    def __set_time(self):
        # Double under score ensures the method is
        # private, used for the sake of information hiding.
 
        self.start_time = time.time()

    def __reset_time(self):

        self.start_time = 0
        pass
