#!/bin/bash
foo(){
    date
}
echo "Today is $(foo)"
printf "Today is %s\n" "$(foo)"