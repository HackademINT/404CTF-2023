ip route delete default via "$(ip r | grep default | grep -Eo '[0-9]+\.[0-9+\.[0-9]+\.[0-9]+' | head -n 1)"
ip route add default via "$1"