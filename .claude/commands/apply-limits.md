An existing urdf file must be specified in $ARGUMENTS. If it is not, give the user approriate feedback and exit.

There must also be a file named `limits.xml` immediately adjacent to the urdf file. If there is not one, give the user appropriate feedback and exit.

Ensure the limits are applied to the urdf.

If any joints are continuous, and there are upper and lower limits specified, make them revolute.