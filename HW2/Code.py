import numpy as np
from AIUT_RoboticsToolbox.Toolbox import *

d =1
d2 =0
links = np.array([[0.0, 0.0, 0.0, 0.0, 0],
                 [np.pi/2, d, d2, 0.0, 1],
                  [-np.pi/2, 0.0 , 0.0, 0.0 ,0]])

robot = SerialLink('Example 3.36', links)
T = robot.fkin([np.pi/6,4.0,np.pi/4])
print('T=', T)
robot.plot()