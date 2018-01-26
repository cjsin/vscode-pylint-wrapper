#!/usr/bin/python3
MAX_LIFE_SECONDS=120
MAXFD = 1024
REAL_EXEC="/usr/bin/pylint-3"

import os
import resource
import subprocess
import sys

def close_filedescriptors():
		# determine maximal file descriptor limit
		maxfd = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
		if (maxfd == resource.RLIM_INFINITY):
		    maxfd = MAXFD

    # close all file descriptors left over from the parent process
    # which didn't properly close them when executing this.
		for fd in range(3, maxfd):
		    try:
		        os.close(fd)
		    except OSError:
		        sys.stderr.write("error closing file: (%d) %s\n" % (e.errno, e.strerror))
		        pass


command = [ REAL_EXEC ] + sys.argv
subprocess.run(command, timeout=MAX_LIFE_SECONDS)

