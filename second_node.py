#!/usr/bin/env python3

import threading
import rospy
from std_msgs.msg import String

def pub_sub():
    rospy.init_node('pub_sub')

    def pub():
        pub_details = rospy.Publisher('second_publisher', String, queue_size=10)
        rate = rospy.Rate(1)

        while not rospy.is_shutdown():
            msg = "this is second publisher"
            pub_details.publish(msg)
            rospy.loginfo(msg)
            rate.sleep()

    def msgCallback(greeting):
        rospy.loginfo(greeting.data)

    def subscriber():
        rospy.Subscriber('Electronics_projects', String, msgCallback)
        rospy.spin()

    if __name__ == '__main__':
     pub_thread = threading.Thread(target=pub)
     pub_thread.start()

    subscriber()

if __name__ == '__main__':
    pub_sub()
