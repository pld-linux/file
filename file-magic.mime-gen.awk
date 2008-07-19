#!/bin/awk -f

BEGIN {
	FS = "\t+|  +"
	level = 0
}

/^#/ { next }

/^[^!]/ {
	pref=$0
	sub(/[^>].*/, "", pref)
	level = length(pref)
	str[level] = $1"\t"$2"\t"$3
}

/^!:mime/ {
	for(i = 0; i < level; i++)
		print str[i]
	print str[level]"\t"$2
}
