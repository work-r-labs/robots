import time
from pathlib import Path
import argparse
import rerun as rr
import rerun.blueprint as rrb

bp = rrb.Blueprint(
    rrb.BlueprintPanel(state="hidden"),
    rrb.SelectionPanel(state="hidden"),
    rrb.TimePanel(state="hidden"),
    rrb.TopPanel(state="hidden"),
)


def main(urdf_path: Path, mode: str = "spawn"):
    rr.init(str(int(time.time())), default_blueprint=bp)

    if mode == "spawn":
        rr.spawn(default_blueprint=bp)
    elif mode == "save":
        rr.save(f"{urdf_path.parent}/{urdf_path.stem}.rrd", default_blueprint=bp)

    rr.log_file_from_path(urdf_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="URDF Viewer")
    parser.add_argument("urdf_path", type=Path)
    parser.add_argument(
        "--mode",
        choices=["spawn", "save"],
        default="spawn",
        help="Mode: 'spawn' to view interactively, 'save' to save .rrd file",
    )
    args = parser.parse_args()

    urdf_path: Path = args.urdf_path
    if not urdf_path.exists():
        print(f"{urdf_path=} does not exist")
    else:
        main(urdf_path, args.mode)
