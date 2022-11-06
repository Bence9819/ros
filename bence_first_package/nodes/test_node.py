#!/usr/bin/env python3
 
 
from multiprocessing.sharedctypes import Value
 
import rospy
from faketelen_platform_msgs.srv import SetBoolByIndexSrv, SetBoolByIndexSrvRequest
from faketelen_platform_msgs.msg import BoolArray, BoolEvent
 
def main ():

   
    rospy.init_node('first_serviceProxy')
    rate = rospy.Rate(2)
    def buttonLightOn ():
        buttonOneLightOnService = rospy.ServiceProxy('/module_services/module_1/digital_outputs/set_channel', SetBoolByIndexSrv)
        buttonOneLightOnRequest = SetBoolByIndexSrvRequest()
        buttonOneLightOnRequest.index = 0
        buttonOneLightOnRequest.value = True        
        
        buttonOneLightOnResponse = buttonOneLightOnService.call(
                buttonOneLightOnRequest
        )
    
    def buttonLightOff ():
        buttonOneLightOffService = rospy.ServiceProxy('/module_services/module_1/digital_outputs/set_channel', SetBoolByIndexSrv)
        buttonOneLightOffRequest = SetBoolByIndexSrvRequest()
        buttonOneLightOffRequest.index = 0
        buttonOneLightOffRequest.value = False        
        
        buttonOneLightOffResponse = buttonOneLightOffService.call(
            buttonOneLightOffRequest
        )

    def callback_input_data (msg):

        buttonLightState = 0 
        my_array = msg.values
        x = my_array[0]

        if (x == True and buttonLightState == 0):
            buttonLightOn ()
            buttonLightState = 1
            rospy.loginfo("Light On")
            rospy.loginfo(buttonLightState)

   


        if (x == True and buttonLightState == 1):
            buttonLightOff ()
            buttonLightState = 0
            rospy.loginfo("Light Off")
            rospy.loginfo(buttonLightState)
        
  
 
    sub = rospy.Subscriber('/module_topics/module_1/digital_inputs/channels', BoolArray, callback_input_data)
 
    
    
 
 
 
 
    #rospy.loginfo(response)
    
    
 
 
 
if __name__== '__main__':
    main()
    rospy.spin()