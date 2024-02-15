#!/bin/bash
TARGET="${HOME}/.putty/sessions/theme_random"
SRC="linux/08. Desert.reg"

ran_index (){
	
	return $(($RANDOM % ${1} +1))
}
get_profilenum (){
	[  -f linux/index ] && return $(cat linux/index) || return 51
}
get_profilenum
PROFILE_NUM=$?
ran_index ${PROFILE_NUM}
INDEX=`printf "%02d" $?`
SRC="linux/`ls -1A linux | grep -E "^${INDEX}"`"
echo $SRC
while read line; do
KEY=$(echo $line | cut -d "=" -f 1 )
sed -i "s/${KEY}=.*/${line}/" $TARGET
done < "${SRC}"

putty -load theme_random
