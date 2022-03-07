import time

class vector:
    def __init__(self, greatness=0, angle=0):
        self.vector[0] = greatness
        self.vector[1] = angle
        self.set_greatness(0)

    def set_greatness(self, val: float):
        if not val == 0:
            self.vector[0] = val

            # We should get the time in order to
            # calculate the delta time while greatness of the
            # vector != 0
            self.__set_time()
        else:
            self.vector[0] = 0
            self.__reset_time()

    def get_delta(self):
        if self.start_time is not 0:
            return time.time() - self.start_time
        else: pass

    def __set_time(self):
        # Double under score ensures the method is
        # private, used for the sake of information hiding.
 
        self.start_time = time.time()

    def __reset_time(self):

        self.start_time = 0
        pass
