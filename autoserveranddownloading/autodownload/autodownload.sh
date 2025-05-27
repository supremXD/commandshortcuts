#!/bin/bash

# ANSI colours
GREEN="\033[92m"
RESET="\033[0m"

# Download file
download() {
    echo ""
    read -p "Write the local IP from which to download (e.g: 192.168.1.125) ---> " ip
    read -p "Write the port of the local IP ---> " port
    read -p "Write the name of the file to download ---> " file
    read -p "Write the directory to save the file (. for current) ---> " directory

    # User "." directory
    if [[ "$directory" == "." ]]; then
        directory="$(pwd)"
    fi

    url="http://$ip:$port/$file"
    wget "$url" -P "$directory"

    echo -e "${GREEN}Done!${RESET}"
    exit
}

# Run tool
download
