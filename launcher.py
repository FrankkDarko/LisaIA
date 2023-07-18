import asyncio

import lisa_bot
import lisa_web
import time
from multiprocessing import Process, set_start_method
from dotenv import load_dotenv
import os

# Load Token and api
load_dotenv()
token = os.environ['BOT_TOKEN']


# Process Lisa Web
def lisaweb():

    lisa_web.app.run(port=os.getenv("FLASK_PORT"), host=os.getenv("FLASK_HOST"))


# Process Lisa Bot
def lisabot():

    lisa_bot.client.run(token)


# entry point for the program
if __name__ == '__main__':

    set_start_method('spawn')
    # define a task to run in a new process
    p = Process(target=lisaweb)
    p2 = Process(target=lisabot)
    # start the task in a new process and sleep to prevent l og from mixing
    p.start()
    time.sleep(10)
    p2.start()