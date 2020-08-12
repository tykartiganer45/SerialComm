#!/bin/bash


for i in {1..4}
    do
    rm -Rf /home/socialvenu/SerialComm/TestImages/P$i/Cropped/*
    done

for x in {1..100}
    do
    rm -Rf /home/socialvenu/SerialComm/TestImages/P1/Position1_Pattern$x.jpg
    rm -Rf /home/socialvenu/SerialComm/TestImages/P2/Position2_Pattern$x.jpg
    rm -Rf /home/socialvenu/SerialComm/TestImages/P3/Position3_Pattern$x.jpg
    rm -Rf /home/socialvenu/SerialComm/TestImages/P4/Position4_Pattern$x.jpg
    done


