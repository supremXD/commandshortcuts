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

# Start server
server() {
    echo ""
    get_ip
    echo ""
    echo -e "${YELLOW}Starting server. Press Ctrl+C to stop.${RESET}${WHITE}"
    echo ""
    python3 -m http.server 8080
    exit
}

# Run tool
server
