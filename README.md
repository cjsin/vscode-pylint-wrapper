# vscode-pylint-wrapper
Wrapper for executing pylint in vscode to avoid hung processes and runaway memory usage

When using pylint with vscode, it seems to suffer from two problems:

   - the pylint processes never exit, leading to hundreds or thousands of pylint processes after a few hours
   - the pylint processes themselves, or else the vscode javascript extension which is executing them, consumes more and more memory, leading to an eventual hang as the linux out of memory handler kicks in to kill every *other* process running on the system, for the sake of the pylint processes.
   
This repo provides a simple wrapper script which does two things:
  - close all file descriptors except useful ones (stdin,stderr,stdout) immediately
  - execute the 'real' pylint3 process, with a timeout, so that it will be killed if it does not exit in a timely manner.
  
To use this wrapper with vscode:

  - Save the pylint-3-wrapper.py file somewhere on your system
  - Run chmod +rx pylint-3-wrapper.py
  - In your VSCode user settings, set property 'python.linting.pylintPath' to the path of the wrapper script.
  
 
Example vscode settings for pylint-3

{ 
    "python.linting.pylintPath":"/usr/bin/pylint-3",
    "python.linting.pylintArgs": [
        "-j","10",
        "-d","C0303",
    ],
}
