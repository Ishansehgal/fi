#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def move_turtle(shape, size):
    # Initialize the ROS node
    rospy.init_node('turtlebot_controller', anonymous=True)

    # Create a publisher to control the turtle's movement
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Create a Twist message to send velocity commands
    vel_msg = Twist()

    # Set the linear velocity (forward/backward)
    vel_msg.linear.x = 1.0  # Adjust this value to control the speed

    # Set the angular velocity (turning)
    vel_msg.angular.z = 1.0  # Adjust this value to control the turning

    # Define the shape movements using a dictionary
    shape_movements = {
        'rectangle': [(1.0, 0.0), (0.0, 1.0), (-1.0, 0.0), (0.0, -1.0)],
        'square': [(1.0, 0.0), (0.0, 1.0), (-1.0, 0.0), (0.0, -1.0)],
        'star': [(1.0, 0.0), (0.0, 2.0), (0.0, -2.0), (1.0, 0.0), (0.0, 0.0)]
    }

    # Retrieve the corresponding movements for the specified shape
    movements = shape_movements.get(shape)

    if movements is None:
        rospy.logerr('Invalid shape specified.')
        return

    # Calculate the duration for each straight segment based on the size
    duration = size / vel_msg.linear.x

    # Publish the velocity commands to draw the shape
    for linear, angular in movements:
        rospy.sleep(0.5)  # Pause briefly between segments

        # Move straight
        vel_msg.linear.x = linear
        vel_msg.angular.z = angular
        pub.publish(vel_msg)
        rospy.sleep(duration)

    # Stop the turtlebot after drawing the shape
    vel_msg.linear.x = 0.0
    vel_msg.angular.z = 0.0
    pub.publish(vel_msg)

if __name__ == '__main__':
    try:
        shape = input("Enter the desired shape (rectangle, square, star): ")
        size = float(input("Enter the size of the shape: "))
        move_turtle(shape, size)
    except rospy.ROSInterruptException:
        pass
