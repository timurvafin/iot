#!/bin/bash

TOKEN="DvezaaJasgz9HEUDY9o8dmbUfLgRsPQz"
ACCOUNT_ID="57906"
ZONE_ID="vafin.ru"
RECORD_ID="18466657"
IP=`curl --ipv4 -s http://icanhazip.com/`

curl -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -X "PATCH" \
     -i "https://api.dnsimple.com/v2/$ACCOUNT_ID/zones/$ZONE_ID/records/$RECORD_ID" \
     -d "{\"content\":\"$IP\"}"

