#!/bin/bash

# Script to process all unprocessed ABB robot models
# Run each command individually to process the robots that don't have USD files yet

echo "Processing 5 remaining unprocessed robots..."
echo "Run each command individually:"
echo

bash process.sh ABB/IRB14000_Yumi/IRB14000_rev01_description/urdf/IRB14000_rev01.xacro
bash process.sh ABB/IRB14050_SAYuMi/IRB14050_SAYuMi_-_rev00_description/urdf/IRB14050_SAYuMi_-_rev00.xacro
bash process.sh ABB/IRB910INV-350/IRB_description/urdf/IRB.xacro
bash process.sh ABB/IRB910INV-550/IRB_description/urdf/IRB.xacro
bash process.sh ABB/IRB920_6kg-650-180-STD/IRB920_6kg-650-180-STD_OmniCore_rev00_Assembly_description/urdf/IRB920_6kg-650-180-STD_OmniCore_rev00_Assembly.xacro

echo
echo "After processing all robots above, the repository will have 30 fully processed robots."