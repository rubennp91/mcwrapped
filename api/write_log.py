from datetime import datetime
import os


def write_log(message, logfile=None):
    if logfile:
        with open(logfile, 'a') as f:
            f.write(message + "\n")
    else:
        logfile = './logs/' + str(datetime.now().strftime("%d%m%Y")) + '.txt'
        if os.path.isfile(logfile):
            with open(logfile, 'a') as f:
                f.write(message + "\n")
        else:
            with open(logfile, 'w') as f:
                f.write(message + "\n")
