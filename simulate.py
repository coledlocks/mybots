import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
from simulation import SIMULATION
import constants as c

backLegSensorValues = np.zeros(c.MAX_TIME)
frontLegSensorValues = np.zeros(c.MAX_TIME)

backLegMotorCommands = c.backLegAmplitude * np.sin(c.backLegFrequency * np.linspace(0., 2*np.pi, 1000) + c.backLegPhaseOffset)
frontLegMotorCommands = c.frontLegAmplitude * np.sin(c.frontLegFrequency * np.linspace(0., 2*np.pi, 1000) + c.frontLegPhaseOffset)

# scaling the target angles
backLegAngles = backLegMotorCommands * (np.pi/4.0)
frontLegAngles = frontLegMotorCommands * (np.pi/4.0)

# saving and exiting
# np.save("C:/Users/coled/PycharmProjects/mybots/data/backLegMotorCommands.npy", backLegMotorCommands)
# np.save("C:/Users/coled/PycharmProjects/mybots/data/frontLegMotorCommands.npy", frontLegMotorCommands)
# exit()

p.disconnect()

np.save("C:/Users/coled/PycharmProjects/mybots/data/backLegSensorValues.npy", backLegSensorValues)
np.save("C:/Users/coled/PycharmProjects/mybots/data/frontLegSensorValues.npy", frontLegSensorValues)

simulation = SIMULATE()
world = WORLD()
robot = ROBOT()
