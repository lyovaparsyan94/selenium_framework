import os
from time import sleep
from multiprocessing import Process, Pool


def run(phrase):
    os.environ['phrase'] = phrase
    sleep(2)
    return os.environ['phrase']


if __name__ == '__main__':
    with Pool() as pool:
        x = [pool.apply_async(run, args=(phrase, )) for phrase in ['hello', 'bye', 'abc']]
        for process in x:
            print(process.get())
