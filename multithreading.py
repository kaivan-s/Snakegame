import threading
import time

class thred(threading.Thread):
    def __int__(self):
        self.start()


    def run(self,name):
        print("Starting Thread {} ".format(self.name))


