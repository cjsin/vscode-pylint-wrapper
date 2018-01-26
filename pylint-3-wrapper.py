#!/usr/bin/python3
import os
import resource
import subprocess
import sys

MAX_LIFE_SECONDS=120
REAL_EXEC="/usr/bin/pylint-3"
MAXFD = 1024

def close_filedescriptors():
    # determine maximal file descriptor limit
    maxfd = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
    if maxfd == resource.RLIM_INFINITY:
        maxfd = MAXFD

    # close all file descriptors left over from the parent process
    # which didn't properly close them when executing this.
    for fd in range(6, maxfd):
        try:
            os.close(fd)
        except OSError:
            pass

close_filedescriptors()

command = [ REAL_EXEC ] + sys.argv

subprocess.run(command, timeout=MAX_LIFE_SECONDS)
