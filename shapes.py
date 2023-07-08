#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

PI = 3.1415926535897

vel_msg = Twist()
tz = 0
velocity_publisher = None

def pose_callback(pose_message):
    global tz
    tz = pose_message.theta

def move_forward(target_distance):
    global velocity_publisher

    # Receiveing the user's input
    print("Let's move your robot")
    speed = 2
    distance = target_distance

    # Checking if the movement is forward or backwards
    vel_msg.linear.x = speed
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0
    vel_msg.angular.z = 0

    # Setting the current time for distance calculus
    t0 = rospy.Time.now().to_sec()
    current_distance = 0

    while current_distance < distance:
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = speed * (t1 - t0)

    # After the loop, stop the robot
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)


def rotate(deg):
    global velocity_publisher

    # Receiveing the user's input
    print("Let's rotate your robot")
    speed = 50
    angle = deg

    # Converting from angles to radians
    angular_speed = speed * 2 * PI / 360
    relative_angle = angle * 2 * PI / 360

    # We won't use linear components
    vel_msg.linear.x = 0
    vel_msg.linear.y = 0
    vel_msg.linear.z = 0
    vel_msg.angular.x = 0
    vel_msg.angular.y = 0

    # Set the angular velocity
    vel_msg.angular.z = angular_speed

    # Set the current time for angle calculus
    t0 = rospy.Time.now().to_sec()
    current_angle = 0

    while current_angle < relative_angle:
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_angle = angular_speed * (t1 - t0)

    # Stop the robot
    vel_msg.angular.z = 0
    velocity_publisher.publish(vel_msg)


def make_square():
    for _ in range(4):
        #rospy.sleep(0.1)
        move_forward(2)
        rotate(90)


def make_rectangle():
    move_forward(5)
    rotate(90)
    move_forward(3)
    rotate(90)
    move_forward(5)
    rotate(90)
    move_forward(3)
    rotate(90)


if __name__ == '__main__':
    rospy.init_node('turtle_shape_node')
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # Rate at which to run the ROS loop
    position_topic = "/turtle1/pose"
    pose_subscriber = rospy.Subscriber(position_topic, Pose, pose_callback)
    
    #while not rospy.is_shutdown():
    print("enter the shape")
    shape=input()
    if(shape=="square"):    
        make_square()
        

    elif  (shape=="rectangel"):

            
        make_rectangle()
        
        
            
            
    else : 
            print("enter right value")