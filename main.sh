#!/bin/bash

while true
do
    echo -e "<<< LOT, MFG, EXP Detection >>>"
    for i in {2..1}
    do
        echo -ne "Starting in $i seconds \r"
        sleep 1
    done

    echo -e "\n"
    
    cd /home/polipharm/Desktop/LME_DETECT || exit
    source detection_venv/bin/activate
    python3 ./main.py
done
