#!/usr/bin/env python3

import rospy
from nav_msgs.msg import Path
from rmp01.srv import posemsg

def plan_callback(msg):
        global x, y, z 
        pose_stamped = msg.poses[0]
        pose = pose_stamped.pose
        position = pose.position
        x = position.x
        y = position.y
        z = position.z
        #rospy.loginfo("the values are x={}, y={}, z={}".format(x, y, z))
        return x,y,z

def handle_get_plan_coordinates(req):
    global x, y, z 


    response = posemsg()
    response.x = float(x)
    response.y = float(y)
    response.z = float(z)
      
    rospy.loginfo("the values are x={}, y={}, z={}".format(x, y, z))
    return response      
def main():
    rospy.init_node('plan_subscriber')
    plan_topic = 'move_base/NavfnROS/plan'
    rospy.Subscriber(plan_topic, Path, plan_callback)
    service = rospy.Service('pose_msg', posemsg, handle_get_plan_coordinates)
    rospy.spin()

if __name__ == '__main__':
    main()
