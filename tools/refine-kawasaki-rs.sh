#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REFINE_SCRIPT="$SCRIPT_DIR/refine-conventions.sh"
KAWASAKI_DIR="$SCRIPT_DIR/../library/Kawasaki"

if [ ! -f "$REFINE_SCRIPT" ]; then
    echo "Error: refine-conventions.sh not found at $REFINE_SCRIPT"
    exit 1
fi

if [ ! -d "$KAWASAKI_DIR" ]; then
    echo "Error: Kawasaki directory not found at $KAWASAKI_DIR"
    exit 1
fi

echo "Applying refine-conventions.sh to all Kawasaki RS series robots..."

# List of RS series robots with their URDF files
RS_ROBOTS=(
    # "RS003N_A001_v2/RS003N_A001.urdf"
    # "RS005L_A001_v2/RS005L_A001.urdf"
    # "RS005N_A001_v2/RS005N_A001.urdf"
    # "RS006L_A001_v2/RS006L_A001.urdf"
    "RS007L_BC01_v1/RS007L_BC01.urdf"
    "RS007N_BC01_v1/RS007N_BC01.urdf"
    "RS013N_AC01_v1/RS013N_AC01.urdf"
    "RS015X_B001_v1/RS015X_B001.urdf"
    "RS020N_A001_v1/RS020N_A001.urdf"
    "RS025N_AC01_v1/RS025N_AC01.urdf"
    "RS030N_B001_v1/RS030N_B001.urdf"
    "RS050N_B001_v1/RS050N_B001.urdf"
    "RS080N_B001_v1/RS080N_B001.urdf"
)

for robot in "${RS_ROBOTS[@]}"; do
    urdf_path="$KAWASAKI_DIR/$robot"
    
    if [ -f "$urdf_path" ]; then
        echo "Processing: $robot"
        "$REFINE_SCRIPT" "$urdf_path"
        echo "Completed: $robot"
        echo "---"
    else
        echo "Warning: URDF file not found: $urdf_path"
    fi
done

echo "All Kawasaki RS series robots processed!"