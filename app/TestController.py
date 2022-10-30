#!/usr/bin/env python3
#encoding=utf-8
import time
from robot_arm_control.robot_arm_controller import ControlArmController

controller = ControlArmController()

def test_single_servo_pass():
    """ main function """
    start_execution()
    time.sleep(.1)
    controller.send_servo_command()
    
def start_execution():
    """start execution message"""
    print("Hello World! from a multi arm container")


if __name__=="__main__":
    test_single_servo_pass()
