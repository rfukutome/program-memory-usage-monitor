# TODO: log and do something with the return value (twitter bot?)
# Make function more dynamic

import time
import psutil

MEMORY_USAGE = []

def get_memory_utilization(pubg_not_running_count):
    '''
    Get the memory utilization of the PUBG video game,
    which runs as TslGame.exe.
    @todo: make this more dynamic
    @param pubg_not_running_count: number of times this has been called and pubg wasn't running
    @type pubg_not_running_count: int
    @return: an updated pubg_not_running_count (+1 if not running, reset to 0 if running)
    @rtype: int
    '''
    for proc in psutil.process_iter():

        if proc.name() == 'TslGame.exe':
            process = psutil.Process(proc.pid)
            memory_usage = process.memory_percent()
            print('PUBG is using %.2f%% of your memory' % memory_usage)
            MEMORY_USAGE.append(memory_usage)
            return 0

    print('PUBG is not running right now')
    return pubg_not_running_count + 1


if __name__ == '__main__':
    pubg_not_running_count = 0
    try:
        while True and pubg_not_running_count < 2:
            pubg_not_running_count = get_memory_utilization(pubg_not_running_count)
            time.sleep(10)
    except KeyboardInterrupt:
        print('Quitting the program')

    print(MEMORY_USAGE)
