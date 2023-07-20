#!/usr/bin/env python3
import threading
import rospy
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn
from std_srvs.srv import Empty
def all_shapes():
    def rotate1(angel):
        rotate=Twist()
        rotate.angular.z=angel   
        turtle1_pub.publish(rotate)
    def rotate2(angel):
        rotate=Twist()
        rotate.angular.z=angel   
        turtle2_pub.publish(rotate)
    def forward1(distance):
        forword = Twist()
        forword.linear.x =distance
        turtle1_pub.publish(forword)
    def forward2(distance):
        forword = Twist()
        forword.linear.x =distance
        turtle2_pub.publish(forword)
    def rotate3(angel):
        rotate=Twist()
        rotate.angular.z=angel   
        turtle3_pub.publish(rotate)
    def rotate4(angel):
        rotate=Twist()
        rotate.angular.z=angel   
        turtle4_pub.publish(rotate)
    def forward3(distance):
        forword = Twist()
        forword.linear.x =distance
        turtle3_pub.publish(forword)
    def forward4(distance):
        forword = Twist()
        forword.linear.x =distance
        turtle4_pub.publish(forword)

    def square():
        for _ in range(4):
            forward1(float(2))
            rospy.sleep(2)
            rotate1(float(1.57))
            rospy.sleep(2)
    if __name__ == '__main__':
     pub_thread = threading.Thread(target=square)
     pub_thread.start()
    def rectangle():
        forward2(float(2))
        rospy.sleep(2)
        rotate2 (float(1.57))
        rospy.sleep(2)        
        forward2(float(1))
        rospy.sleep(2)
        rotate2 (float(1.57))
        rospy.sleep(2)  
        forward2(float(2))
        rospy.sleep(2)
        rotate2 (float(1.57))  
        rospy.sleep(2)
        forward2(float(1))
        rospy.sleep(2)
        rotate2 (float(1.57)) 
        rospy.sleep(2) 
    if __name__ == '__main__':
     pub_thread = threading.Thread(target=rectangle)
     pub_thread.start()    
    def triangle():
        forward3(float(2))
        rospy.sleep(2)
        rotate3 (float(2.094))
        rospy.sleep(2)
        forward3(float(2))
        rospy.sleep(2)
        rotate3 (float(2.094))
        rospy.sleep(2)
        forward3(float(2))
        rospy.sleep(2)
        rotate3 (float(2.094))  
        rospy.sleep(2)
    if __name__ == '__main__':
     pub_thread = threading.Thread(target=triangle)
     pub_thread.start()    
    def make_star():
        for _ in range(5):
            forward4(float(2))
            rospy.sleep(2)
            rotate4(float(2.513))
            rospy.sleep(2)
            forward4(2)
            rospy.sleep(2)
            rotate4(float(1.256 - 2.513))
            rospy.sleep(2)
    if __name__ == '__main__':
     pub_thread = threading.Thread(target=make_star)
     pub_thread.start()        
def reset_turtle():
    client =rospy.ServiceProxy('/reset', Empty)
    client.call()
if __name__ == '__main__':
    rospy.init_node('multi_turtlesim', anonymous=True)

    turtle1_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    turtle2_pub = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
    turtle3_pub = rospy.Publisher('/turtle3/cmd_vel', Twist, queue_size=10)
    turtle4_pub = rospy.Publisher('/turtle4/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)   
    while(1):
        rospy.wait_for_service('/spawn')
        spawn_turtle = rospy.ServiceProxy('/spawn', Spawn)
        spawn_turtle(5.0, 5.0, 0.0, 'turtle2')
        spawn_turtle(8.0, 8.0, 0.0, 'turtle3')
        spawn_turtle(3.0, 3.0, 0.0, 'turtle4')

        print("turtles spawned ")
        all_shapes()
    