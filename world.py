import pybullet as p

class WORLD:
  def __init__(self):
    # Create a thin box (runway) instead of the default plane
    runway_length = 25  # meters
    runway_width = 2  # meters
    runway_thickness = 0.1  # meters (thin surface)

    # Create collision shape and visual shape
    runway_collision = p.createCollisionShape(p.GEOM_BOX,
                                              halfExtents=[runway_length / 2, runway_width / 2, runway_thickness / 2])
    runway_visual = p.createVisualShape(p.GEOM_BOX,
                                        halfExtents=[runway_length / 2, runway_width / 2, runway_thickness / 2],
                                        rgbaColor=[0.5, 0.5, 0.5, 1])  # Gray color

    # Position the runway so it starts at the origin and extends forward (+X)
    # The center of the box is at [runway_length/2, 0, -thickness/2]
    self.runwayId = p.createMultiBody(
        baseMass=0,  # Static object
        baseCollisionShapeIndex=runway_collision,
        baseVisualShapeIndex=runway_visual,
        basePosition=[2-runway_length / 2, 0, -runway_thickness / 2])

    # Load the rest of your world
    p.loadSDF("world.sdf")