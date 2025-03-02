import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim
import pybullet as p


class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.values = np.zeros(c.MAX_TIME)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        # oscillating at diff frequencies
        if self.jointName == 'Torso_BackLeg':
            self.frequency = c.frequency / 4
        self.offset = c.phaseOffset
        self.values = (self.amplitude * np.sin(self.frequency * c.t + self.offset))

    def Set_Value(self, robot, t):
        pyrosim.Set_Motor_For_Joint(
            bodyIndex=robot,
            jointName=self.jointName,
            controlMode=p.POSITION_CONTROL,
            targetPosition=self.values[t],
            maxForce=100)

    def Save_Values(self):
        np.save(f"./data/{self.jointName}-motor-values.npy", self.values)
