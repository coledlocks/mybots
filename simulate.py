import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

backLegAmplitude = np.pi/6
backLegFrequency = 50
backLegPhaseOffset = 0
frontLegAmplitude = np.pi/6
frontLegFrequency = 25
frontLegPhaseOffset = np.pi/3

# setting up physics client
physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())
#p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

backLegMotorCommands = backLegAmplitude * np.sin(backLegFrequency * np.linspace(0., 2*np.pi, 1000) + backLegPhaseOffset)
frontLegMotorCommands = frontLegAmplitude * np.sin(frontLegFrequency * np.linspace(0., 2*np.pi, 1000) + frontLegPhaseOffset)

# scaling the target angles
backLegAngles = backLegMotorCommands * (np.pi/4.0)
frontLegAngles = frontLegMotorCommands * (np.pi/4.0)

# saving and exiting
# np.save("C:/Users/coled/PycharmProjects/mybots/data/backLegMotorCommands.npy", backLegMotorCommands)
# np.save("C:/Users/coled/PycharmProjects/mybots/data/frontLegMotorCommands.npy", frontLegMotorCommands)
# exit()

for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robotId,

        jointName=b'Torso_BackLeg',

        controlMode=p.POSITION_CONTROL,

        targetPosition=backLegMotorCommands[i],

        maxForce=100)
    pyrosim.Set_Motor_For_Joint(

        bodyIndex=robotId,

        jointName=b'Torso_FrontLeg',

        controlMode=p.POSITION_CONTROL,

        targetPosition=frontLegMotorCommands[i],

        maxForce=100)
    time.sleep(1/240)

p.disconnect()

np.save("C:/Users/coled/PycharmProjects/mybots/data/backLegSensorValues.npy", backLegSensorValues)
np.save("C:/Users/coled/PycharmProjects/mybots/data/frontLegSensorValues.npy", frontLegSensorValues)