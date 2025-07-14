An existing xacro or urdf file must be specified in $ARGUMENTS. If it is not, give the user approriate feedback and exit.

The overarching goal is to produce a final urdf file and meshes folder from a the input xacro/urdf file which is appropriate to load into IsaacSim.

When working with xacro and urdf files, do not use external tools. Rely on your own knowledege of the formats to do the work.

The final output folder should be placed into a folder called `generated` in the project root directory with the following structure

root -> library -> brand -> my_robot_vX -> my_robot.urdf & meshes/

Where vX is a version number chosen depending on how many other versions of that same robot are already there. Start at v1.

Complete the following steps:
1. if a xacro file is specified: expand the xacro file
2. in the new file, sanitise the names of links, joints, meshes etc such that all names contain only numbers, letters and underscores. When copying meshes into the generated output folder, you will need to rename them if you have sanitised their names.
3. in the new file, remove all uses of materials
4. in the new file, remove the ros specific path system, have all mesh paths start at `meshes/`.

Remember that when moving mesh files, you MUST rename them to match the sanitized name in the URDF. Mesh names with dashes are never ok.