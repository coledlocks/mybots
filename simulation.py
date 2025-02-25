# import packages
from world import WORLD
from robot import ROBOT
import pybullet as p

class SIMULATION:

  def __init__(self):
    # set up physics client
    self.physicsClient = p.connect(p.GUI)
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    #p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
    p.setGravity(0,0,-9.8)

    # initialize world and robot
    self.world = WORLD()
    self.robot = ROBOT()

def Run():
  for t in range(c.MAX_TIME):
    print(t)
    # p.stepSimulation()
    # pyrosim.Set_Motor_For_Joint(

    #     bodyIndex=robotId,

    #     jointName=b'Torso_BackLeg',

    #     controlMode=p.POSITION_CONTROL,

    #     targetPosition=backLegMotorCommands[i],

    #     maxForce=100)
    # pyrosim.Set_Motor_For_Joint(

    #     bodyIndex=robotId,

    #     jointName=b'Torso_FrontLeg',

    #     controlMode=p.POSITION_CONTROL,

    #     targetPosition=frontLegMotorCommands[i],

    #     maxForce=100)
    time.sleep(1/240)

# calling the run function
Run()

# disconnecting the simulation
def __del__(self):

    p.disconnect()
