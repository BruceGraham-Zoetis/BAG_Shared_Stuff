#!/bin/bash

function validate_YNQ {
   read -p "Copy over template file? Yes, No, Quit: Y N Q: " user_choice

   # Firstly Validate if any input field is left blank.
   # If not, display appropriate message and stop execution of script 
   if [ -z "$user_choice" ] 
   then 
     echo 'Inputs cannot be blank please try again' 
     exit 0 
   fi

   # Now Validate if the user input is YNQ.
   # If not, display appropriate message and stop execution of script 
   if [[ "$user_choice" == "Y" ]] || [[ "$user_choice" == "y" ]]
   then 
	echo "Y"
	exit 1
   elif [[ "$user_choice" == "N" ]] || [[ "$user_choice" == "n" ]]
   then
	echo "N"
	exit 1
   elif [[ "$user_choice" == "Q" ]] || [[ "$user_choice" == "q" ]]
   then
	echo "Q"
	exit 1
   else
        echo "?" 
        exit 1
   fi
}


function myBackupFunction {
    #echo " 2 $2"
    #echo " 1 $1"

    if cmp -s "$2" "$1"
    then
      echo "No diff $2"
      return 1
    fi
  
    echo "."
    echo "Files are different"
    echo "  $2"
    echo "  $1"
    echo "."
    
    while true; do
	result=$(validate_YNQ)
	if [[ $result == "Y" ]]
	then
	    cp -f "$2" "$1"
	    echo "Copied $2 to $1"
	    break
	elif [[ $result == "N" ]]
	then
	    echo "Skipped file"
	    break
	elif [[ $result == "Q" ]]
	then
	    echo "Quiting"
	    exit 1
	else
	    echo "Invalid input"
	fi
     done
}


declare -a arrFiles=(
	"AUTHORS.md;AUTHORS.md"
	"openapi_server/controllers/CDBusDraculaService.py;openapi_server/controllers/CDBusDraculaService.py"
	"openapi_server/controllers/measurement_channel_controller.py;openapi_server/controllers/measurement_channel_controller.py"
	"openapi_server/controllers/configuration_channel_controller.py;openapi_server/controllers/configuration_channel_controller.py"
	"openapi_server/controllers/security_controller_.py;openapi_server/controllers/security_controller_.py"
	"openapi_server/controllers/control_channel_controller.py;openapi_server/controllers/control_channel_controller.py"
	"openapi_server/controllers/status_channel_controller.py;openapi_server/controllers/status_channel_controller.py"
	"openapi_server/controllers/prompts_channel_controller.py;openapi_server/controllers/prompts_channel_controller.py"
	"openapi_server/models/analyzer_type.py;openapi_server/models/analyzer_type.py"
	"openapi_server/models/inline_object1.py;openapi_server/models/inline_object1.py"
	"openapi_server/models/inline_response2002.py;openapi_server/models/inline_response2002.py"
	"openapi_server/models/inline_response400.py;openapi_server/models/inline_response400.py"
	"openapi_server/models/base_model_.py;openapi_server/models/base_model_.py"
	"openapi_server/models/inline_object.py;openapi_server/models/inline_object.py"
	"openapi_server/models/inline_response2003.py;openapi_server/models/inline_response2003.py"
	"openapi_server/models/measurement_result.py;openapi_server/models/measurement_result.py"
	"openapi_server/models/event_info.py;openapi_server/models/event_info.py"
	"openapi_server/models/inline_response2001.py;openapi_server/models/inline_response2001.py"
	"openapi_server/models/inline_response200.py;openapi_server/models/inline_response200.py")

## now loop through the above array
for files in "${arrFiles[@]}"
do
   # echo "$files"
   arrFiles=$(echo $files | tr ";" "\n")
   #echo "$arrFiles"
   declare -i index=0
   for file in $arrFiles
   do
      if [[ $index == 0 ]]
      then
         fileTemplate="./templates/"$file
      else
         fileGenerated="./analyzer_app/"$file
      fi
      index=$((index + 1))
   done
   echo "$fileTemplate $fileGenerated"
   myBackupFunction "$fileTemplate" "$fileGenerated"
done



