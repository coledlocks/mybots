# importing packages
from sensor import SENSOR
from motor import MOTOR
import pybullet as p

class ROBOT:

  def __init__(self):

    self.sensors = {}
    self.motors = {}
    self.robotId = p.loadURDF("body.urdf")
    pyrosim.Prepare_To_Simulate(robotId)
    self.robot.Prepare_to_Sense()
  def Prepare_to_Sense(self):
    self.sensors = {}
    for linkName in pyrosim.linkNamesToIndices:
      self.sensors[linkName] = SENSOR(linkName)

  def Sense(self):
    for i in range(self.sensors):
      self.sensors[i].Get_Values(t)
