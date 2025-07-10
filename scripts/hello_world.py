import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("urdf_path", type=Path)

args = parser.parse_args()

urdf_path: Path = args.urdf_path.resolve()
assert urdf_path.exists()
