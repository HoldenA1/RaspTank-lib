import move
import servo
import time
import ultra

def turn_left(degrees):
  move.moveTank(100,100)
  time.sleep(.008888*degrees)
  move.motorStop()
  
  
def turn_right(degrees):
  move.moveTank(-100,-100)
  time.sleep(.008888*degrees)
  move.motorStop()
  
def open_hand(degrees=-10):
  servo.hand(degrees)
  time.sleep(.15)
  
def close_hand(degrees=7):
  servo.hand(degrees)
  time.sleep(.15)

def read_ultrasonic():
  return ultra.checkdist()

def move_arm(position):
  servo.arm_pos(position)
  time.sleep(.2)
