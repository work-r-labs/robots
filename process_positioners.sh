#!/usr/bin/env bash

# Process all ABB positioners from sources/ABB/Positioners/ to library/
# This script excludes positioners already in the library

set -euo pipefail

echo "Processing ABB positioners..."

# Irbpa-500_D1000-H700_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpa-500_D1000-H700_IRC5_rev02_CAD_description/urdf/Irbpa-500_D1000-H700_IRC5_rev02_CAD.urdf"

# Irbpa-500_D1450-H900_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpa-500_D1450-H900_IRC5_rev02_CAD_description/urdf/Irbpa-500_D1450-H900_IRC5_rev02_CAD.urdf"

# Irbpa-750_D1000-H700_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpa-750_D1000-H700_IRC5_rev02_CAD_description/urdf/Irbpa-750_D1000-H700_IRC5_rev02_CAD.urdf"

# Irbpb-250_D1000_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpb-250_D1000_IRC5_rev02_CAD_description/urdf/Irbpb-250_D1000_IRC5_rev02_CAD.urdf"

# Irbpb-500_D1450_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpb-500_D1450_IRC5_rev02_CAD_description/urdf/Irbpb-500_D1450_IRC5_rev02_CAD.urdf"

# Irbpb-750_D1450_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpb-750_D1450_IRC5_rev02_CAD_description/urdf/Irbpb-750_D1450_IRC5_rev02_CAD.urdf"

# Irbpc-1000_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpc-1000_IRC5_rev02_CAD_description/urdf/Irbpc-1000_IRC5_rev02_CAD.urdf"

# Irbpc-500_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpc-500_IRC5_rev02_CAD_description/urdf/Irbpc-500_IRC5_rev02_CAD.urdf"

# Irbpd-600_D1000-L1600_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpd-600_D1000-L1600_IRC5_rev02_CAD_description/urdf/Irbpd-600_D1000-L1600_IRC5_rev02_CAD.urdf"

# Irbpd-600_D1200-L2000_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpd-600_D1200-L2000_IRC5_rev02_CAD_description/urdf/Irbpd-600_D1200-L2000_IRC5_rev02_CAD.urdf"

# Irbpk-1000_D1400-L4000_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpk-1000_D1400-L4000_IRC5_rev02_CAD_description/urdf/Irbpk-1000_D1400-L4000_IRC5_rev02_CAD.urdf"

# Irbpl-1000_L1250_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpl-1000_L1250_IRC5_rev02_CAD_description/urdf/Irbpl-1000_L1250_IRC5_rev02_CAD.urdf"

# Irbpl-5000_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpl-5000_IRC5_rev02_CAD_description/urdf/Irbpl-5000_IRC5_rev02_CAD.urdf"

# Irbpr-300_D1000-L1250_IRC5_rev02_CAD
bash tools/prepare-for-isaacsim.sh "sources/ABB/Positioners/Irbpr-300_D1000-L1250_IRC5_rev02_CAD_description/urdf/Irbpr-300_D1000-L1250_IRC5_rev02_CAD.urdf"

echo "All positioners processed successfully!"