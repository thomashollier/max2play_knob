#!/bin/bash

# Path to current Directory
CURRENTDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo "Install-Script"

echo ""
echo server IP: $1
echo player MAC: $2
echo usb device name: $3
echo ""

echo "Update sources"
sudo apt-get update
echo "Done"

echo "Install pip"
apt-get -y install python-pip
echo "Done"

echo "Install evdev"
pip install evdev
echo "Done"

echo "Install requests"
pip install requests
echo "Done"

echo "Stopping systemd usbvolumeknob.service if it is running"
sudo systemctl stop usbvolumeknob.service

echo "Creating systemd usbvolumeknob.service file"
cat > /lib/systemd/system/usbvolumeknob.service << EOF
[Unit]
Description=USB Rotary Knob service
After=multi-user.target

[Service]
Type=simple
ExecStart=/var/www/max2play/application/plugins/Usbvolumeknob/scripts/knobLogic.py -s $1 -m $2 -n "$3"

[Install]
WantedBy=multi-user.target

EOF

echo "Registering, enabling and starting systemd usbvolumeknob.service"
systemctl daemon-reload
sudo systemctl enable usbvolumeknob.service
sudo systemctl start usbvolumeknob.service

echo "finished"
exit 0
