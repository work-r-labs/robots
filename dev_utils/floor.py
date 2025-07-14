from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.api import World
from isaacsim.core.prims import SingleArticulation, XFormPrim
from isaacsim.sensors.camera import Camera

world = World()

world.scene.add_default_ground_plane()

while True:
    world.step(render=True)
