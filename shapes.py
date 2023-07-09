#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
from turtlesim.srv import Spawn
from std_srvs.srv import Empty
PI = 3.1415926535897

vel_msg = Twist()

velocity_publisher = None

def move_forward(target_distance):
    global velocity_publisher

    # Receiveing the user's input
    print("Let's move your robot")
    speed = 2
    distance = target_distance
    vel_msg.linear.x = speed
    
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
        
        move_forward(2)
        rospy.sleep(0.1)
        rotate(90)


def make_rectangle():
    rospy.sleep(0.5)
    move_forward(4)
    rospy.sleep(0.5)
    rotate(90)
    move_forward(2)
    rospy.sleep(0.5)
    rotate(90)
    rospy.sleep(0.5)
    move_forward(4)
    rospy.sleep(0.5)
    rotate(90)
    rospy.sleep(0.5)
    move_forward(2)
    rospy.sleep(0.5)
    rotate(90)
    rospy.sleep(0.5)


def make_star():
    angle = 144
    for _ in range(5):
        move_forward(2)
        rotate(angle)
        move_forward(2)
        rotate(72 - angle)
def reset_turtle():
    client =rospy.ServiceProxy('/reset', Empty)
    client.call()

def spwan_bot():
    rospy.wait_for_service('/spawn')
    spawn_turtle= rospy.ServiceProxy('/spawn',Spawn)

    x =float(input("enter the x coordinate: " ))
    y=float(input("enter the y coordinate: "))
    theta=float(input("enter the theta in radians: "))
    turtle_name="my_turtle" 
    
    response=spawn_turtle(x,y,theta,turtle_name)
    if response.name == turtle_name:
        rospy.loginfo("Turtle spawned successfully!")
    else:
        rospy.logerr("Failed to spawn turtle.")

if __name__ == '__main__':
    rospy.init_node('turtle_shape_node')
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # Rate at which to run the ROS loop
    
    
    
    while not rospy.is_shutdown():
        print("enter the shape")
        shape=input()
        if(shape=="square"):    
            make_square()
            rospy.sleep(1)
            reset_turtle()
        
        

        elif  (shape=="rectangel"):

            
            make_rectangle()
            rospy.sleep(1)
            reset_turtle()


        elif  (shape=="star"):

            make_star()
            rospy.sleep(1)
            reset_turtle()
        
        elif (shape=="spawn"):

            spwan_bot()    
            
            
        else : 
            print("enter right value")