#!/bin/bash

# Script to process unprocessed ABB robot models
# Run each command to process the remaining robots

echo "Processing unprocessed ABB robot models..."

# Positioner Robots (Not Processed)
bash process.sh ABB/Positioners/Irbpa-250_D1000_IRC5_rev02_CAD_description/urdf/Irbpa-250_D1000_IRC5_rev02_CAD.xacro
bash process.sh ABB/Positioners/Irbpk-600_D1200-L1600_IRC5_rev02_CAD_description/urdf/Irbpk-600_D1200-L1600_IRC5_rev02_CAD.xacro
bash process.sh ABB/Positioners/Irbpr-1000_D1200-L2000_IRC5_rev02_CAD_description/urdf/Irbpr-1000_D1200-L2000_IRC5_rev02_CAD.xacro

echo "Processing completed for all remaining robots."