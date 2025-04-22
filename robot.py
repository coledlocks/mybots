# importing packages
import constants as c
from sensor import SENSOR
from motor import MOTOR
import os
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
from pyrosim.neuralNetwork import NEURAL_NETWORK
import time

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
          desiredAngle = self.nn.Get_Value_Of(neuronName) * c.motorJointRange
          self.motors[jointName].Set_Value(self.robotId, desiredAngle)
        # jointName = jointName.decode("utf-8")
        # print(neuronName, jointName, desiredAngle)

  def Think(self):
    self.nn.Update()

  def Get_Fitness(self, solutionID):
    self.start_time = time.time()

    self.basePositionAndOrientation = p.getBasePositionAndOrientation(self.robotId)
    self.basePosition = self.basePositionAndOrientation[0]
    self.xPosition = self.basePosition[0]

    if self.xPosition == -25:
      self.runway_end_reached = True
      self.end_time = time.time()
      time_taken = self.end_time - self.start_time
      print(f'Robot reached the end! Time taken: {time_taken} seconds')
      self.fitness = self.xPosition - 25/(time_taken/60) # -25 is the end position of the runway
    else:
      self.fitness = self.xPosition


    with open(f"tmp{solutionID}.txt", 'w') as f:
      f.write(str(self.fitness))

    os.system(f"rename tmp{solutionID}.txt fitness{solutionID}.txt")
    # os.rename("tmp" + str(solutionID) + ".txt", "fitness" + str(solutionID) + ".txt")
