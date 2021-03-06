import move
import servo
import time
import ultra
import linetracking
import LED

status_right = linetracking.status_right
status_left = linetracking.status_left
status_middle = linetracking.status_middle


def turn_left(degrees):
  move.moveTank(100,100)
  time.sleep(.008888*degrees)
  move.motorStop()
  
  
def turn_right(degrees):
  move.moveTank(-100,-100)
  time.sleep(.008888*degrees)
  move.motorStop()

def move_forward(seconds):
   move.moveTank(-100,100)
   time.sleep(seconds)

def move_backwards(seconds):
   move.moveTank(100,-100)
   time.sleep(seconds)
  
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
  
def move_wrist(degrees):
  #-90 to 90 degrees
  servo.wrist(int((degrees/12)+6))
  time.sleep(.25)
  
def white_light(time):
  led2 = LED.LED(640000)
  led2.colorWipe(10, wait_ms=time/12)
  
def blue_light(time):
  led = LED.LED(800000)
  led.colorWipe(10, wait_ms=time/12)
  
def loop(functions):
  while True:
    text = input("")
    function_names = [e.__name__ for e in functions]
    if text in function_names:
      functions[function_names.index(text)]()
