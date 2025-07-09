An existing urdf file must be specified in $ARGUMENTS. If it is not, give the user approriate feedback and exit.

Edit the urdf file so that the joint names and link names follow ros-industrial conventions.

If editing mesh paths, make sure to rename the corresponding meshes in the file system too.

base_link, flange and tool0 are required.

Always run `uv run tools/validate_urdf.py URDF_PATH` to make sure your changes are correct.