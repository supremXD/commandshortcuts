#!/bin/bash
# ~/.config/polybar/scripts/appmenu.sh
# Menú de energía con rofi (funciona incluso si Polybar tiene entorno limitado)

# Detectar el DISPLAY activo
if [ -z "$DISPLAY" ]; then
  export DISPLAY=$(grep -oP '(?<=DISPLAY=):\d+' /proc/$(pgrep -u $USER bspwm)/environ 2>/dev/null | head -n1)
  [ -z "$DISPLAY" ] && export DISPLAY=:0
fi

# Detectar el bus de sesión de DBus (necesario para systemctl --user y rofi)
if [ -z "$DBUS_SESSION_BUS_ADDRESS" ]; then
  export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$(pgrep -u $USER bspwm)/environ 2>/dev/null | tr -d '\0' | cut -d= -f2-)
fi

# Ejecutar rofi
chosen=$(printf " Google Chrome\n VScode\n Nautilus\n Thunar" | \
  rofi -dmenu -i -p "Apps:" -theme-str 'window {width: 20%;}')

case "$chosen" in
  " Google Chrome") google-chrome & ;;
  " VScode") code & ;;
  " Nautilus") nautilus & ;;
  " Thunar") thunar & ;;
esac
