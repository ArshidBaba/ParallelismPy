from threading import Thread


class Counter(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    # we start a Thread this run() function will be called
    def run(self):
        for i in range(100):
            print("%s thread is running: %s" % (self.name, str(i)))


t1 = Counter("#Thread1")
t2 = Counter("#Thread2")

t1.start()
t2.start()
