#!/bin/ksh
echo 'Content-Type: text/plain';
echo '';
#ssh -q -i /home/lighttpd/.ssh/id_rsa_pi root@scubboraspi.dyndns.org 'df' | grep '/var/media' | perl -pe 's/.*\s([0-9]+)%.*/$1/' | tr -d '\n';
ssh -q -i /home/lighttpd/.ssh/id_rsa_pi root@scubboraspi.dyndns.org 'df -h' | grep '/var/media' | awk '{ print "{\"used\":\"" $3 "\",\"total\":\"" $2 "\",\"percentage_free\":" substr($5,1,length($5)-1) "}"}' | tr -d '\n'
