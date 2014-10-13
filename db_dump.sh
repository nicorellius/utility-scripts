#!/bin/bash

# db dump script using lamp stack

password=$1

dump_cmd="/home/nick/dev/lamp/mysql/bin/mysqldump"
user="root"
password="${password}"
db_name=$1

$dump_cmd -u $user -p$password $db_name > "${db_name}.sql"
