#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from math import pi

def move( distance):
    move= Twist()
    move.linear.x = distance
    publisher.publish(move)
    rospy.sleep(3)

def rotate(angle):
    rotate = Twist()
    rotate.angular.z = angle
    publisher.publish(rotate)
    rospy.sleep(3)

def draw_rectangle():
    #rospy.loginfo("Starting...")
    move( 3.0)
    rotate( pi/2)
    move(2.0)
    rotate( pi/2)
    move(3.0)
    rotate( pi/2)
    move( 2.0)

def draw_triangle():
    #rospy.loginfo("Starting...")
    move(2.0)
    rotate( 2 * pi / 3)
    move(2.0)
    rotate(2 * pi / 3)
    move(2.0)
    rotate(2 * pi / 3)

def draw_square():
    #rospy.loginfo("Starting...")
    for _ in range(4):
     move( 2.0)
     rospy.sleep(2)
     rotate( pi/2)
     rospy.sleep(2)
def draw_star():
    #rospy.loginfo("Starting...")
    move(1.0)
    rotate(pi / 5)  
    move(1.0)
    rotate(-2 * pi / 5) 
    move( 1.0)
    rotate( 2 * pi / 5) 
    move( 1.0)
    rotate(-2 * pi / 5)  
    move( 1.0)
    rotate( pi / 5) 
    move( 1.0)
    rotate( pi / 2) 
    move( 1.0)
    rotate(pi / 2) 
    move( 1.0)
    rotate( pi / 2) 
    move( 1.0)
    rotate( pi / 2) 


if __name__ == '__main__':
    rospy.init_node('Shapes')
    #rospy.loginfo("Welcome Sir")
    publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)
   
    
    while not rospy.is_shutdown():
        print("Shapes that can be navigated")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Star")

        print("Enter the shape:")
        shape = input()

        if shape == "Square":
            draw_square()
            rospy.sleep(2)
            
        elif shape == "Rectangle":
            draw_rectangle()
            rospy.sleep(3)

        elif shape == "Triangle":
            draw_triangle()
            rospy.sleep(3)

        elif shape == "Star":
            draw_star()
            rospy.sleep(3)

        else:
            exit()