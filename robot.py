# importing packages
from sensor import SENSOR
from motor import MOTOR
import os
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
  def __init__(self, solutionID):
    self.nn = NEURAL_NETWORK(f"brain{solutionID}.nndf")
    self.motors = {}
    self.sensors = {}
    self.robotId = p.loadURDF("body.urdf")
    pyrosim.Prepare_To_Simulate(self.robotId)
    self.Prepare_To_Sense()
    self.Prepare_To_Act()
    os.system(f"del brain{solutionID}.nndf")


  def Prepare_To_Sense(self):
    self.sensors = {}
    for linkName in pyrosim.linkNamesToIndices:
      self.sensors[linkName] = SENSOR(linkName)

  def Sense(self, t):
    for i in self.sensors:
      self.sensors[i].Get_Value(t)

  def Prepare_To_Act(self):
    self.motors = {}
    for jointName in pyrosim.jointNamesToIndices:
      self.motors[jointName] = MOTOR(jointName)

  def Act(self, t):
    for neuronName in self.nn.Get_Neuron_Names():
      if self.nn.Is_Motor_Neuron(neuronName):
        jointName = self.nn.Get_Motor_Neurons_Joint(neuronName).encode("utf-8")
        desiredAngle = self.nn.Get_Value_Of(neuronName)
        self.motors[jointName].Set_Value(self.robotId, desiredAngle)
        # jointName = jointName.decode("utf-8")
        # print(neuronName, jointName, desiredAngle)

  def Think(self):
    self.nn.Update()

  def Get_Fitness(self, solutionID):
    self.stateOfLinkZero = p.getLinkState(self.robotId, 0)
    self.positionOfLinkZero = self.stateOfLinkZero[0]
    self.xCoordinateOfLinkZero = self.positionOfLinkZero[0]
    # print(self.stateOfLinkZero)

    with open(f"tmp{solutionID}.txt", 'w') as f:
      f.write(str(self.xCoordinateOfLinkZero))

    os.system(f"rename tmp{solutionID}.txt fitness{solutionID}.txt")
    # os.rename("tmp" + str(solutionID) + ".txt", "fitness" + str(solutionID) + ".txt")
