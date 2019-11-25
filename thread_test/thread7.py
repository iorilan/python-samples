import threading , time

count = 0

def adder():
    global count
    count += 1
    time.sleep(0.5)
    count += 1
    print('t=>',count)

threads = []
for i in range(100):
    thread = threading.Thread(target=adder, args=())
    thread.start()
    threads.append(thread)

for t in threads: t.join()

print(count)