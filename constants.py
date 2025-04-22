import numpy as np

# max time of simulation
MAX_TIME = 10000

# general amplitude values
amplitude = np.pi / 4
frequency = 60
phaseOffset = 0

# number of sensor and motor neurons
numSensorNeurons = 9
numMotorNeurons = 8

t = np.linspace(0, 2 * np.pi, MAX_TIME)

# back and front leg values
backLegAmplitude = np.pi/4
backLegFrequency = 30
backLegPhaseOffset = 0
frontLegAmplitude = -np.pi/1.75
frontLegFrequency = 0
frontLegPhaseOffset = np.pi/3

motorJointRange = 0.5

# number of generations
numberOfGenerations = 20

# pop size
populationSize = 20