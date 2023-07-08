#!/usr/bin/env python3

import rospy
from std_msgs.msg import String


def pub():
    rospy.init_node('pub1')

    pub_details = rospy.Publisher('Electronics_projects', String, queue_size=10)

    rate = rospy.Rate(1) 

    while not rospy.is_shutdown():

        msg = "this is first node "

        pub_details.publish(msg)

        rospy.loginfo(msg)

        rate.sleep()

if __name__=='__main__':
    pub()
