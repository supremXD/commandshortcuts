#!/bin/bash
# ~/.config/polybar/scripts/powermenu.sh
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
chosen=$(printf "  Apagar\n  Reiniciar\n  Cerrar sesión\n  Suspender" | \
  rofi -dmenu -i -p "Energía:" -theme-str 'window {width: 20%;}')

case "$chosen" in
  "  Apagar") systemctl poweroff ;;
  "  Reiniciar") systemctl reboot ;;
  "  Cerrar sesión") bspc quit ;;
  "  Suspender") systemctl suspend ;;
esac
