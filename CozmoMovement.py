#In this sample code, you will learn how to program Cozmo to
#move forward, turn 90 degrees left or right, spin in a circle
#talk, and perform an animation


#import the cozmo and image libraries
import cozmo

#import libraries for movement 
from cozmo.util import degrees, distance_mm

#we shouldn't need anything for asynchronous behavior
#import asyncio

#import libraries for light colors.  If this library has not been
#acquired, comment out all actions involving colors

#from colors import Colors
#from woc import WOC

#import _thread
#import time

def moveInCircle(robot, speed, seconds):

    #robot.say_text("I will spin in three circles").wait_for_completed()
    #robot.set_all_backpack_lights(Colors.BLUE)
    
    #the first value is the speed for one of the treads, and the second value
    #is the speed for the other tread (left? right?).  They can both be
    #the same sign, or have opposite signs.  the last value is the duration of the
    #movement (measured in seconds?)
    robot.drive_wheels(speed, -1 * speed, None, None, seconds)
    #robot.set_all_backpack_lights(Colors.GREEN)
    return

def turnRight(robot):
    #robot.say_text("I will turn right").wait_for_completed()
    #robot.set_all_backpack_lights(Colors.RED)
    robot.turn_in_place(cozmo.util.degrees(-90)).wait_for_completed()
   # robot.set_all_backpack_lights(Colors.GREEN)
    return

def turnLeft(robot):
    robot.turn_in_place(cozmo.util.degrees(90)).wait_for_completed()
    return

# 0,0 to x,y; assuming coordinate values are for us and not something we need to take in
def cozmo_program1(robot: cozmo.robot.Robot):
    x = 5
    y = 7
    
    h_mm = x*100
    v_mm = y*100

    # Vertical movement
    robot.say_text("I will drive seven units").wait_for_completed()
    robot.drive_straight(cozmo.util.distance_mm(v_mm), cozmo.util.speed_mmps(200)).wait_for_completed()
    # Horizontal movement
    if h_mm > 0:
        turnRight(robot)
    if h_mm < 0:
        turnLeft(robot)
    robot.say_text("I will drive five units").wait_for_completed()    
    robot.drive_straight(cozmo.util.distance_mm(h_mm), cozmo.util.speed_mmps(200)).wait_for_completed()

    # Action: randomly chosen because I couldn't find a list of actions and didn't want to stick with the dog one
    # This is based on the random animation example from github
    all_animation_triggers = robot.anim_triggers
    random.shuffle(all_animation_triggers)
    chosen_trigger = all_animation_triggers[:1]
    robot.play_anim_trigger(chosen_trigger).wait_for_completed()
    return

# a,b to x,y 
def cozmo_program2(robot: cozmo.robot.Robot):
    a = 3
    b = 9
    x = 5
    y = 4
    
    h_mm = (x-a)*100
    v_mm = (y-b)*100
    
    # Vertical movement
    robot.say_text("I will drive five units").wait_for_completed()
    robot.drive_straight(cozmo.util.distance_mm(v_mm), cozmo.util.speed_mmps(200)).wait_for_completed()
    # Horizontal movement
    if h_mm > 0:
        turnRight(robot)
    if h_mm < 0:
        turnLeft(robot)    
    robot.say_text("I will drive two units").wait_for_completed()
    robot.drive_straight(cozmo.util.distance_mm(h_mm), cozmo.util.speed_mmps(200)).wait_for_completed()

    # Action
    all_animation_triggers = robot.anim_triggers
    random.shuffle(all_animation_triggers)
    chosen_trigger = all_animation_triggers[:1]
    robot.play_anim_trigger(chosen_trigger).wait_for_completed()
    return    

cozmo.run_program(cozmo_program1, use_viewer=False, force_viewer_on_top=False)
#cozmo.run_program(cozmo_program2, use_viewer=False, force_viewer_on_top=False)