#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device

class ControlArmController:
    """Control the arm with the servo manipulator, provide {angle} and {time} to move"""
    def __init__(self):
        self.arm_device = Arm_Device()

    def control_single_servo(self, servo, angle, s_time = 500):
        """Control a servo separately"""
        self.arm_device.Arm_serial_servo_write(servo, angle, s_time)
        time.sleep(1)
          
    def control_all_servo(self, angle, s_time = 500):
        """Control the arm with the servo manipulator, provide {angle} and {time} to move"""
        self.arm_device.Arm_serial_servo_write6(angle, 180-angle,
                                                angle, angle, angle, angle, s_time)
        time.sleep(s_time/1000)

    def send_servo_command(self, angle = 90, s_time = 500, counter = 0):
        """Sends the command to the servo and can also loop through variations"""
        print("Calling control arm function on Arm_Lib")
        dir_state = 1
        angle = 90

        self.arm_device.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90, s_time)
        time.sleep(1)
        while counter < 5:
            if dir_state == 1:
                angle += 1
                if angle >= 180:
                    dir_state = 0
            else:
                angle -= 1
                if angle <= 0:
                    dir_state = 1
            counter+=1
            self.control_single_servo(angle, 10)
            time.sleep(10/1000)
            print(angle)
