it's appeared to be an issue with the network printers. any printer to be seen by JRE has to be in "shared" state. unfortunately network printers aren't. the only option so far is to install cups-pdf bridge and print from Java glovebox through PDF exported file (printed by "local" PDF sink appeared in the configuration after installing cups-pdf).

the command for installing necessary cups-pdf sink:

sudo apt-get install cups-pdf
next, System Settings->Printers->PDF->->Shared (enable checkbox)
