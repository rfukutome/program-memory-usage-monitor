# TODO: log and do something with the return value (twitter bot?)
# Make function more dynamic

import psutil


def get_memory_utilization():
    '''
    Get the memory utilization of the PUBG video game,
    which runs as TslGame.exe.
    @todo: make this more dynamic
    @return: None
    @rtype: None
    '''
    for proc in psutil.process_iter():

        if proc.name() == 'TslGame.exe':
            process = psutil.Process(proc.pid)
            memory_usage = process.memory_percent()
            print('PUBG is using %.2f%% of your memory' % memory_usage)
            return
    else:
        print('PUBG is not running right now')


if __name__ == '__main__':
    get_memory_utilization()
