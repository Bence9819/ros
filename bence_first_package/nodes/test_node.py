#!/usr/bin/env python3
 
 
from multiprocessing.sharedctypes import Value
 
import rospy
from faketelen_platform_msgs.srv import SetBoolByIndexSrv, SetBoolByIndexSrvRequest, GetBoolByIndexSrv, GetBoolByIndexSrvRequest,GetBoolByIndexSrvResponse
from faketelen_platform_msgs.msg import BoolArray, BoolEvent
 
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

def buttonLightState ():
    buttonOneLightStateService = rospy.ServiceProxy('/module_services/module_1/digital_outputs/get_channel', GetBoolByIndexSrv)
    buttonOneLightStateRequest = GetBoolByIndexSrvRequest()
    buttonOneLightStateRequest.index = 0
    buttonOneLightStateResponse = GetBoolByIndexSrvResponse()

    buttonOneLightStateResponse = buttonOneLightStateService.call(
        buttonOneLightStateRequest
    )
    return buttonOneLightStateRequest


def main ():

    rospy.init_node('first_serviceProxy')
    
    def callback_input_data (msg):

        my_array = msg.values
        input_data = my_array[0]
        if input_data == True:
            buttonLightOn()

            # out: "index: 0"
            rospy.loginfo(buttonLightState())

        
 
    sub = rospy.Subscriber('/module_topics/module_1/digital_inputs/channels', BoolArray, callback_input_data)
 

if __name__== '__main__':
    main()
    rospy.spin()