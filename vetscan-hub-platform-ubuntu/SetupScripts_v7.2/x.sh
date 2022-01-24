#!/bin/sh

log_init()
{
    today=`date`
    echo $today > ./x.log
}

# =====================================
# set lubuntu default video resolution
# =====================================
log_write()
{
    echo $@ >> ./x.log
    echo $@ >&2
}

main ()
{
    log_init

	#sudo fbi -vt 1 /home/vetscan/delayed_splash/hub_background.png

	# display image for 10 seconds
	# sudo fbi -vt 1 -t 10 /home/vetscan/delayed_splash/hub_background.png

	# -noverbose no message at bottom of screen
	# sudo fbi -a -noverbose -norandom -T 1 -t 8 hub_background.png

	# sudo fbi -noverbose -T 1 -t 10 -cahcemem 0 /home/vetscan/delayed_splash/hub_background.png
	
	# does not cause logout
	# sudo fbi -noverbose -T 2 -t 10 -cachemem 0 /home/vetscan/delayed_splash/hub_background.png
	
	sudo fbi -noverbose -T 2 -t 10 -cachemem 0 /home/vetscan/delayed_splash/hub_background.png
	if [ $? -eq 0 ]
	then
		log_write "....OK - fbi ..."
		rtnvalue=0
	else
		log_write "....ERROR: fbi ..."
	fi
}

main
