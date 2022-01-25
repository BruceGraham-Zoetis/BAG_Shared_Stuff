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
setup_grub_with_splash()
{
	log_write "setup_grub_with_splash()"
	rtnvalue=0

	sudo cp ./files/usr/share/plymouth/themes/vetscan_splash/hub_background.png /boot/grub/hub_background.png
	if [ $? -eq 0 ]
	then
		log_write "....OK: cp ...hub_background.png"
	else
		log_write "....ERROR: cp ...hub_background.png"
		rtnvalue=1
	fi
	
	if [ $rtnvalue -eq 0 ]
    then
        log_write "update-grub"
		sudo update-grub
		if [ $? -eq 0 ]
		then
			log_write "....OK: update-grub"
		else
			log_write "....ERROR: update-grub"
			rtnvalue=1
		fi
	fi
}

# =====================================
# Copy files used by the delayed_splash
# =====================================
copy_delayed_splash_files()
{
	log_write "copy_delayed_splash_files()"
    rtnvalue=0

	# Copy delayed_splash_exec.sh
    if [ ! -d /delayed_splash ]
    then
		sudo mkdir /delayed_splash
		if [ $? -eq 0 ]
		then
			log_write "....OK: Creating /delayed_splash"
		else
			log_write "....ERROR: Creating /delayed_splash"
			rtnvalue=1
		fi
		
		sudo chown vetscan:vetscan /delayed_splash
	fi
	
	# delayed_splash_exec.sh will display the splash screen
	# while the hub app is starting up.
	sudo cp ./delayed_splash_exec.sh /delayed_splash/
    if [ $? -eq 0 ]
    then
        log_write "....OK: Copying delayed_splash_exec.sh"
    else
        log_write "....ERROR: Copying delayed_splash_exec.sh"
		rtnvalue=1
    fi
	
	# The image to display.
	sudo cp ./hub_background.png /delayed_splash/
    if [ $? -eq 0 ]
    then
        log_write "....OK: Copying hub_background.png"
    else
        log_write "....ERROR: Copying hub_background.png"
		rtnvalue=1
    fi
}

# =====================================
# Install plymouth
# =====================================
install_plymouth()
{
	log_write "install_plymouth()"
	rtnvalue=0

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
            log_write "....ERROR: plymouth is not installed."
            rtnvalue=1
        else
            log_write "....OK: Plymouth is installed."
        fi
#    fi
}

# =====================================
# Copy the vetscan splash
# =====================================
copy_vetscan_splash()
{
	log_write "copy_vetscan_splash()"
    rtnvalue=0

    sudo cp -r ./files/usr/share/plymouth/themes/vetscan_splash /usr/share/plymouth/themes/
    if [ $? -eq 0 ]
    then
        log_write "....OK: Copying vetscan splash files"
    else
        log_write "....ERROR: Copying vetscan splash files"
		rtnvalue=1
    fi
}

# =====================================
# Setup the vetscan splash as the default
# =====================================
setup_vetscan_splash()
{
	log_write "setup_vetscan_splash()"
    rtnvalue=0

    # update-alternatives --install <link> <name> <path> <priority>
    # Note vetscan_splash needs to be set with the highest priority (200)
    sudo update-alternatives --install /usr/share/plymouth/themes/default.plymouth default.plymouth /usr/share/plymouth/themes/vetscan_splash/vetscan_splash.plymouth 200
    if [ $? -eq 0 ]
    then
        log_write "....OK: update-alternatives --install ..."
    else
        log_write "....ERROR: update-alternatives --install ..."
        rtnvalue=1
    fi

    if [ 0 -eq $rtnvalue ]
    then
        log_write "update-initramfs -u"
        sudo update-initramfs -u
        if [ $? -eq 0 ]
        then
            log_write "....OK: update-initramfs -u"
        else
            log_write "....ERROR: update-initramfs -u"
            rtnvalue=1
        fi
    fi
}

# =====================================
# install the service for starting the delayed_splash
# =====================================
install_service()
{
	log_write "install_service()"
	rtnvalue=0

	sudo chmod +x /delayed_splash/delayed_splash_exec.sh
	if [ $? -eq 0 ]
	then
		log_write "....OK: chmod +x delayed_splash_exec.sh"
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
			log_write "....OK: Copying delayed_splash.service"
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
			log_write "....OK: update-rc.d"
		else
			log_write "....ERROR: update-rc.d"
			rtnvalue=1
		fi
	fi
}

# =====================================
# Install gnome extension
# =====================================
install_gnome_extension()
{
	log_write "install_gnome_extension()"
	rtnvalue=0

	sudo apt install gnome-shell-extension-prefs
	if [ $? -eq 0 ]
	then
		log_write "....OK: install gnome extension"
	else
		log_write "....ERROR: install gnome extension"
		rtnvalue=1
	fi
}

