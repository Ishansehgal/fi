#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

rospy.init_node('turtle_shape_node')
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
twist_msg = Twist()
pose = Pose()  # Global variable to store pose information
prev_x = 0.0
prev_y = 0.0
prev_theta = 0.0
unit_length = 1.0  # Length of each grid cell in meters (assuming 1:1 scale)

# Callback function for the pose topic
def pose_callback(data):
    global pose, prev_x, prev_y, prev_theta
    pose = data
    prev_x = pose.x
    prev_y = pose.y
    prev_theta = pose.theta

# Subscribe to the pose topic
rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

# Function to move the turtle in a straight line
def move_forward(distance):
    global twist_msg, pose, prev_x, prev_y, unit_length

    twist_msg.linear.x = 1.0  # Linear velocity in the x direction
    twist_msg.angular.z = 0.0  # Angular velocity (no rotation)
    target_distance = distance  # Assuming the distance is already in meters

    while math.sqrt((pose.x - prev_x) ** 2 + (pose.y - prev_y) ** 2) < target_distance:
        distance_moved = math.sqrt((pose.x - prev_x) ** 2 + (pose.y - prev_y) ** 2)
        print("Distance moved:", distance_moved)
        velocity_publisher.publish(twist_msg)
        rospy.sleep(0.1)  # Small delay to allow pose updates

    # Stop the turtle's movement
    twist_msg.linear.x = 0.0
    velocity_publisher.publish(twist_msg)

# Function to rotate the turtle
def rotate(angle):
    global twist_msg, pose, prev_theta

    twist_msg.linear.x = 0.0  # No linear movement
    twist_msg.angular.z = 1.0  # Angular velocity for rotation
    target_angle = angle  # Assuming the angle is already in radians

    while abs(pose.theta - prev_theta) < target_angle:
        velocity_publisher.publish(twist_msg)
        rospy.sleep(0.1)  # Small delay to allow pose updates

    # Stop the turtle's rotation
    twist_msg.angular.z = 0.0
    velocity_publisher.publish(twist_msg)

# Make a square
def make_square():
    for _ in range(4):
        move_forward(2.0)
        rotate(math.pi / 2.0)

# Make a rectangle
def make_rectangle():
    move_forward(3.0)
    rotate(math.pi / 2.0)
    move_forward(2.0)
    rotate(math.pi / 2.0)
    move_forward(3.0)
    rotate(math.pi / 2.0)
    move_forward(2.0)
    rotate(math.pi / 2.0)

# Make a 5-pointed star
def make_star():
    for _ in range(5):
        move_forward(2.0)
        rotate(2 * math.pi / 3.0)

if __name__ == '__main__':
    try:
        rate = rospy.Rate(10)  # Rate at which to run the ROS loop
        while not rospy.is_shutdown():
            make_square()
            rospy.sleep(1)  # Pause for 1 second
            make_rectangle()
            rospy.sleep(1)  # Pause for 1 second
            make_star()
            rospy.sleep(1)  # Pause for 1 second
            rate.sleep()
    except rospy.ROSInterruptException:
        pass
