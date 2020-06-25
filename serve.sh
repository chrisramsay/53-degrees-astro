#! /bin/bash

# Docker command for starting the machine in the first place
# sudo docker run --name nginx-cr -p 8080:80 -v \
#    /home/raz/web/sites/53-degrees-astro/local: \
#    /usr/share/nginx/html:ro -d nginx
#

MACHINE="nginx-53"
# Start the machine
SNAME=$(sudo docker start $MACHINE);
# Get its IP address
IPADD=$(sudo docker inspect -f "{{ .NetworkSettings.IPAddress }}" $MACHINE);
# Replace serving IP address in the config file
sed -i -e 's/[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}/'"$IPADD"'/g' ./configs/local_conf.py
echo "Serving ${SNAME} at ${IPADD}";
