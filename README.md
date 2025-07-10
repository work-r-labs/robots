# ABB Robot Models Repository

Plug and play USD and URDF assets for ABB robots, ready for use in IsaacSim and other robotics applications.

![Alt text](docs/release_video.png)

[Release Announcement](https://www.linkedin.com/feed/update/urn:li:activity:7348423533506547712/)

## Quickstart

```bash
# clone the repo, including the submodule required for type hinting
git clone --recurse-submodules https://github.com/work-r-labs/robots.git

# load a cobot and move it backwards and forwards
~/isaacsim/python.sh scripts/hello_world.py library/ABB/CRB15000_10kg_152_v1/CRB15000_10kg_152.urdf
```

## Available Robot Models

| Brand | Name | Type | URDF | USD |
|-------|------|------|------|-----|
| ABB | CRB15000_10kg_152 | Cobot | [URDF](library/ABB/CRB15000_10kg_152_v1/CRB15000_10kg_152.urdf) | [USD](library/ABB/CRB15000_10kg_152_v1/CRB15000_10kg_152/CRB15000_10kg_152.usd) |
| ABB | CRB15000_12kg_127 | Cobot | [URDF](library/ABB/CRB15000_12kg_127_v1/CRB15000_12kg_127.urdf) | [USD](library/ABB/CRB15000_12kg_127_v1/CRB15000_12kg_127/CRB15000_12kg_127.usd) |
| ABB | CRB15000_5kg_950 | Cobot | [URDF](library/ABB/CRB15000_5kg_950_v1/CRB15000_5kg_950.urdf) | [USD](library/ABB/CRB15000_5kg_950_v1/CRB15000_5kg_950/CRB15000_5kg_950.usd) |
| ABB | IRB1010_1_5kg_370 | Industrial Robot | [URDF](library/ABB/IRB1010_1_5kg_370_v1/IRB1010_1_5kg_370.urdf) | [USD](library/ABB/IRB1010_1_5kg_370_v1/IRB1010_1_5kg_370/IRB1010_1_5kg_370.usd) |
| ABB | IRB1100_4kg_475_STD | Industrial Robot | [URDF](library/ABB/IRB1100_4kg_475_STD_v1/IRB1100_4kg_475_STD.urdf) | [USD](library/ABB/IRB1100_4kg_475_STD_v1/IRB1100_4kg_475_STD/IRB1100_4kg_475_STD.usd) |
| ABB | IRB1100_4kg_580_STD | Industrial Robot | [URDF](library/ABB/IRB1100_4kg_580_STD_v1/IRB1100_4kg_580_STD.urdf) | [USD](library/ABB/IRB1100_4kg_580_STD_v1/IRB1100_4kg_580_STD/IRB1100_4kg_580_STD.usd) |
| ABB | IRB1200_5_90_STD | Industrial Robot | [URDF](library/ABB/IRB1200_5_90_STD_v1/IRB1200_5_90_STD.urdf) | [USD](library/ABB/IRB1200_5_90_STD_v1/IRB1200_5_90_STD/IRB1200_5_90_STD.usd) |
| ABB | IRB1200H_5_90_STD | Industrial Robot | [URDF](library/ABB/IRB1200H_5_90_STD_v1/IRB1200H_5_90_STD.urdf) | [USD](library/ABB/IRB1200H_5_90_STD_v1/IRB1200H_5_90_STD/IRB1200H_5_90_STD.usd) |
| ABB | IRB1200H_7_70_STD | Industrial Robot | [URDF](library/ABB/IRB1200H_7_70_STD_v1/IRB1200H_7_70_STD.urdf) | [USD](library/ABB/IRB1200H_7_70_STD_v1/IRB1200H_7_70_STD/IRB1200H_7_70_STD.usd) |
| ABB | IRB14000_Yumi | Dual-Arm Cobot | [URDF](library/ABB/IRB14000_Yumi_v1/IRB14000_Yumi.urdf) | [USD](library/ABB/IRB14000_Yumi_v1/IRB14000_Yumi/IRB14000_Yumi.usd) |
| ABB | IRB14050_SAYuMi | Cobot | [URDF](library/ABB/IRB14050_SAYuMi_v1/IRB14050_SAYuMi.urdf) | [USD](library/ABB/IRB14050_SAYuMi_v1/IRB14050_SAYuMi/IRB14050_SAYuMi.usd) |
| ABB | IRB1520ID_4_150 | Industrial Robot | [URDF](library/ABB/IRB1520ID_4_150_v1/IRB1520ID_4_150.urdf) | [USD](library/ABB/IRB1520ID_4_150_v1/IRB1520ID_4_150/IRB1520ID_4_150.usd) |
| ABB | IRB1600_X-120 | Industrial Robot | [URDF](library/ABB/IRB1600_X-120_v1/IRB1600_X-120.urdf) | [USD](library/ABB/IRB1600_X-120_v1/IRB1600_X-120/IRB1600_X-120.usd) |
| ABB | IRB52_7-1_2-Short | Paint Robot | [URDF](library/ABB/IRB52_7-1_2-Short_v1/IRB52_7-1_2-Short.urdf) | [USD](library/ABB/IRB52_7-1_2-Short_v1/IRB52_7-1_2-Short/IRB52_7-1_2-Short.usd) |
| ABB | IRB52_7-1_45-Long | Paint Robot | [URDF](library/ABB/IRB52_7-1_45-Long_v1/IRB52_7-1_45-Long.urdf) | [USD](library/ABB/IRB52_7-1_45-Long_v1/IRB52_7-1_45-Long/IRB52_7-1_45-Long.usd) |
| ABB | IRB5500-22 | Industrial Robot | [URDF](library/ABB/IRB5500-22_v1/IRB5500-22.urdf) | [USD](library/ABB/IRB5500-22_v1/IRB5500-22/IRB5500-22.usd) |
| ABB | IRB5500-27 | Industrial Robot | [URDF](library/ABB/IRB5500-27_v1/IRB5500-27.urdf) | [USD](library/ABB/IRB5500-27_v1/IRB5500-27/IRB5500-27.usd) |
| ABB | IRB5510-12 | Industrial Robot | [URDF](library/ABB/IRB5510-12_v1/IRB5510-12.urdf) | [USD](library/ABB/IRB5510-12_v1/IRB5510-12/IRB5510-12.usd) |
| ABB | IRB6750S_185-390-LID | Industrial Robot | [URDF](library/ABB/IRB6750S_185-390-LID_v1/IRB6750S_185-390-LID.urdf) | [USD](library/ABB/IRB6750S_185-390-LID_v1/IRB6750S_185-390-LID/IRB6750S_185-390-LID.usd) |
| ABB | IRB8700_550-420-SW6 | Industrial Robot | [URDF](library/ABB/IRB8700_550-420-SW6_v1/IRB8700_550-420-SW6.urdf) | [USD](library/ABB/IRB8700_550-420-SW6_v1/IRB8700_550-420-SW6/IRB8700_550-420-SW6.usd) |
| ABB | IRB8700_800_350 | Industrial Robot | [URDF](library/ABB/IRB8700_800_350_v1/IRB8700_800_350.urdf) | [USD](library/ABB/IRB8700_800_350_v1/IRB8700_800_350/IRB8700_800_350.usd) |
| ABB | IRB910INV-350 | SCARA Robot | [URDF](library/ABB/IRB910INV-350_v1/IRB910INV-350.urdf) | [USD](library/ABB/IRB910INV-350_v1/IRB910INV-350/IRB910INV-350.usd) |
| ABB | IRB910INV-550 | SCARA Robot | [URDF](library/ABB/IRB910INV-550_v1/IRB910INV-550.urdf) | [USD](library/ABB/IRB910INV-550_v1/IRB910INV-550/IRB910INV-550.usd) |
| ABB | IRB920_6kg_550_180_STD | SCARA Robot | [URDF](library/ABB/IRB920_6kg-550-180-STD_v1/IRB920_6kg_550_180_STD.urdf) | [USD](library/ABB/IRB920_6kg-550-180-STD_v1/IRB920_6kg_550_180_STD/IRB920_6kg_550_180_STD.usd) |
| ABB | IRB920_6kg_650_180_STD | SCARA Robot | [URDF](library/ABB/IRB920_6kg_650_180_STD_v1/IRB920_6kg_650_180_STD.urdf) | [USD](library/ABB/IRB920_6kg_650_180_STD_v1/IRB920_6kg_650_180_STD/IRB920_6kg_650_180_STD.usd) |
| ABB | IRB920T_6kg_450_180_STD | SCARA Robot | [URDF](library/ABB/IRB920T_6kg_450_180_STD_v1/IRB920T_6kg_450_180_STD.urdf) | [USD](library/ABB/IRB920T_6kg_450_180_STD_v1/IRB920T_6kg_450_180_STD/IRB920T_6kg_450_180_STD.usd) |
| ABB | IRB930_12kg_1050_300_STD | SCARA Robot | [URDF](library/ABB/IRB930_12kg_1050_300_STD_v1/IRB930_12kg_1050_300_STD.urdf) | [USD](library/ABB/IRB930_12kg_1050_300_STD_v1/IRB930_12kg_1050_300_STD/IRB930_12kg_1050_300_STD.usd) |
| ABB | Irbpa_250_D1000_IRC5_rev02_CAD | Positioner | [URDF](library/ABB/Irbpa_250_D1000_IRC5_rev02_CAD_v1/Irbpa_250_D1000_IRC5_rev02_CAD.urdf) | [USD](library/ABB/Irbpa_250_D1000_IRC5_rev02_CAD_v1/Irbpa_250_D1000_IRC5_rev02_CAD/Irbpa_250_D1000_IRC5_rev02_CAD.usd) |
| ABB | Irbpk_600_D1200_L1600_IRC5_rev02_CAD | Positioner | [URDF](library/ABB/Irbpk_600_D1200_L1600_IRC5_rev02_CAD_v1/Irbpk_600_D1200_L1600_IRC5_rev02_CAD.urdf) | [USD](library/ABB/Irbpk_600_D1200_L1600_IRC5_rev02_CAD_v1/Irbpk_600_D1200_L1600_IRC5_rev02_CAD/Irbpk_600_D1200_L1600_IRC5_rev02_CAD.usd) |
| ABB | Irbpr_1000_D1200_L2000_IRC5_rev02_CAD | Positioner | [URDF](library/ABB/Irbpr_1000_D1200_L2000_IRC5_rev02_CAD_v1/Irbpr_1000_D1200_L2000_IRC5_rev02_CAD.urdf) | [USD](library/ABB/Irbpr_1000_D1200_L2000_IRC5_rev02_CAD_v1/Irbpr_1000_D1200_L2000_IRC5_rev02_CAD/Irbpr_1000_D1200_L2000_IRC5_rev02_CAD.usd) |

**Total**: 30 ABB robot models available

## Demos

### Hello World

How to load a robot and instantiate a `SingleArticulation` to control it.

```bash
~/isaacsim/python.sh scripts/hello_world.py library/ABB/CRB15000_10kg_152_v1/CRB15000_10kg_152.urdf

```

### Interactive Inverse Kinematics

Drag a cube around the scene and watch a robot follow it.

![An animated GIF showing a screen recording of an IsaacSim scene where the user is draging a cube around space while an ABB1200 robot is following it.](docs/ik_animation.gif)


```bash
# install PyRoKi (provides Inverse Kinematics)
~/isaacsim/python.sh -m pip install git+https://github.com/chungmin99/pyroki

# cobot
~/isaacsim/python.sh scripts/ikdemo.py library/ABB/CRB15000_10kg_152_v1/CRB15000_10kg_152.urdf

# industrial robot
~/isaacsim/python.sh scripts/ikdemo.py library/ABB/IRB1200H_5_90_STD_v1/IRB1200H_5_90_STD.urdf
```


## Resources

* **ABB Robot Models Spreadsheet**: https://docs.google.com/spreadsheets/d/1CGoqaV-FV7UAYWtw-b55ihwH7Zm8Z7hNbWZzfseqUVU/edit?usp=sharing

* **IsaacSim Typings**: https://github.com/work-r-labs/isaacsim_typings

* **Official IsaacSim Installation And Guides**: https://docs.isaacsim.omniverse.nvidia.com/4.5.0/index.html

* **IsaacSim Installation Video (From Articulated Robotics)**: https://www.youtube.com/watch?v=SjVqOqEXXrY&t=68s

* **Official IsaacSim API Documentation**: https://docs.isaacsim.omniverse.nvidia.com/4.5.0/py/index.html

* **PyRoKi (Kinematics Toolkit)**: https://github.com/chungmin99/pyroki

## Contributing

### Validate All URDF files

```bash
uv venv
uv pip install -r requirements.txt
bash tools/validate_all_urdfs.sh
```

### Formatting

```
ruff format
```