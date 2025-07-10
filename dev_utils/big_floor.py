import numpy as np
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.api import World
from isaacsim.core.api.objects import GroundPlane
from isaacsim.core.prims import SingleArticulation, XFormPrim

"""
def add_default_ground_plane(
        self,
        z_position: float = 0,
        name="default_ground_plane",
        prim_path: str = "/World/defaultGroundPlane",
        static_friction: float = 0.5,
        dynamic_friction: float = 0.5,
        restitution: float = 0.8,
    ) -> GroundPlane:
"""


def set_xform(prim_path, x, y, z, rot=None):
    xform = XFormPrim(prim_path)
    xform.set_world_poses(
        positions=np.array([list(map(float, [x, y, z]))]), orientations=rot
    )


world = World()

tile_halfsize = 50
n_tiles = 3

for ix in range(-n_tiles, n_tiles + 1):
    for iy in range(-n_tiles, n_tiles + 1):
        prim_path = f"/World/groundplane/tile_{ix}_{iy}".replace("-", "neg")
        name = prim_path.split("/")[-1]
        print(f"{prim_path=} {name=}")
        world.scene.add_default_ground_plane(prim_path=prim_path, name=name)

world.reset()

step = 2 * tile_halfsize
for ix in range(-n_tiles, n_tiles + 1):
    for iy in range(-n_tiles, n_tiles + 1):
        prim_path = f"/World/groundplane/tile_{ix}_{iy}".replace("-", "neg")
        set_xform(prim_path, ix * step, iy * step, 0)

while True:
    world.step(render=True)
