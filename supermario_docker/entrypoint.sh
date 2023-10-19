#!/bin/bash

while true; do
        SERVER="marioweb.netsec-docker.isi.jhu.edu"
        PORT="23"

        USERNAME="bowser"
        PASSWORD="goombaMask"

        COMMAND="cat /home/bowser/mario_notes.conf"

        expect << EOF
          spawn telnet $SERVER $PORT
          expect "login: "
          send "$USERNAME\r"
          expect "Password: "
          send "$PASSWORD\r"
          expect "$ "
          send "$COMMAND\r"
          expect "$ "
          interact
EOF

  sleep 60
done
