import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER


phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
print("completed evolution", os.path.exists("fitness*.txt"))
phc.Show_Best()
print("showing best:", os.path.exists("fitness*.txt"))