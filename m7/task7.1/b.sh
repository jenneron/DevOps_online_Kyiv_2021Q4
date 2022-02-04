#!/bin/bash

print_help() {
    echo -e "Usage: b.sh [OPTION] [FILE]\n"
    echo "Available parameters:"
    echo -e "\t--the-most-requested-ip\t\tDisplays from which ip were the most requests."
    echo -e "\t--the-most-requested-page\tDisplays the most requested page."
    echo -e "\t--requests-amount-from-ips\tDisplays how many requests were there from each ip."
    echo -e "\t--reffered-non-existed-pages\tDisplays non-existent pages which clients were referred to."
    echo -e "\t--time-with-most-requests\tDisplays what time did site get the most requests."
    echo -e "\t--search-bots\t\t\tDisplays what search bots have accessed the site."
}

if [ "$1" = "--the-most-requested-ip" ]
then
    cat $2 | awk '{print $1}' | sort | uniq -c | sort -nr | head -1 | awk '{print $2", it was repeated "$1" times"}' 
elif [ "$1" = "--the-most-requested-page" ]
then
    cat $2  | awk '{print $7}' | sort | uniq -c | sort -nr | head -1 | awk '{print $2", it was requested "$1" times"}' 
elif [ "$1" = "--requests-amount-from-ips" ]
then
    cat $2 | awk '{print $1}'  | sort | uniq -c
elif [ "$1" = "--reffered-non-existed-pages" ]
then
    cat $2 | grep 404 | awk '{print $7}' | sort -n | uniq
elif [ "$1" = "--time-with-most-requests" ]
then
    cat $2 | awk '{print $4}' | tr -d '[' | sort | uniq -c | sort -nr | head -1 | awk '{print $2" there were "$1" requests"}'
elif [ "$1" = "--search-bots" ]
then
    cat $2 | grep bot | awk -F'"' '{print $6,$1}' | cut --complement -d"-" -f2-3 | sort | uniq -c | sort -nr
else
    print_help
fi
