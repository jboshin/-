import sys
sys.path.append("~/MPU_test/main_program/main_program.py")

import main_program
import time

main_program.MPU_maincall()
while True:
    print "accel: ",int(round(main_program.get_date(),0))
    time.sleep(1)
