#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

rospy.init_node('turtle_shape_node')
velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
twist_msg = Twist()

# Variables to store previous position
prev_x = 0.0
prev_y = 0.0

# Callback function for the pose topic
def pose_callback(pose):
    global prev_x, prev_y

    # Calculate the distance moved
    distance = math.sqrt((pose.x - prev_x) ** 2 + (pose.y - prev_y) ** 2)

    # Update the previous position
    prev_x = pose.x
    prev_y = pose.y

    # Print the distance moved
    print("Distance moved:", distance)

# Subscribe to the pose topic
rospy.Subscriber('/turtle1/pose', Pose, pose_callback)

# Function to move the turtle in a straight line
def move_forward(distance):
    global twist_msg

    twist_msg.linear.x = 1.0  # Linear velocity in the x direction
    twist_msg.angular.z = 0.0  # Angular velocity (no rotation)
    distance_moved = 0.0

    while distance_moved < distance:
        velocity_publisher.publish(twist_msg)
        distance_moved += math.sqrt((twist_msg.linear.x * (pose.x - prev_x)) ** 2 + (twist_msg.linear.x * (pose.y - prev_y)) ** 2)

    # Stop the turtle's movement
    twist_msg.linear.x = 0.0
    velocity_publisher.publish(twist_msg)

# Function to rotate the turtle
def rotate(angle):
    global twist_msg

    twist_msg.linear.x = 0.0  # No linear movement
    twist_msg.angular.z = 1.0  # Angular velocity for rotation
    angle_rotated = 0.0

    while angle_rotated < angle:
        velocity_publisher.publish(twist_msg)
        angle_rotated += abs(twist_msg.angular.z * (pose.theta - prev_theta))

    # Stop the turtle's rotation
    twist_msg.angular.z = 0.0
    velocity_publisher.publish(twist_msg)

# Make a square
def make_square():
    global prev_x, prev_y, prev_theta

    for _ in range(4):
        move_forward(2.0)
        rotate(math.pi / 2.0)

# Make a rectangle
def make_rectangle():
    global prev_x, prev_y, prev_theta

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
    global prev_x, prev_y, prev_theta

    for _ in range(5):
        move_forward(2.0)
        rotate(2 * math.pi / 3.0)

if __name__ == '__main__':
    try:
        make_square()
        rospy.sleep(1)  # Pause for 1 second
        make_rectangle()
        rospy.sleep(1)  # Pause for 1 second
        make_star()
    except rospy.ROSInterruptException:
        pass
