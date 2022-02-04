#!/bin/bash

print_help() {
    echo "Available parameters:"
    echo -e "\t--all\t\tDisplay the IP addresses and symbolic names of all hosts in the current subnet"
    echo -e "\t--target\tDisplays a list of open system TCP ports"
}

check_deps() {
    if ! command -v nmap &> /dev/null
    then
        echo "ERROR: a.sh depends on nmap, but it is not installed"
        exit
    fi
}

all() {
    nmap -sn -oG - $1
}

target() {
    nmap -p- $1
}

check_deps

if [ "$1" = "--all" ]
then
    all $2
elif [ "$1" = "--target" ]
then
    target $2
else
    print_help
fi
