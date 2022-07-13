#!/usr/bin/python
import smbus
import math
import time

# Power management registers
power_mgmt_1 = 0x6b
power_mgmt_2 = 0x6c

bus = smbus.SMBus(1) # or bus = smbus.SMBus(1) for Revision 2 boards
address = 0x68       # This is the address value read via the i2cdetect command

#global
circle = 3 #set max circle
time2 = 0 #new time
time4 = 0 #gyro new time
v_rotation = circle*180 #base (circle*360)
gyro_v_rotation = 540
threed_rotation=540
angle = 0 #rotation of gyro
new_x = 1
new_y = 1
new_z = 1

def get_date(): #all data in here
       return wheel_rotation()

'''
def threeD_rotation():
    global new_x
    global new_y
    global new_z
    global threed_rotation

    old_x=new_x
    new_x=get_x_rotation(accel_xout_scaled()+0.52, accel_yout_scaled()-0.07, accel$
    old_y=new_y
    new_y=get_y_rotation(accel_xout_scaled()+0.52, accel_yout_scaled()-0.07, accel$
    old_z=new_z
    new_z=get_z_rotation(accel_xout_scaled()+0.52, accel_yout_scaled()-0.07, accel$

    threed_rotation=threed_rotation+math.acos(( (old_x*new_x)+(old_y*new_y)+(old_z$
    return threed_rotation
'''
'''
def gyro_rotation():
    global angle
    global time4
    global gyro_v_rotation

    rotation = -get_x_rotation(accel_xout_scaled()+0.52, accel_yout_scaled()-0.07,$
    time3=time4 #past time
    time4=rotation #new time
    transition = time4 - time3
    angle = 0.98 * (angle + (gyro_xout()/131) * 0.05) + 0.02 * transition

    if abs(transition) > 180: #turn over then 180
        if transition > 0: #turn right
                   gyro_v_rotation = gyro_v_rotation + angle # base - rotation   #$
        else: #turn left
                   gyro_v_rotation = gyro_v_rotation - angle # base + rotation
    else: #turn less then 180
        gyro_v_rotation = gyro_v_rotation + transition #base(540)+rotation

    if gyro_v_rotation <= 0:
        return 0
    elif gyro_v_rotation < post_data():
        return gyro_v_rotation
    else:
        return post_data()
'''

'''
def all_information():
    print "accelerometer data"
    print "------------------"
    print "accel_zout: ", accel_zout(), " scaled: ", accel_zout_scaled()
    print "z rotation: " , get_z_rotation(accel_xout_scaled(), accel_yout_scaled()$
    if get_z_rotation(accel_xout_scaled(), accel_yout_scaled(), accel_zout_scaled($
       print "Rotation: " , wheel_rotation()
    else:
       print "max rotation: " , post_data()
    print "max rotation: " , post_data()
'''

def wheel_rotation():
    global v_rotation
    global time2

    rotation = -get_z_rotation(accel_xout_scaled()+0.49, accel_yout_scaled()-0.025, accel_zout_scaled()-0.01)
    print "rotation:",rotation
    print "x:",accel_xout_scaled(),"y:" ,accel_yout_scaled(),"z:", accel_zout_scaled()
    time1=time2 #past time
    time2=rotation #new time
    transition = time2 - time1
    print "transition:",transition
    if abs(transition) > 180: #turn over then 180
        if transition > 0: #turn right
            v_rotation = v_rotation - (360 - abs(transition)) # base - rotatio$
        else: #turn left
            v_rotation = v_rotation + (360 - abs(transition)) # base + rotatio$
    else: #turn less then 180
        v_rotation = v_rotation + transition #base(540)+rotation

    if v_rotation <= 0: #set border
        return 0
    elif v_rotation < post_data():
        return v_rotation
    else:
        return post_data()


def post_data(): #max rotation
    global circle
    max_rotation = 360 * circle
    return max_rotation

#orginal data
def gyro_xout():
    gyro_xout = read_word_2c(0x43)
    return gyro_xout
def gyro_yout():
    gyro_yout = read_word_2c(0x45)
    return gyro_yout
def gyro_zout():
    gyro_zout = read_word_2c(0x47)
    return gyro_zout
def accel_xout():
    accel_xout = read_word_2c(0x3b)
    return accel_xout
def accel_yout():
    accel_yout = read_word_2c(0x3d)
    return accel_yout
def accel_zout():
    accel_zout = read_word_2c(0x3f)
    return accel_zout
def accel_xout_scaled():
    accel_xout = read_word_2c(0x3b)
    accel_xout_scaled = accel_xout/ 16384.0
    return -accel_xout_scaled
def accel_yout_scaled():
    accel_yout = read_word_2c(0x3d)
    accel_yout_scaled = accel_yout/ 16384.0
    return -accel_yout_scaled
def accel_zout_scaled():
    accel_zout = read_word_2c(0x3f)
    accel_zout_scaled = accel_zout/ 16384.0
    return -accel_zout_scaled
def read_byte(adr):
	return bus.read_byte_data(address, adr)
def read_word(adr):
    high = bus.read_byte_data(address, adr)
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    low = bus.read_byte_data(address, adr+1)
    val = (high << 8) + low
    return val
def read_word_2c(adr):
    val = read_word(adr)
    if (val >= 0x8000):
        return -((65535 - val) + 1)
    else:
        return val
def dist(a,b):
    return math.sqrt((a*a)+(b*b))
def get_y_rotation(x,y,z):
    radians = math.atan2(x, dist(y,z))
    return -math.degrees(radians)
def get_x_rotation(x,y,z):
    radians = math.atan2(y, dist(x,z))
    return math.degrees(radians)
def get_z_rotation(x,y,z):
    radians =math.atan2(dist(x,y),z)
    return -math.degrees(radians)
def MPU_maincall():
    # Now wake the 6050 up as it starts in sleep mode
    bus.write_byte_data(address, power_mgmt_1, 0)

'''
#main
MPU_maincall()
while True:
    print "accel: ",int(round(get_date(),0))
    print "gyro:  ",int(round(gyro_rotation(),0))
    time.sleep(0.05)
'''
