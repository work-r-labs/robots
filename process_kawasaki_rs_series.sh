#!/usr/bin/env bash

set -euo pipefail

# Array of all Kawasaki RS Series URDF files
RS_SERIES_URDFS=(
    "sources/Kawasaki/RS Series/RS003N-A001_description/urdf/RS003N-A001.urdf"
    "sources/Kawasaki/RS Series/RS005L-A001_description/urdf/RS005L-A001.urdf"
    "sources/Kawasaki/RS Series/RS005N-A001_description/urdf/RS005N-A001.urdf"
    "sources/Kawasaki/RS Series/RS006L-A001_description/urdf/RS006L-A001.urdf"
    "sources/Kawasaki/RS Series/RS007L-BC01_description/urdf/RS007L-BC01.urdf"
    "sources/Kawasaki/RS Series/RS007N-BC01_description/urdf/RS007N-BC01.urdf"
    "sources/Kawasaki/RS Series/RS013N-AC01_description/urdf/RS013N-AC01.urdf"
    "sources/Kawasaki/RS Series/RS015X-B001_description/urdf/RS015X-B001.urdf"
    "sources/Kawasaki/RS Series/RS020N-A001_description/urdf/RS020N-A001.urdf"
    "sources/Kawasaki/RS Series/RS025N-AC01_description/urdf/RS025N-AC01.urdf"
    "sources/Kawasaki/RS Series/RS030N-B001_description/urdf/RS030N-B001.urdf"
    "sources/Kawasaki/RS Series/RS050N-B001_description/urdf/RS050N-B001.urdf"
    "sources/Kawasaki/RS Series/RS080N-B001_description/urdf/RS080N-B001.urdf"
)

echo "Processing ${#RS_SERIES_URDFS[@]} Kawasaki RS Series robots..."
echo ""

# Process each URDF file
for urdf in "${RS_SERIES_URDFS[@]}"; do
    echo "Processing: $urdf"
    bash tools/prepare-for-isaacsim.sh "$urdf"
    echo "---"
    echo ""
done

echo "All Kawasaki RS Series robots processed!"