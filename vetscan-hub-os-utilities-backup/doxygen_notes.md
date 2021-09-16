-- stall
$ sudo apt-get install doxygen
$ sudo apt-get install doxygen-gui
$ sudo apt-get install graphviz

-- create initial doxygen config file
$ cd ~
$ mkdir vetscan_doxygen
$ cd vetscan_doxygen
$ doxygen -g vetscan.doxygen.config

-- edit config with Doxywizard
$ doxywizard &

-- run doxygen from the command line with the config
$ doxygen vetscan.doxygen.config

