#!/usr/bin/env python3
#Initialization of Libraries
#Library for OpenWeatherMap(OWM) web APIs
import pyowm
#for writing ros node
import rospy
#message type using std_msgs package 
from std_msgs.msg import String
from math import pi

#Function definition for publishing user input
def weather_pub():
    #Initialization of publisher node
    rospy.init_node("weather_pub_node")
    #creating topic named as 'Weather' with String msg type
    pub = rospy.Publisher("Weather", String , queue_size = 10)

    rate = rospy.Rate(5)
    #infinite loop until forced shutdown
    while not rospy.is_shutdown():
        text = input("Enter name for city:  ")
        #publishing user input i.e. city name on the topic 'Weather'
        pub.publish(text)

#Main function
if __name__ == '__main__':
    try:
        #calling function
        weather_pub()
    #if any exception or interruption occurs during the process
    except rospy.ROSInterruptException:
        pass
