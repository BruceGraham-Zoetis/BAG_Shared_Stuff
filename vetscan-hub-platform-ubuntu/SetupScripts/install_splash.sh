#!/bin/sh

# =====================================================
# File: install_splash.sh
#
# Purpose: This shell script will install the
#   splash screen for the Vetscan.
#
# Installed files
# -----------------------------
# Directory: files\usr\share\plymouth\themes\vetscan_splash
#	LOGO.PNG
#		1920x1080 image that is transparent.
#       This file is used in vetscan_splash.script to
#		calculate positions of the other images.
#   hub_background.png
#		The Hub Logo file
#   BOX.PNG, LOCK.PNG, THROBBER_BACK.PNG, BULLET.PNG
#   THROBBER_FORE.PNG, ENTRY.PNG, PROGRESS_FADE.PNG
#		Images for the progress bar.
#   vetscan_splash.plymouth
#		The plymouth configuration file that specifies
#		the script to execute.
#   vetscan_splash.script
#		The script to execute that displays the images.
#
# Directory: files\etc\default
#	grub (not used)
#		A grub file that can get grub to display the
#		hub_background.png when grub loads Linux.
#
# Directory: files\.config\lxsession/Lubuntu
#	autostart
#		A configuration file for setting graphics mode
#		at boot time.

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
# set lubuntu default video resolution
# =====================================
set_video_resolution()
{
    # create file /home/{user}/.config/lxsession/Lubuntu/autostart

    if [ ! -f ~/.config/lxsession/Lubuntu/autostart ]
    then
        log_write "Creating ~/.config/lxsession/Lubuntu/autostart"

        # sudo mkdir -p ~/.config/lxsession/Lubuntu
        # touch ~/.config/lxsession/Lubuntu/autostart
        # tried resolution settings:
        # xrandr -s {1920x1080} -r 60
        # xrandr --output HDMI-0 --mode 1920x1080 -r 60
        # echo "xrandr --output HDMI-0 --mode 1920x1080 -r 60" >> ~/.config/lxsession/Lubuntu/autostart

        log_write "Copying autostart file"
        sudo mkdir -p ~/.config/lxsession/Lubuntu
        sudo cp ./files/.config/lxsession/Lubuntu/autostart ~/.config/lxsession/Lubuntu/autostart

        if [ $? -eq 0 ]
        then
            log_write "OK - Copying autostart file"
            rtnvalue=0
        else
            log_write "ERROR: Copying autostart file failed"
        fi
    else
        rtnvalue=0
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


main ()
{
    log_init

    set_video_resolution

    if [ 0 -eq $rtnvalue ]
    then
        install_plymouth
    fi

    if [ 0 -eq $rtnvalue ]
    then
        copy_vetscan_splash
    fi

    if [ 0 -eq $rtnvalue ]
    then
        setup_vetscan_splash
    fi

    if [ 0 -eq $rtnvalue ]
    then
        log_write "End with SUCCESS"
        exit 0
    else
        log_write "End with ERROR"
        exit 1
    fi
}

main
