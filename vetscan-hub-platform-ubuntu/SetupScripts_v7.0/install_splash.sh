#!/bin/sh

# =====================================================
# File: install_splash.sh
#
# Purpose: This shell script will install the
#   splash screen for the Vetscan.
#
# Installed files
# -----------------------------
# Directory: .
#   hub_background.png
#		The Hub Logo file
#

# =====================================================

rtnvalue=1 # 0 = success, 1 == error

# =====================================
# Init the log file
# =====================================
log_init()
{
    today=`date`
    echo $today > ./install_splash.log
}

# =====================================
# set lubuntu default video resolution
# =====================================
log_write()
{
    echo $@ >> ./install_splash.log
    echo $@ >&2
}

copy_files ()
{
    rtnvalue=1

	# Copy delayed_splash_exec.sh
    if [ ! -d /delayed_splash ]
    then
		sudo mkdir /delayed_splash
		if [ $? -eq 0 ]
		then
			log_write "....OK - Creating /delayed_splash"
			rtnvalue=0
		else
			log_write "....ERROR: Creating /delayed_splash"
		fi
		
		sudo chown vetscan:vetscan /delayed_splash
	fi
	
	# delayed_splash_exec.sh will display the splash screen
	# while the hub app is starting up.
	sudo cp ./delayed_splash_exec.sh /delayed_splash/
    if [ $? -eq 0 ]
    then
        log_write "....OK - Copying delayed_splash_exec.sh"
        rtnvalue=0
    else
        log_write "....ERROR: Copying delayed_splash_exec.sh"
    fi
	
	# The image to display.
	sudo cp ./hub_background.png /delayed_splash/
    if [ $? -eq 0 ]
    then
        log_write "....OK - Copying hub_background.png"
        rtnvalue=0
    else
        log_write "....ERROR: Copying hub_background.png"
    fi
}


main ()
{
    log_init
	
	copy_files
	
    if [ 0 -eq $rtnvalue ]
    then
		sudo chmod +x /delayed_splash/delayed_splash_exec.sh
		if [ $? -eq 0 ]
		then
			log_write "....OK - chmod +x delayed_splash_exec.sh"
			rtnvalue=0
		else
			log_write "....ERROR: chmod +x delayed_splash_exec.sh"
			rtnvalue=1
		fi
	fi

    if [ 0 -eq $rtnvalue ]
    then
		# Copy delayed_splash.service into the /etc/systemd/system folder.
		# It will be executed during Linux startup and will startup
		# delayed_splash_exec.sh
		sudo cp ./delayed_splash.service /etc/systemd/system
		if [ $? -eq 0 ]
		then
			log_write "....OK - Copying delayed_splash.service"
			rtnvalue=0
		else
			log_write "....ERROR: Copying delayed_splash.service"
			rtnvalue=1
		fi
	fi

    if [ 0 -eq $rtnvalue ]
    then
		# Set the file permissions to 644 and enable our service by using systemctl:
		sudo chmod 644 /etc/systemd/system/delayed_splash.service
		sudo systemctl enable delayed_splash.service
		if [ $? -eq 0 ]
		then
			log_write "....OK - update-rc.d"
			rtnvalue=0
		else
			log_write "....ERROR: update-rc.d"
			rtnvalue=1
		fi
	fi

    if [ 0 -eq $rtnvalue ]
    then
		log_write "-------------------------------"
        log_write "SUCCESS - Completed"
		log_write "-------------------------------"
        exit 0
    else
		log_write "-------------------------------"
        log_write "ERROR - Not completed"
		log_write "-------------------------------"
        exit 1
    fi
}

main
