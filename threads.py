import threading


# so the MainThread will run everything sequentially
# all other threads are created by the MaiunThread (application thread)
def count_operation():
    for i in range(100):
        print(threading.current_thread().name + " - " + str(i))


# This is sequential execution - operations right after each other
count_operation()
count_operation()

t1 = threading.Thread(target=count_operation, name="Adam")
t2 = threading.Thread(target=count_operation, name="Joe")

t1.start()
t2.start()
