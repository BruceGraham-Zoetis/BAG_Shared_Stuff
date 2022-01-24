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

main ()
{
    log_init

	# log_write "fbi ... png"
	# sudo fbi -noverbose -T 1 -t 10 -cachemem 0 /delayed_splash/hub_background.png
    #if [ $? -eq 0 ]
    #then
    #    log_write "....OK - fbi ..."
    #    rtnvalue=0
    #else
    #    log_write "....ERROR: fbi ..."
    #fi

	# todo - switch to the veritual terminal
	
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
	
	today=`date`
    log_write $today

	# TODO -o /dev/null
	http_response=$(sudo /usr/bin/curl -s -o response.txt -w "%{http_code}" localhost:43002/species)
	if [ "$http_response" = "200" ]; then
		log_write "service is up"
	else
		log_write "timed out waiting for service"
	fi
}


main


