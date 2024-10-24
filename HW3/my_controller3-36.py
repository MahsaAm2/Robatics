"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot


# create the Robot instance.
robot = Robot()
timestep=64

# get the time step of the current world.
# timestep = int(robot.getBasicTimeStep())
timestep=64

# You should insert a getDevice-like function in order to get the
# instance of a device of the robot. Something like:
#  motor = robot.getDevice('motorname')
#  ds = robot.getDevice('dsname')
#  ds.enable(timestep)

m1=robot.getDevice("rotational_motor1")
m2=robot.getDevice("linear_motor")
m3=robot.getDevice("rotational_motor2")

m1.setPosition(float('inf'))
m1.setVelocity(0.0)

m2.setPosition(float('inf'))
m2.setVelocity(0.0)

m3.setPosition(float('inf'))
m3.setVelocity(0.0)


       
l2 = 0.2


theta1 = 0.78

theta3 = 0.52

d2 = 0.3
# or
# d2 = (a[1][3]/a[1][2]) - l2

# Main loop:
# - perform simulation steps until Webots is stopping the controller
speed=1
print(theta1, theta3, d2)
while robot.step(timestep) != -1:
    # Read the sensors:
    # Enter here functions to read sensor data, like:
    #  val = ds.getValue()
    m1.setPosition(theta1)
    m1.setVelocity(speed)
    
    m2.setPosition(d2)
    m2.setVelocity(speed)
    
    m3.setPosition(theta3)
    m3.setVelocity(speed)

    # Process sensor data here.

    # Enter here functions to send actuator commands, like:
    #  motor.setPosition(10.0)
    pass

# Enter here exit cleanup code.
