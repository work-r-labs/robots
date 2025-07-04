#!/usr/bin/env bash
set -euo pipefail

# find each URDF and process it sequentially
find . -type f -name '*.urdf' -print0 | while IFS= read -r -d '' urdf; do
  echo "Preparing $urdf"
  claude -p "/prepare-for-isaacsim $urdf"
done
