# importing packages
from sensor import SENSOR
from motor import MOTOR
import pybullet as p
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK

class ROBOT:
  def __init__(self):
    self.sensors = {}
    self.motors = {}
    self.robotId = p.loadURDF("body.urdf")
    self.nn = NEURAL_NETWORK("brain.nndf")
    pyrosim.Prepare_To_Simulate(self.robotId)
    self.Prepare_To_Sense()
    self.Prepare_To_Act()


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
        jointName = jointName.decode("utf-8")
        print(neuronName, jointName, desiredAngle)
    # for i in self.motors:
    #   print(f'THIS IS i: {i}, use these: {list(self.motors.keys())}')
    #   self.motors[i].Set_Value(self.robotId, t)

  def Think(self, t):
    self.nn.Update()
    self.nn.Print()
