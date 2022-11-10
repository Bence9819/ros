#!/usr/bin/env python3
 
import rospy
import actionlib
from robot_gui.msg import RobotJobAction, RobotJobActionGoal, RobotJobResult



if __name__== '__main__':

    rospy.init_node('screw_picking_client')

    client = actionlib.SimpleActionClient('/tinker/screw_picking/goal', RobotJobAction)
    client.wait_for_server()

    goal = RobotJobActionGoal()
    goal.header.seq = 2
    goal.goal.name = "WebGuiJob"
    goal.goal_id.id = 'goal_0.5595086582897133_1667899291054'
    
    rospy.loginfo(goal)
    client.send_goal(goal)
    client.wait_for_result()