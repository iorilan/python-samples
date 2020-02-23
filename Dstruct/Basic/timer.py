"generic code timer tool"
def test(reps, func, *args):        # or best of N? see Learning Python
    import time
    start = time.process_time()            # current CPU time in float seconds
    for i in range(reps):           # call function reps times
        func(*args)                 # discard any return value
    return time.process_time() - start     # stop time - start time
