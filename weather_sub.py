#!/usr/bin/env python3
# initialization of libraries
import pyowm
import rospy
from std_msgs.msg import String
from math import pi

# Function definition
def weather_process(msg):
    #creating topics named as Temperature and Status for publishing information
    pub = rospy.Publisher("Temperature",String , queue_size = 10)
    pub1 = rospy.Publisher("Status",String , queue_size = 10)
    # reading msg containing a name of city published from client end
    city = msg.data
    #converting into string
    a = str(city)
    # For making an API call by adding API Key
    OpenWMap = pyowm.OWM("05faa43bb46420cd43e1c91bfce26b95")
    mng = OpenWMap.weather_manager()
    # searching for current weather of user published city name
    Weather = mng.weather_at_place(a)
    Data = Weather.weather
    # reading temperature, humidity and status details
    temp = Data.temperature(unit = 'celsius')
    humid = Data.humidity
    detail = Data.detailed_status
    # publishing data on above defined topics 'Temperature' and 'Status'
    pub.publish(a+ " current Temperature is "+ str(temp['temp'])+ " C" + " and Humidity level is "+ str(humid )+ "%")
    pub1.publish("Weather Status in "+ a + ": "+ str(detail))

# function definition for subscribing topic 'Weather' published by client
def create_subscriber():
    rospy.Subscriber("Weather", String, weather_process)
    print("Data is publishing on corresponding topics ")

if __name__== '__main__':
    #initializing subscriber node
    rospy.init_node("weather_sub_node")
    #calling function
    create_subscriber()
    rospy.spin()
