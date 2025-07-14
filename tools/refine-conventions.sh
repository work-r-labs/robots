#!/usr/bin/env bash

set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $(basename "$0") <URDF file>"
  exit 1
fi

URDF_PATH="$1"

claude -p "/refine-conventions $URDF_PATH" \
       --print \
       --output-format stream-json \
       --verbose \
       --dangerously-skip-permissions \
       | jq
