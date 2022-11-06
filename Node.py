#!/usr/bin/env python
# -*- coding: UTF-8 -*- #
import rospy
import serial
import time
from ccmslam_msgs import rssi

pub = rospy.Publisher('rssi_topic', my_uart, queue_size=10)

serialPort = serial.Serial(port="COM3", baudrate=115200,
                           bytesize=8, timeout=0)
rospy.init_node('rssi', anonymous=True)

rate = rospy.Rate(10)

while (not rospy.is_shutdown()):

    rssi_data = rssi()
    data = serialPort.readline()
    data1 = data.decode('utf-8')
    if data1 == '':
        continue
    else:
        rssi_data.strength = data1

    time.sleep(0.1)

pub.publish(rssi_data)
rate.sleep()
