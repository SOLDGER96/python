#!/bin/bash
#

if [ -z "$1" ]; then
	echo "Usage: ./gitpush.sh \"Your commit message\""
	exit 1
fi

MESSAGE="$1"

git add .
git commit -m "$MESSAGE"
git push origin main
