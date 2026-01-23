#!/bin/bash
IP=$(~/.commandshortcuts/ip.sh)
export DISPLAY=:0
echo -n "$IP" | xclip -selection clipboard
