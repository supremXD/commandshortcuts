#!/bin/bash

# ANSI colours
GREEN="\033[92m"
YELLOW="\033[93m"
WHITE="\033[97m"
RESET="\033[0m"

# Get local IP
get_ip() {
    local_ip=$(ip route get 8.8.8.8 | awk '{print $7; exit}')
    echo -e "Your local IP is: $local_ip, access by: ${GREEN}http://$local_ip:8080${RESET}"
}

# Main menu
menu() {
    echo ""
    echo -e "${GREEN}Welcome to autoserver, please select an option:${RESET}"
    echo ""
    echo "1 ---> Start python3 server"
    echo "2 ---> Download from a server"
    echo "3 ---> Exit"
    echo ""
    read -p "Select an option ---> " option

    if [[ "$option" == "1" ]]; then
        echo ""
        get_ip
        echo ""
        echo -e "${YELLOW}Starting server. Press Ctrl+C to stop.${RESET}"
        echo ""
        python3 -m http.server 8080
        exit

    elif [[ "$option" == "2" ]]; then
        echo ""
        read -p "Write the local IP(e.g: 192.168.1.125) ---> " ip
        read -p "Write the port of the local IP ---> " port
        read -p "Write the name of the file to download ---> " file
        read -p "Write the directory to save the file (e.g: . for current) ---> " dir
        wget "http://$ip:$port/$file" -P "$dir"
        echo -e "${GREEN}Done!${RESET}"
        exit

    elif [[ "$option" == "3" ]]; then
        exit

    else
        echo -e "${YELLOW}Invalid option.${RESET}"
        sleep 1
        clear
        menu
    fi
}

# Run tool
menu

