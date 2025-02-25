# importing packages
import constants as c
import numpy as np

class SENSOR:

  def __init__(self):
    self.linkName = linkeName
    self.values = np.zeros(c.MAX_TIME)

  def Get_Value(self):
    self.linkName[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName[i])
