#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

def move_turtles():
    # Initialize the ROS node
    rospy.init_node('multi_turtlesim', anonymous=True)

    # Create publishers for each turtle
    turtle1_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    turtle2_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)

    # Create Twist messages for velocity commands
    turtle1_cmd = Twist()
    turtle2_cmd = Twist()

    # Set the linear and angular velocities for each turtle
    turtle1_cmd.linear.x = 3.0
    turtle1_cmd.angular.z = 3.3
    rospy.sleep(1)
    turtle1_pub.publish(turtle1_cmd)
    rospy.sleep(2)
    turtle1_cmd.angular.z = -3.3
    turtle1_cmd.linear.x = 3.0

    turtle1_pub.publish(turtle1_cmd)
   # rospy.sleep(2)

    turtle2_cmd.linear.x = 0.5
    turtle2_cmd.angular.z = -0.5

    rate = rospy.Rate(10)  # Publish at 10 Hz

    
        # Publish the velocity commands for each turtle
    turtle1_pub.publish(turtle1_cmd)
    turtle2_pub.publish(turtle2_cmd)
       
if __name__ == '__main__':
    try:
        # Spawn turtle2 using the spawn_turtle service
        rospy.wait_for_service('/spawn')
        spawn_turtle = rospy.ServiceProxy('/spawn', Spawn)
        spawn_turtle(5.0, 5.0, 0.0, 'turtle2')

        move_turtles()
    except rospy.ROSInterruptException:
        pass
