#!/usr/bin/env python3
import rospy
import actionlib
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal


def goal_pub():
    rospy.init_node("goal_pub", anonymous=True)
    goal = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    goal.wait_for_server()

    goal_point = MoveBaseGoal()
    goal_point.target_pose.header.frame_id = "map"
    goal_point.target_pose.header.stamp = rospy.Time.now()
    x_coor = int(input("enter where you want to send the robot in x direction "))
    y_coor = int(input("enter where you want to send the robot in y direction "))
    goal_point.target_pose.pose.position.x = x_coor
    goal_point.target_pose.pose.orientation.w = y_coor

    goal.send_goal(goal_point)


if __name__ == "__main__":
    goal_pub()
