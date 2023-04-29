import itertools
import threading
import time
import sys

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['.', '..', '...']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.3)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

time.sleep(10)
done = True