import threading, time

count = 0

def adder(addlock):
    global count
    with addlock:
        count += 1
        print('t=>',count)
    time.sleep(0.5)
    with addlock:
        count += 1
        print('t=>',count)

addlock = threading.Lock()
threads = []

for i in range(100):
    t = threading.Thread(target=adder, args=(addlock,))
    t.start()
    threads.append(t)

for t in threads: t.join()

print(count)