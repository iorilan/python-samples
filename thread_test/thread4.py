import _thread as thread, time


def bgWork():
    counter = 0
    while True:
        time.sleep(1)
        print(counter)
        counter += 1
        if counter % 10 == 0:
            print ("doing something")
        
thread.start_new_thread(bgWork,())

print("press enter to exit.")
input()
