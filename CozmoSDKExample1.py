#In this sample code, you will learn how to program Cozmo to
#move forward, turn 90 degrees left or right, spin in a circle
#talk, and perform an animation
import random

#import the cozmo and image libraries
import cozmo

#import libraries for movement 
from cozmo.util import degrees, distance_mm

#we shouldn't need these for this demonstration
#import _thread
#import time
'''
def moveAround(robot, speed1, speed2, seconds):

	#the first value is the speed for one of the treads, and the second value
	#is the speed for the other tread (left? right?).  They can both be
	#the same sign, or have opposite signs.  the last value is the duration of the
	#movement (measured in seconds?)
	#the radius of the circle is measured in mm.t
	robot.drive_wheels(speed1, speed2, None, None, seconds)
	return
'''
def cozmo_program(robot: cozmo.robot.Robot):
	
	# Move lift down and tilt the head up
	#robot.move_lift(10)
	robot.move_lift(0)
	#robot.set_head_angle(degrees(0)).wait_for_completed()
	#make an announcment and drive off contacts
	#robot.say_text("I will move off of the charger").wait_for_completed()
	#robot.drive_straight(cozmo.util.distance_mm(400), cozmo.util.speed_mmps(150)).wait_for_completed()
	#robot.drive_off_charger_contacts().wait_for_completed()
	
	#robot.say_text("I will now move forward").wait_for_completed()

	#robot, speed, speed, seconds
	#moveAround(robot, 250, 250, 2)
	
	#robot.say_text("I will now make some turns").wait_for_completed()
	#moveAround(robot, 250, 200, 2)
	#moveAround(robot, 100, 200, 2)
	#moveAround(robot, 150, 250, 3)
	
	#robot.say_text("I will now move forward one more time").wait_for_completed()
	#moveAround(robot, 250, 250, 2)
	
	#robot.say_text("I am tired.").wait_for_completed()
	
	return

cozmo.run_program(cozmo_program, use_viewer=False, force_viewer_on_top=False)
