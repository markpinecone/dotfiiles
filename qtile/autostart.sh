#!/bin/sh
nitrogen --restore &
picom &
nm-applet &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
setxkbmap lv

