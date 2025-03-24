
# import packages
from world import WORLD
from robot import ROBOT
import pybullet_data
import pybullet as p
import pyrosim.pyrosim as pyrosim
import constants as c
import time

class SIMULATION:
  def __init__(self, directOrGUI, solutionID):
    self.runSetting = directOrGUI
    self.solutionID = solutionID
    if directOrGUI == 'DIRECT':
      self.physicsClient = p.connect(p.DIRECT)
    if directOrGUI == 'GUI':
      self.physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.configureDebugVisualizer(p.COV_ENABLE_GUI, 1)  # set to 0 to enable
    p.setGravity(0, 0, -9.8)

    # initialize world and robot
    self.world = WORLD()
    self.robot = ROBOT(self.solutionID)

    pyrosim.Prepare_To_Simulate(self.robot.robotId)

  def Run(self):
    for t in range(c.MAX_TIME):
      p.stepSimulation()
      self.robot.Sense(t)
      self.robot.Think(t)
      self.robot.Act(t)
      if self.runSetting == 'GUI':
        time.sleep(1 / 60)

  def Get_Fitness(self):
    self.robot.Get_Fitness(self.solutionID)

  def __del__(self):
    p.disconnect()