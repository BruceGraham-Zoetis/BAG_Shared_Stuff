#!/bin/bash

function validate_YNQ {
   read -p "Copy modified generated files to template directory? Yes, No: " user_choice

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


fileGenerated="./analyzer_app"
fileTemplate="./templates"

while true; do
	result=$(validate_YNQ)
	if [[ $result == "Y" ]]
	then
	    echo "cp $fileGenerated/AUTHORS.md $fileTemplate/AUTHORS.md"
	    cp $fileGenerated/AUTHORS.md $fileTemplate/AUTHORS.md
	    echo .
	    echo "cp $fileGenerated/openapi_server/controllers/*.py $fileTemplate/openapi_server/controllers"
	    cp $fileGenerated/openapi_server/controllers/*.py $fileTemplate/openapi_server/controllers
	    echo .
	    echo "cp $fileGenerated/openapi_server/models/*.py $fileTemplate/openapi_server/models"
	    cp $fileGenerated/openapi_server/models/*.py $fileTemplate/openapi_server/models
	    echo .	    
	    echo "cp $fileGenerated/openapi_server/test/*.py $fileTemplate/openapi_server/test"
	    cp $fileGenerated/openapi_server/test/*.py $fileTemplate/openapi_server/test
	    echo "Completed."
	    break
	elif [[ $result == "N" ]]
	then
	    echo "Cancelled"
	    exit 1
	else
	    echo "Invalid input"
	fi
done



