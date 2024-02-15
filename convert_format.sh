#!/bin/bash
IFS=$'\n'
[ !  -d linux ] && mkdir linux 
for file in  `ls -1A | grep -E "^[0-9]{2}\..*\.reg"`
do
	sed '1,3d;s/\"//g'  "$file" > linux/$file
done
