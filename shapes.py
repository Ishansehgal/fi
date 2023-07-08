#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

twist_msg = Twist()

x = 0
y = 0
tz = 0

# Callback function for the pose topic
def pose_callback(pose_message):
    global x, y, tz

    x = pose_message.x
    y = pose_message.y
    tz = pose_message.theta

# Function to move the turtle in a straight line
def move_forward(distance):
    global x, y

    x0 = x
    y0 = y
    distance_moved = 0.0
    loop_rate = rospy.Rate(10)  # Create a rate object for controlling the publishing frequency

    twist_msg.linear.x = 1.0  # Linear velocity in the x direction
    twist_msg.angular.z = 0.0  # Angular velocity (no rotation)
    #target_distance = distance  # Assuming the distance is already in meters

    while True:
        rospy.loginfo("bot is moving forward")
        velocity_publisher.publish(twist_msg)

        loop_rate.sleep()

        distance_moved = abs(0.5 * math.sqrt(((x - x0) ** 2) + ((y - y0) ** 2)))
        print(distance_moved)

        if not (distance_moved < distance):
            rospy.loginfo("reached")
            break

    twist_msg.linear.x = 0
    velocity_publisher.publish(twist_msg)
    rospy.sleep(0.1)  # Small delay to allow pose updates

def rotate(angle_deg):
    global twist_msg,tz
    angle_rad =math.radians(angle_deg)
    target_angle = tz + angle_rad
    twist_msg.linear.x = 0.0  # No linear movement
    twist_msg.angular.z = 5  # Angular velocity for rotation
    #target_angle = angle_  # Assuming the angle is already in radians

    while True :

        rospy.loginfo("bot is rotating")
        velocity_publisher.publish(twist_msg)
        rospy.sleep(0.1)  # Small delay to allow pose updates

        if tz >= target_angle:
           break

    
    twist_msg.angular.z = 0.0

    velocity_publisher.publish(twist_msg)

def make_square():
    for _ in range(4):
        move_forward(5)
        rotate(90)

# Make a rectangle
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
    pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, pose_callback)
    while not rospy.is_shutdown():
            make_square()
            rospy.sleep(1)  # Pause for 1 second
            make_rectangle()
            rospy.sleep(1)  # Pause for 1 second
    #rotate(90)
