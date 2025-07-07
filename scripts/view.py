import math
import numpy as np
from pathlib import Path
from isaacsim import SimulationApp

simulation_app = SimulationApp({"headless": False})

from isaacsim.core.utils.stage import add_reference_to_stage
from isaacsim.core.api import World
from isaacsim.core.prims import SingleArticulation, XFormPrim

world = World()

project_root = Path(__file__).parent.parent

usd_paths = [
    # "generated/CRB15000_10kg_152_v1/CRB15000_10kg_152/CRB15000_10kg_152.usd",
    # "generated/CRB15000_12kg_127_v1/CRB15000_12kg_127/CRB15000_12kg_127.usd",
    # "generated/CRB15000_5kg_950_v1/CRB15000_5kg_950/CRB15000_5kg_950.usd",
    # "generated/IRB1010_1_5kg_370_v1/IRB1010_1_5kg_370/IRB1010_1_5kg_370.usd",
    # "generated/IRB1100_4kg_475_STD_v1/IRB1100_4kg_475_STD/IRB1100_4kg_475_STD.usd",
    # "generated/IRB1100_4kg_580_STD_v1/IRB1100_4kg_580_STD/IRB1100_4kg_580_STD.usd",
    # "generated/IRB1200_5_90_STD_v1/IRB1200_5_90_STD/IRB1200_5_90_STD.usd",
    # "generated/IRB1200H_5_90_STD_v1/IRB1200H_5_90_STD/IRB1200H_5_90_STD.usd",
    # "generated/IRB1200H_7_70_STD_v1/IRB1200H_7_70_STD/IRB1200H_7_70_STD.usd",
    # "generated/IRB1520ID_4_150_v1/IRB1520ID_4_150/IRB1520ID_4_150.usd",
    # "generated/IRB1600_X-120_v1/IRB1600_X-120/IRB1600_X-120.usd",
    # "generated/IRB460_110-240_v1/IRB460_110-240/IRB460_110-240.usd",
    # "generated/IRB52_7-1_2-Short_v1/IRB52_7-1_2-Short/IRB52_7-1_2-Short.usd",
    # "generated/IRB52_7-1_45-Long_v1/IRB52_7-1_45-Long/IRB52_7-1_45-Long.usd",
    "generated/IRB5500-22_v1/IRB5500-22/IRB5500-22.usd",
    "generated/IRB5500-27_v1/IRB5500-27/IRB5500-27.usd",
    "generated/IRB5510-12_v1/IRB5510-12/IRB5510-12.usd",
    # "generated/IRB6750S_185-390-LID_v1/IRB6750S_185-390-LID/IRB6750S_185-390-LID.usd",
    # "generated/IRB8700_550-420-SW6_v1/IRB8700_550-420-SW6/IRB8700_550-420-SW6.usd",
    # "generated/IRB8700_800_350_v1/IRB8700_800_350/IRB8700_800_350.usd",
    # "generated/IRB920_6kg_550_180_STD_v1/IRB920_6kg_550_180_STD/IRB920_6kg_550_180_STD.usd",
    # "generated/abb_irb920_v1/abb_irb920/abb_irb920.usd",
]
usd_paths = [project_root / p for p in usd_paths]


world.scene.add_default_ground_plane()

def sanitize_name(name: str) -> str:
    return name.replace("-", "_")


spacing = 2         # m  – centre-to-centre distance between robots
n       = len(usd_paths)
side    = math.ceil(math.sqrt(n)) 
robots = []
for i, usd_path in enumerate(usd_paths):
    print(f"Loading {usd_path}")
    prim_path = sanitize_name(f"/world/robots/{usd_path.stem}")
    add_reference_to_stage(str(usd_path), prim_path)

    row, col = divmod(i, side)      # integer grid coordinates
    x = col * spacing               # metres in X
    y = row * spacing               # metres in Y
    z = 0.0  

    xform = XFormPrim(prim_path)
    xform.set_local_poses(
        translations=np.array([[x, y, z]]),
    )

    robot = SingleArticulation(prim_path=prim_path)
    robots.append(robot)

world.reset()

while True:
    world.step(render=True)
