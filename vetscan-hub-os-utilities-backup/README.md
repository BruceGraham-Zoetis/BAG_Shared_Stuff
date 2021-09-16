# vetscan-hub-os-utilities
Operating system utilities scripts for the vetscan hub operating system

## Utility Requirements
The following list of requirements describes how the utilities shall be structured and implemented:
1. Utilities shall be implemented as a single python module.
2. Utilities shall contain a requirements.txt file that lists all dependencies such that a single "pip3 install -r requirements.txt" will install all dependencies.
3. Utilities shall be grouped one per file in this directory.
4. Each function shall have a function header describing all inputs and outputs as well as providing a basic description of functionality.
5. Each function that is intended to be called externally shall have testing implemented in test.py in the top level of the repository.
6. All python dependencies shall be listed in the repository requirements.txt file.
7. All utility functions shall be implemented synchronously.

## Utility List
The following list details the different utilities contained in this repository:
1. audio-control
   1. set_percent - function to set the master volume for the system
   2. get_percent - function to get the master volume for the system
2. wifi-control
3. screen-brightness-control
4. print-utility
5. play-sound
6. scan-QR
7. network-control