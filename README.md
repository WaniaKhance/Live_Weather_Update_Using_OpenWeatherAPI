# UK Live Weather Update using OpenWeatherAPI 
## Publish and Subscribe Method - Intelligent Systems and Robotics

* Introduction
  ------------

In this project, we described a system design which provides users an access to check current weather update of any city locating in UK using OpenWeatherAPI. To get current weather information, we are performing API Call to https://openweathermap.org/current using an API key. 

* Python Files Description
  ------------

We have developed this system in ROS using publisher & subscribe method where:

1. Weather_pub.py: a publisher node where user will be asked to enter the name of the city to get its weather update which will be published on a topic named as “Weather”.

2. Weather_sub.py: a publisher as well as subscriber node which will subscribe to this ‘Weather’ topic for reading the published message i.e. city_name. This information will be used to make an API call in order to retrieve specific city weather updates. Once it receives the information, it will be published on multiple topics i.e. “Temperature” for current temperature and humidity and “Status” for weather status. 


* Requirements
  ------------

1.	Linux OS - Ubuntu 20.04 

2.	Python 3.7 or above 


* Installation
  ------------
  
First we need to install:

1. Installation of pip3: sudo apt install python3-pip
2. Install pyowm to access OpenWeather API: pip3 install pyowm
3. Add std_msgs in generate_messages section of CMakeLists.txt file.
4. Add std_msgs in package.xml file as well.
5. See output section below to perform other required steps.

* Output Results
  ------------
  
To run the given python codes, we will perform following steps:

1. Go to the directory where all the files are saved i.e. catkin_ws
2. Do catkin_make for updating all the directories and messages.
3. Run roscore, as we must have a roscore running in order for ROS nodes to communicate.
4. Open a new terminal and sourcing setup.bash file for adding several environment variables that ROS needs in order to work. (source devel/setup.bash) It needs to be done whenever using a new terminal.
5. Make all the python files executable using chmod +x *.py.
6. Open three more terminal windows to run publisher and subscriber python files.
7. See topic list using rostopic list.
8. Type rostopic echo /topic_name to see messages published to a topic.
9. Enter the name of the city and all the weather information will be published on their respective topics as shown below:

![alt text](https://github.com/WaniaKhance/Live_Weather_Update_Using_OpenWeatherAPI/blob/main/Picture1.png?raw=true)


