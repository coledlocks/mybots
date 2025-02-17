import numpy as np
from matplotlib import pyplot as plt

backLegSensorValues = np.load("C:/Users/coled/PycharmProjects/mybots/data/backLegSensorValues.npy")
frontLegSensorValues = np.load("C:/Users/coled/PycharmProjects/mybots/data/frontLegSensorValues.npy")

backLegMotorCommands = np.load("C:/Users/coled/PycharmProjects/mybots/data/backLegMotorCommands.npy")
frontLegMotorCommands = np.load("C:/Users/coled/PycharmProjects/mybots/data/frontLegMotorCommands.npy")

#print(backLegSensorValues)
#print(frontLegSensorValues)

#plt.plot(backLegSensorValues, label='Back Leg', linewidth = 2)
#plt.plot(frontLegSensorValues, label='Front Leg', alpha = 0.6)
plt.plot(backLegMotorCommands, label="Back Leg", linewidth=2)
plt.plot(frontLegMotorCommands, label="Front Leg", alpha=0.6)

plt.title("Motor Commands")
plt.ylabel("Value in Radians")
plt.legend()
plt.show()