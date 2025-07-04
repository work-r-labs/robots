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
    "generated/abb_irb920_v1/abb_irb920/abb_irb920.usd",
    "generated/IRB1100_4kg_580_STD_v1/IRB1100_4kg_580_STD/IRB1100_4kg_580_STD.usd",
    "generated/IRB1200H_5_90_STD_v1/IRB1200H_5_90_STD/IRB1200H_5_90_STD.usd",
    "generated/CRB15000_5kg_950_v1/CRB15000_5kg_950/CRB15000_5kg_950.usd",
    "generated/IRB8700_800_350_v1/IRB8700_800_350/IRB8700_800_350.usd",
    "generated/CRB15000_10kg_152_v1/CRB15000_10kg_152/CRB15000_10kg_152.usd",
    "generated/IRB1200H_7_70_STD_v1/IRB1200H_7_70_STD/IRB1200H_7_70_STD.usd",
    "generated/CRB15000_12_127_v1/CRB15000_12_127/CRB15000_12_127.usd",
    "generated/IRB1200_5_90_STD_v1/IRB1200_5_90_STD/IRB1200_5_90_STD.usd",
    "generated/IRB1100_4kg_475_STD_v1/IRB1100_4kg_475_STD/IRB1100_4kg_475_STD.usd",
    "generated/IRB1010_1_5kg_370_v1/IRB1010_1_5kg_370/IRB1010_1_5kg_370.usd",
]
usd_paths = [project_root / p for p in usd_paths]


world.scene.add_default_ground_plane()
for i, usd_path in enumerate(usd_paths):
    prim_name = f"/world/robots/{usd_path.stem}"
    add_reference_to_stage(str(usd_path), prim_name)

    xform = XFormPrim(prim_name)
    xform.set_local_poses(
        translations=np.array([[float(0), float(i * 0.8), float(0)]]),
    )

world.reset()

while True:
    world.step(render=True)
