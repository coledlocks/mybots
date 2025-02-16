import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

start_length, start_width = 0, 0 # starting x, y location of cube

# this function creates a tower of 10 cubes with each cube being 90% of the dimensions as the one below it
def cube_tower(start_length, start_width):
    length, width, height, total_height = 1, 1, 1, 1 # initial parameters of bottom cube
    start_height = 0.5
    for i in range(10):
        pyrosim.Send_Cube(name="Box", pos=[start_length, start_width, start_height], size=[length, width, height])
        length, width, height = 0.9 * length, 0.9 * width, 0.9 * height # decreasing the cube parameters by 10%
        start_height = total_height + height / 2 # setting a new starting height so cube sits on previous cube
        total_height += height

# nested for loops placing all the towers
for i in range(5):
    for j in range(5):
        cube_tower(start_length, start_width)
        start_length += 1
    start_width += 1
    start_length = 0

pyrosim.End()