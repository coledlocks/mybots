from simulation import SIMULATION
import sys

directOrGUI = sys.argv[1]

# directOrGUI = "GUI"

simulation = SIMULATION(directOrGUI)
simulation.Run()
simulation.Get_Fitness()