# =====================================
# Disable desktop icons, dock, app indicators
# =====================================
disable_desktop_icons_etc()
{
	log_write "disable_desktop_icons_etc()"
	rtnvalue=0
	
	gnome-extensions disable desktop-icons@csoriano
	if [ $? -eq 0 ]
	then
		log_write "....OK: disable desktop-icons@csoriano"
	else
		log_write "....ERROR: disable desktop-icons@csoriano"
		rtnvalue=1
	fi

	gnome-extensions disable ubuntu-appindicators@ubuntu.com
	if [ $? -eq 0 ]
	then
		log_write "....OK: disable ubuntu-appindicators@ubuntu.com"
	else
		log_write "....ERROR: disable ubuntu-appindicators@ubuntu.com"
		rtnvalue=1
	fi

	gnome-extensions disable ubuntu-dock@ubuntu.com
	if [ $? -eq 0 ]
	then
		log_write "....OK: disable ubuntu-dock@ubuntu.com"
	else
		log_write "....ERROR: disable ubuntu-dock@ubuntu.com"
		rtnvalue=1
	fi
}

# =====================================
# Modify the default Ubuntu plymouth splash
# =====================================
modify_ubuntu_plymouth_splash()
{
	log_write "modify_ubuntu_plymouth_splash()"
	rtnvalue=0

	if [ -f /usr/share/plymouth/themes/spinner/watermake.png ]
	then
		# the watermake.png file contains the Ubuntu logo.
		# rename the watermake.png file so that it is not displayed.
		sudo mv /usr/share/plymouth/themes/spinner/watermake.png /usr/share/plymouth/themes/spinner/watermake.png.org
		if [ $? -eq 0 ]
		then
			log_write "....OK: mv ...watermake.png"
		else
			log_write "....ERROR: mv ...watermake.png"
			rtnvalue=1
		fi
	else
		log_write "....OK: watermake.png"
	fi
}

# =====================================
# Copy autostart files
# =====================================
copy_autostart_files()
{
	log_write "copy_autostart_files()"
    rtnvalue=0

    sudo cp -r ./files/.config/autostart/bootScreen.desktop /home/vetscan/.config/autostart/bootScreen.desktop
    if [ $? -eq 0 ]
    then
        log_write "....OK: Copied bootScreen.desktop"
    else
        log_write "....ERROR: Copying bootScreen.desktop"
		rtnvalue=1
    fi
	
    if [ $rtnvalue -eq 0 ]
    then
		sudo chmod 755 /home/vetscan/.config/autostart/bootScreen.desktop
		if [ $? -eq 0 ]
		then
			log_write "....OK: chmod 755 ...bootScreen.desktop"
		else
			log_write "....ERROR: chmod 755 ...bootScreen.desktop"
			rtnvalue=1
		fi
	fi
	
    if [ $rtnvalue -eq 0 ]
		then
		sudo cp -r ./files/Desktop/Screen_3.jpg /home/vetscan/Desktop/Screen_3.jpg
		if [ $? -eq 0 ]
		then
			log_write "....OK: Copied Screen_3.jpg"
		else
			log_write "....ERROR: Copying Screen_3.jpg"
			rtnvalue=1
		fi
	fi

    if [ $rtnvalue -eq 0 ]
    then
		sudo cp -r ./files/Desktop/kiosk.sh /home/vetscan/Desktop/kiosk.sh
		if [ $? -eq 0 ]
		then
			log_write "....OK: Copied kiosk.sh"
		else
			log_write "....ERROR: Copying kiosk.sh"
			rtnvalue=1
		fi
	fi
	
    if [ $rtnvalue -eq 0 ]
    then
		sudo chmod 775 /home/vetscan/Desktop/kiosk.sh
		if [ $? -eq 0 ]
		then
			log_write "....OK: chmod 775 ...kiosk.sh"
		else
			log_write "....ERROR: chmod 775 ...kiosk.sh"
			rtnvalue=1
		fi
	fi

}

# =====================================
# Set the desktop's background color to white
# =====================================
set_desktop_background_color()
{
	log_write "copy_autostart_files()"
    rtnvalue=1

    sudo gsettings set org.gnome.desktop.background secondary-color '#000000'
    if [ $? -eq 0 ]
    then
        log_write "....OK: gsettings ...background color"
        rtnvalue=0
    else
        log_write "....ERROR: gsettings ...background color"
		rtnvalue=1
    fi
}

# =====================================
# Set the desktop's background image
# =====================================
set_desktop_background_picture()
{
	log_write "set_desktop_background_picture()"
    rtnvalue=1

	sudo cp -r ./files/Desktop/Screen_2.gif /home/vetscan/Desktop/Screen_2.gif
	if [ $? -eq 0 ]
	then
		log_write "....OK: Copied Screen_2.gif"
		rtnvalue=0
	else
		log_write "....ERROR: Copying Screen_2.gif"
		rtnvalue=1
	fi

	if [ $rtnvalue -eq 0 ]
	then
		sudo gsettings set org.gnome.desktop.background picture-uri /home/vetscan/Desktop/Screen_2.gif 
		if [ $? -eq 0 ]
		then
			log_write "....OK: gsettings ...background picture"
			rtnvalue=0
		else
			log_write "....ERROR: gsettings ...background picture"
			rtnvalue=1
		fi
	fi
}

main()
{
    log_init

	setup_grub_with_splash
	
    if [ 0 -eq $rtnvalue ]
    then
		modify_ubuntu_plymouth_splash
	fi
	
    if [ 0 -eq $rtnvalue ]
    then
		copy_autostart_files
	fi
	
    if [ 0 -eq $rtnvalue ]
    then
		set_desktop_background_color
	fi
	
    if [ 0 -eq $rtnvalue ]
    then
		set_desktop_background_picture
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
