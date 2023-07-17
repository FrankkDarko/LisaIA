import lisa_bot
import lisa_web
import time
from multiprocessing import Process


# Process Lisa Web
def lisaweb():

    lisa_web.starter()


# Process Lisa Bot
def lisabot():

    lisa_bot.starter()


# entry point for the program
if __name__ == '__main__':

    # define a task to run in a new process
    p = Process(target=lisaweb)
    p2 = Process(target=lisabot)
    # start the task in a new process and sleep to prevent l og from mixing
    p.start()
    time.sleep(10)
    p2.start()
    # wait for the task to complete
    p.join()
    p2.join()
