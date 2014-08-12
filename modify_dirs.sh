#!/bin/bash

# nick vincent-maloney
# 2014-0611
#
# script for removing certain files and copying others
# built for asms 2014 thumb drives for tutorials
#

usb_path=$1
sfd_inst_dir=""

if [ -d $sfd_inst_dir ]
then
    rm "/$1/$sfd_inst_dir/*"
fi
