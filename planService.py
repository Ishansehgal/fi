#!/usr/bin/env python3

import rospy
from rmp01.srv import posemsg  # Replace 'rmp01' with the actual name of your package
from geometry_msgs.msg import Point
import math

def call_custom_service():
    rospy.wait_for_service('pose_msg')  # Replace '/pose_msg' with the correct service name
    try:
        # Create a proxy to call the service
        custom_service = rospy.ServiceProxy('pose_msg', posemsg)

        # Call the service
        response = custom_service()
        
        # Process the response
        
            # Extract x, y, and z coordinates from the response
        x = response.x
        y = response.y
        z = response.z

          
            
        rospy.loginfo(x)
           



    except rospy.ServiceException as e:
        rospy.logerr(f"Service call failed: {e}")

def main():
    rospy.init_node('custom_service_client')
    call_custom_service()

if __name__ == '__main__':
    main()
