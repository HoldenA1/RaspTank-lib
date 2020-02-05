import move
import servo
import time
import ultra
servo.clean_all()

count=-4
while(count<5):
    servo.arm_pos(count)
    count+=1
    time.sleep(1)
    
servo.hand(-180)
time.sleep(1)
servo.hand(180)
time.sleep(1)

servo.wrist(-15)
time.sleep(1)
servo.wrist(15)
time.sleep(1)

move.moveArcade(50,10)



for e in range(10):
  print(ultra.checkdist())
  time.sleep(.2)
    
 

servo.clean_all()
