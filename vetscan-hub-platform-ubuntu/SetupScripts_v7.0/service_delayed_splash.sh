#!/bin/sh
# chkconfig: 345 99 10
case "$1" in
  start)
    # Executes our script
    sudo sh /home/vetscan/delayed_splash_exec.sh
    ;;
  *)
    ;;
esac
exit 0
