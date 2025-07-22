import subprocess
from pathlib import Path
import sys

def main():
    library = Path(__file__).parent.parent / "library"
    assert library.is_dir()
    print(library)
    for urdf in library.rglob("*.urdf"):
        output = urdf.parent / "thumbnail.png"
        rrd_path = f"{urdf.parent}/{urdf.stem}.rrd"
        subprocess.call(f"{sys.executable} tools/urdfview.py {urdf} --mode save && rerun {rrd_path} --screenshot-to {output} --window-size 256x256", shell=True)
        print(urdf)
        # break

if __name__ == '__main__':
    main()