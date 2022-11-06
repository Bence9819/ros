#!/usr/bin/env python3


from multiprocessing.sharedctypes import Value

import rospy
from faketelen_platform_msgs.srv import SetBoolByIndexSrv, SetBoolByIndexSrvRequest
from faketelen_platform_msgs.msg import BoolArray, BoolEvent

def main ():
    rospy.init_node('first_serviceProxy')
    service = rospy.ServiceProxy('/module_services/module_1/digital_outputs/set_channel', SetBoolByIndexSrv)
    request = SetBoolByIndexSrvRequest()
    request.index = 0
    request.value = True
    response = service.call(
        request
    )
    
    def callback_input_data (msg):
        my_array = msg.values
        x = my_array[0]
        if x == True:
            request.value = False
            rospy.loginfo("igaz")
            rospy.loginfo(request.value)
            service.call



    sub = rospy.Subscriber('/module_topics/module_1/digital_inputs/channels', BoolArray, callback_input_data)

    
    




    #rospy.loginfo(response)
    rospy.loginfo(request.value)
    



        
            


    


    
    




if __name__== '__main__':
    main()
    rospy.spin()
    