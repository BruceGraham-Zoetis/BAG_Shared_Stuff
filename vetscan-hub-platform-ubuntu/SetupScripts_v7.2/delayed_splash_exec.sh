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
    #echo $@ >&2
}

wait_for_web_service ()
{
	
	export OPENSSL_CONF=/etc/ssl/openssl.cnf
	
	log_write "waiting for hub app to bring up the web service"
	tries=0
	while [ $tries -lt 12 ] # 12x5=60=1 minute
	do
		# use curl to verify the service is up by getting supported species
		# TODO -o /dev/null
		sudo /usr/bin/curl -s -w "%{http_code}" localhost:43002/species >> /delayed_splash/out.txt
		log_write "curl rtn: $?"
		http_response=$(sudo /usr/bin/curl -s -o response.txt -w "%{http_code}" localhost:43002/species)
		log_write "response: $http_response"
		if [ "$http_response" = "200" ]; then
			break
		else
			# sudo fbi -noverbose -T 1 -t 1 -cachemem 0 /delayed_splash/hub_background.png
			sleep 5
			tries=`expr $tries + 1`
		fi
	done


	# TODO -o /dev/null
	http_response=$(sudo /usr/bin/curl -s -o response.txt -w "%{http_code}" localhost:43002/species)
	if [ "$http_response" = "200" ]; then
		log_write "service is up"
	else
		log_write "timed out waiting for service"
	fi
}

run_eog ()
{
	# log_write "eog ... png"
	sudo eog -f -w -g /delayed_splash/hub_background.png &
    if [ $? -eq 0 ]
    then
        log_write "....OK - eog ..."
        rtnvalue=0
    else
        log_write "....ERROR: eog ..."
    fi
}

run_feh ()
{
	# log_write "feh ... png"
	sudo feh --auto-zoom --fullscreen /delayed_splash/hub_background.png &
    if [ $? -eq 0 ]
    then
        log_write "....OK - feh ..."
        rtnvalue=0
    else
        log_write "....ERROR: feh ..."
    fi
}


main ()
{
    log_init

	# run_eog
	run_feh
	
	# wait_for_web_service

	today=`date`
    log_write $today
}

main


