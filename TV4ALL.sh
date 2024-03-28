#!/bin/bash

# Verificar si se proporciona la contraseña como argumento
if [ $# -eq 0 ]; then
    echo "Error: Se requiere la contraseña como argumento."
    exit 1
fi

password="$1"

for port in /dev/ttyACM*; do
	echo "$password" | sudo -S chmod 666 "$port"
done

echo "Todos los puertos /dev/ttyACM* han sido habilitados."

python3 TV4ALL.py

while true; do
	read -p "entrada: " input
	if [ "$input" = "0" ]; then
		python3 TV4ALL.py
	elif [ "$input" = "1" ]; then
		break
	fi
done
