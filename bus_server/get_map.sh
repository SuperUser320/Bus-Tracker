if [ -n "$1" ] && [ -n "$2" ] && [ -n "$3" ] && [ -n "$4" ] && [ -n "$5" ]; then
	wget -O "$1".png "https://maps.googleapis.com/maps/api/staticmap?size=$4x$5&scale=1&zoom=14&markers=$2,$3"
else
	echo "missing parameters"
fi
