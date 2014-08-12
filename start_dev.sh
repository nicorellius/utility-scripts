#!/bin/bash

project=$1

echo "starting apache and mysql..."

bash /home/nick/dev/lamp/ctlscript.sh start

echo "determining project and working directories..."

if [ "${project}" == "aersol" ]; 
then
    echo "project is ${project} ... using alias aproj..."
    aproj
    settings="${project}.settings.local"

elif [ "${project}" == "serupbot" ]; 
then
    echo "project is ${project} ... using alias sproj..."
    sproj
    settings=""

else
    echo "project is ${project} ... using alias fproj..."
    fproj
    settings=""
fi

function start_server {
    
    if [ "${settings}" != "" ];
    then
        args="--settings=${settings}"
        echo "args for ${project} are ${args}"

    else
        args=""
        echo "args for ${project} are ${args}"
    fi

    workon "${project}"
    echo "working on ${project}"
    echo "starting server..."
    python manage.py runserver $args
}

start_server

unset project
unset args
unset settings
