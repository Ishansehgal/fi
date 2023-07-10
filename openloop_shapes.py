#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose 
from turtlesim.srv import SetPen
from std_srvs.srv import Empty
from turtlesim.srv import Spawn

def pose_callback(msg):
    rospy.losginfo(msg)

def forward(distance):
    forword = Twist()
    forword.linear.x =distance
    shapes.publish(forword)

def rotate(angel):
    rotate=Twist()
    rotate.angular.z=angel   
    shapes.publish(rotate)

def square():
    for _ in range(4):
        forward(float(3))
        rospy.sleep(2)
        rotate(float(1.57))
        rospy.sleep(2)

def rectangle():
    forward(float(4))
    rospy.sleep(2)
    rotate (float(1.57))
    rospy.sleep(2)        
    forward(float(2))
    rospy.sleep(2)
    rotate (float(1.57))
    rospy.sleep(2)  
    forward(float(4))
    rospy.sleep(2)
    rotate (float(1.57))  
    rospy.sleep(2)
    forward(float(2))
    rospy.sleep(2)
    rotate (float(1.57)) 
    rospy.sleep(2) 
def triangle():
    forward(float(4))
    rospy.sleep(2)
    rotate (float(2.094))
    rospy.sleep(2)
    forward(float(4))
    rospy.sleep(2)
    rotate (float(2.094))
    rospy.sleep(2)
    forward(float(4))
    rospy.sleep(2)
    rotate (float(2.094))  
    rospy.sleep(2)
def make_star():
    for _ in range(5):
        forward(float(2))
        rospy.sleep(2)
        rotate(float(2.513))
        rospy.sleep(2)
        forward(2)
        rospy.sleep(2)
        rotate(float(1.256 - 2.513))
        rospy.sleep(2)
def reset_turtle():
    client =rospy.ServiceProxy('/reset', Empty)
    client.call()
def clear_turtle():
    clear =rospy.ServiceProxy('/reset', Empty)
    clear.call()
def colours():
    rospy.wait_for_service('/turtle1/set_pen')
    colour= rospy.ServiceProxy('/turtle1/set_pen',SetPen)
    r=int(input("enter the vale of r between 0-255 "))
    g=int(input("enter the vale of g between 0-255 "))
    b=int(input("enter the vale of b between 0-255 "))
    width=int(input("enter size"))
    off=False
    rospy.sleep(2)
    colour(r,g,b,width,off)
    print("Command ran succesfully")
def spwan_bot():
    rospy.wait_for_service('/spawn')
    spawn_turtle= rospy.ServiceProxy('/spawn',Spawn)

    x =input("enter the x coordinate: " )
    y=float(input("enter the y coordinate: "))
    theta=float(input("enter the theta in radians: "))
    turtle_name="my_turtle" 
    
    response=spawn_turtle(x,y,theta,turtle_name)
    if response.name == turtle_name:
        rospy.loginfo("Turtle spawned successfully!")
    else:
        rospy.logerr("Failed to spawn turtle.")

if __name__ == '__main__':
    rospy.init_node('shapes')
    shapes = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
    rate = rospy.Rate(5)
    pose=rospy.Subscriber("/turtle1/Pose",Pose,callback=pose_callback)
    while not rospy.is_shutdown():
        print("enter the shape you want to print")
        shape=input()
        print("now lets set the color and width if lines")
        colours()
        if (shape=="square"):
            square()
            rospy.sleep(2)
            clear_turtle()
        elif (shape=="rectangle"):
            rectangle()
            rospy.sleep(2)
            clear_turtle()
        elif (shape=="triangle"):
            triangle()
            rospy.sleep(2)
            clear_turtle()
        elif (shape=="spawn"):
            spwan_bot()
        elif  (shape=="star"):
            make_star()
            rospy.sleep(3)
            clear_turtle()
        else :
            (print("Enter right name"))