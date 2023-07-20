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
    def rotate5(angel):
        rotate=Twist()
        rotate.angular.z=angel   
        turtle5_pub.publish(rotate)
    def forward3(distance):
        forword = Twist(5)
        forword.linear.x =distance
        turtle3_pub.publish(forword)
    def forward4(distance):
        forword = Twist()
        forword.linear.x =distance
        turtle4_pub.publish(forword)
    def forward5(distance):
        forword = Twist()
        forword.linear.x =distance
        turtle5_pub.publish(forword)


    def I():
        rospy.sleep(2)
        forward2(float(3))
        rospy.sleep(2)
        rotate2(float(3.14))
        rospy.sleep(2)
        forward2(float(1.5))
        rospy.sleep(2)
        rotate2(float(-1.53))
        rospy.sleep(2)
        forward2(float(3))
        rospy.sleep(2)
        rotate2(float(1.53))
        rospy.sleep(2)
        forward2(float(1.5))
        rospy.sleep(2)
        rotate2(float(3.14))
        rospy.sleep(2)
        forward2(float(3))
        rospy.sleep(2)
        rotate2(float(3.14))
        rospy.sleep(2)
    if __name__ == '__main__':
     pub_thread = threading.Thread(target=I)
     pub_thread.start()
    def s():
        turtle3_cmd=Twist()
        turtle3_cmd.linear.x =3
        turtle3_cmd.angular.z=3.3
        rospy.sleep(2)
        turtle3_pub.publish(turtle3_cmd)
        rospy.sleep(2)
        turtle3_cmd.linear.x =3
        turtle3_cmd.angular.z=-3.3
        rospy.sleep(2)
        turtle3_pub.publish(turtle3_cmd)
        rospy.sleep(2)     
    if __name__ == '__main__':
     pub_thread = threading.Thread(target=s)
     pub_thread.start()    
    def H():
        rospy.sleep(2)
        rotate1 (float(1.53))
        rospy.sleep(2)
        forward1(float(3))
        rospy.sleep(2)
        rotate1 (float(3.14))
        rospy.sleep(2)
        forward1(float(1.5))
        rospy.sleep(2)
        rotate1 (float(1.53))  
        rospy.sleep(2)
        forward1(float(1.5))
        rospy.sleep(2)
        rotate1 (float(1.53))  
        rospy.sleep(2)
        forward1(float(1.5))
        rospy.sleep(2)
        rotate1 (float(3.14))  
        rospy.sleep(2)
        forward1(float(3))
        rospy.sleep(2)
        rotate1 (float(1.53))  
        rospy.sleep(2)
    if __name__ == '__main__':
     pub_thread = threading.Thread(target=H)
     pub_thread.start()    
    def A():
        rospy.sleep(2)
        rotate4(float(1.04))
        rospy.sleep(2)
        forward4(3)
        rospy.sleep(2)
        rotate4(float(-2.35))
        rospy.sleep(2)
        forward4(1)
        rospy.sleep(2)
        rotate4(float(-2.03))
        rospy.sleep(2)
        forward4(0.7)
        rospy.sleep(2)
        rotate4(float(3.14))
        rospy.sleep(2)
        forward4(0.8)
        rospy.sleep(2)
        rotate4(float(-1.0))
        rospy.sleep(2)
        rospy.sleep(2)
        forward4(2)
        rospy.sleep(2)
        rotate4(float(-1.04))
        rospy.sleep(2)
    if __name__ == '__main__':
     pub_thread = threading.Thread(target=A)
     pub_thread.start()
    def N():
        rospy.sleep(2)
        rotate5(float(1.53))
        rospy.sleep(2)
        forward5(3)
        rospy.sleep(2)
        rotate5(float(-2.35))
        rospy.sleep(2)
        forward5(3.7)
        rospy.sleep(2)
        rotate5(float(2.35))
        rospy.sleep(2)
        forward5(3)
        rospy.sleep(2)
    if __name__ == '__main__':
     pub_thread = threading.Thread(target=N)
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
    turtle5_pub = rospy.Publisher('/turtle5/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)   
    while(1):
        rospy.wait_for_service('/spawn')
        spawn_turtle = rospy.ServiceProxy('/spawn', Spawn)
        spawn_turtle(0.3, 5.2, 0.0, 'turtle2')
        spawn_turtle(4.0, 5.2, 0.0, 'turtle3')
        spawn_turtle(7.5, 5.2, 0.0, 'turtle4')
        spawn_turtle(7.5, 1.5, 0.0, 'turtle5')

        print("turtles spawned ")
        all_shapes()
    