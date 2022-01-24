#!/bin/sh

log_init()
{
    today=`date`
    echo $today > /delayed_splash/splash.log
	#echo $today >> /delayed_splash/splash.log
}

# =====================================
# set lubuntu default video resolution
# =====================================
log_write()
{
    echo $@ >> /delayed_splash/splash.log
    echo $@ >&2
}

main ()
{
    log_init

	log_write "fbi ... png"
	sudo fbi -noverbose -T 1 -t 10 -cachemem 0 /delayed_splash/hub_background.png
    if [ $? -eq 0 ]
    then
        log_write "....OK - fbi ..."
        rtnvalue=0
    else
        log_write "....ERROR: fbi ..."
    fi

	# todo - switch to the veritual terminal
	
	log_write "waiting for hub app to bring up the web service"
	tries=0
	while [ $tries -lt 30 ]
	do
		# use curl to verify the service is up by getting supported species
		http_response=$(curl -s -o response.txt -w "%{http_code}" localhost:43002/species)
		if [ "$http_response" = "200" ]; then
			log_write "service is up"
			break
		else
			log_write "response: $http_response"
			log_write "timeout waiting for service"
			sudo fbi -noverbose -T 1 -t 1 -cachemem 0 /delayed_splash/hub_background.png
			sleep 1
			tries=`expr $tries + 1`
		fi
	done

	# todo close the fbi window
}


main


