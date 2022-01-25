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

# =====================================
# setup grub with splash image
# =====================================
setup_grub_with_splash ()
{
	log_write "copy the image to the grub directory."
	sudo cp ./files/usr/share/plymouth/themes/vetscan_splash/hub_background.png /boot/grub/hub_background.png
	if [ $? -eq 0 ]
	then
		log_write "....OK - cp ...hub_background.png"
		rtnvalue=0
	else
		log_write "....ERROR: cp ...hub_background.png"
		rtnvalue=1
	fi
	
	if [ 0 -eq $rtnvalue ]
    then
        log_write "update-grub"
		sudo update-grub
		if [ $? -eq 0 ]
		then
			log_write "....OK - update-grub"
			rtnvalue=0
		else
			log_write "....ERROR: update-grub"
			rtnvalue=1
		fi
	fi
}

# =====================================
# Copy files used by the delayed_splash
# =====================================
copy_delayed_splash_files ()
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

# =====================================
# Install plymouth
# =====================================
install_plymouth()
{
#    if [ ! -f /usr/share/plymouth/themes/default.plymouth ]
#    then
        # Update the package index:
        sudo apt-get update

        # Install plymouth deb packages
        sudo apt-get install plymouth
        sudo apt-get install plymouth-x11
        if [ ! -f /usr/share/plymouth/themes/default.plymouth ]
        then
            log_write "File does not exist: /usr/share/plymouth/themes/default.plymouth"
            log_write "ERROR: plymouth is not installed."
            rtnvalue=1
        else
            log_write "OK - Plymouth is installed."
            rtnvalue=0
        fi
#    else
#        rtnvalue=0
#    fi
}

# =====================================
# Copy the vetscan splash
# =====================================
copy_vetscan_splash()
{
    rtnvalue=1

    log_write "Copying vetscan splash files"
    sudo cp -r ./files/usr/share/plymouth/themes/vetscan_splash /usr/share/plymouth/themes/
    if [ $? -eq 0 ]
    then
        log_write "OK - Copying vetscan splash files"
        rtnvalue=0
    else
        log_write "ERROR: Copying vetscan splash files"
    fi
}

# =====================================
# Setup the vetscan splash as the default
# =====================================
setup_vetscan_splash()
{
    rtnvalue=1

    log_write "update-alternatives --install ... "
    # update-alternatives --install <link> <name> <path> <priority>
    # Note vetscan_splash needs to be set with the highest priority (200)
    sudo update-alternatives --install /usr/share/plymouth/themes/default.plymouth default.plymouth /usr/share/plymouth/themes/vetscan_splash/vetscan_splash.plymouth 200
    if [ $? -eq 0 ]
    then
        log_write "OK - update-alternatives --install ..."
        rtnvalue=0
    else
        log_write "ERROR: update-alternatives --install ..."
        rtnvalue=1
    fi

    if [ 0 -eq $rtnvalue ]
    then
        log_write "update-initramfs -u"
        sudo update-initramfs -u
        if [ $? -eq 0 ]
        then
            log_write "OK - update-initramfs -u"
            rtnvalue=0
        else
            log_write "ERROR: update-initramfs -u"
            rtnvalue=1
        fi
    fi
}

# =====================================
# install the service for starting the delayed_splash
# =====================================
install_service ()
{
	sudo chmod +x /delayed_splash/delayed_splash_exec.sh
	if [ $? -eq 0 ]
	then
		log_write "....OK - chmod +x delayed_splash_exec.sh"
		rtnvalue=0
	else
		log_write "....ERROR: chmod +x delayed_splash_exec.sh"
		rtnvalue=1
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
}

# =====================================
# Install gnome extension
# =====================================
install_gnome_extension ()
{
	sudo apt install gnome-shell-extension-prefs
	if [ $? -eq 0 ]
	then
		log_write "....OK - install gnome extension"
		rtnvalue=0
	else
		log_write "....ERROR: install gnome extension"
		rtnvalue=1
	fi
}

# =====================================
# Disable desktop icons, dock, app indicators
# =====================================
disable_desktop_icons_etc ()
{
	gnome-extensions disable desktop-icons@csoriano
	if [ $? -eq 0 ]
	then
		log_write "....OK - disable desktop-icons@csoriano"
		rtnvalue=0
	else
		log_write "....ERROR: disable desktop-icons@csoriano"
		rtnvalue=1
	fi

	gnome-extensions disable ubuntu-appindicators@ubuntu.com
	if [ $? -eq 0 ]
	then
		log_write "....OK - disable ubuntu-appindicators@ubuntu.com"
		rtnvalue=0
	else
		log_write "....ERROR: disable ubuntu-appindicators@ubuntu.com"
		rtnvalue=1
	fi

	gnome-extensions disable ubuntu-dock@ubuntu.com
	if [ $? -eq 0 ]
	then
		log_write "....OK - disable ubuntu-dock@ubuntu.com"
		rtnvalue=0
	else
		log_write "....ERROR: disable ubuntu-dock@ubuntu.com"
		rtnvalue=1
	fi
}

# =====================================
# Modify the default Ubuntu plymouth splash
# =====================================
modify_ubuntu_plymouth_splash ()
{
	if [ -f /usr/share/plymouth/themes/spinner/watermake.png ]
	then
		# the watermake.png file contains the Ubuntu logo.
		# rename the watermake.png file so that it is not displayed.
		sudo mv /usr/share/plymouth/themes/spinner/watermake.png /usr/share/plymouth/themes/spinner/watermake.png.org
		if [ $? -eq 0 ]
		then
			log_write "....OK - mv ...watermake.png"
			rtnvalue=0
		else
			log_write "....ERROR: mv ...watermake.png"
			rtnvalue=1
		fi
	else
		log_write "....OK - watermake.png"
		rtnvalue=0
	fi
}

main ()
{
    log_init

	setup_grub_with_splash
	
    if [ 0 -eq $rtnvalue ]
    then
		modify_ubuntu_plymouth_splash
	fi
	
    if [ 0 -eq $rtnvalue ]
    then
		echo ....skipping copy_delayed_splash_files
	fi
	
    if [ 0 -eq $rtnvalue ]
    then
		echo ....skipping install_service
	fi
	
    if [ 0 -eq $rtnvalue ]
    then
        echo ....skipping install_plymouth
    fi

    if [ 0 -eq $rtnvalue ]
    then
        echo ....skipping copy_vetscan_splash
    fi

    if [ 0 -eq $rtnvalue ]
    then
        echo ....skipping setup_vetscan_splash
    fi
	
    if [ 0 -eq $rtnvalue ]
    then
        install_gnome_extension
    fi

    if [ 0 -eq $rtnvalue ]
    then
        disable_desktop_icons_etc
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
