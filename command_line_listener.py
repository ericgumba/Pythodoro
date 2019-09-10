import time
from multiprocessing import Process, Value 
class CommandLineListener:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def test_f(self):
        ct = []

        while True:

            k = input()

            if k == 'p':
                print("play")
            if k == 's':
                print("skip")


class Runner:
    def __init__(self, ctr): 
        self.ctr = ctr


    def worker(self, val):
        def runTimer():
            self.ctr += 1
            print("    ", self.ctr)
            time.sleep(1)

        while True:
            if run.value:
                runTimer()
            

if __name__ == "__main__": 
 
    A = Runner(0)
    run = Value("i", 1) 
    print("RUN VALUE    ", run)
 
    p = Process(target=A.worker, args=(run,)) 
    p.start() 

    while True: 
        if a == "p":
            run.value = not run.value
 
# import keyboard #Using module keyboard
# while True:  #making a loop
#     try:  #used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('up'): #if key 'up' is pressed.You can use right,left,up,down and others
#             print('You Pressed A Key!')
#             break #finishing the loop
#         else:
#             pass
#     except:
#         break  #if user pres