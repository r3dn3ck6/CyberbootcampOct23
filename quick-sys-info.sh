#!/bin/bash
# Name: quick-sys-info.sh
# Purpose: Display Linux system CPU, memory and kernel version
# Author: nixCraft {https://www.cyberciti.biz/}, under GPL v2.x+
# --------------------------------------------------------------
 
findcpu(){
	grep 'model name' /proc/cpuinfo  | uniq | awk -F':' '{ print $2}'
}
 
findkernelversion(){
	uname -mrs
}
 
totalmem(){
	grep -i 'memtotal' /proc/meminfo | awk -F':' '{ print $2}'
}
# Display it
echo "CPU Type : $(findcpu)"
echo "Kernel version : $(findkernelversion)"
echo "Total memory : $(totalmem)"
done


# # You learned how to call a shell script function in an echo/printf statement
# using the $(function_name) syntax. For example, if you have a shell script
#  function called bar(), you can call it in an echo statement like this:
###############################################################################
#echo " text here $(bar)"
## or ##
#printf "%s some text here\n" "$(Bar)"