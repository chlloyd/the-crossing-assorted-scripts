import maya.cmds as cmds


"""0 = Bounding Box, 
   1 = Per Object Bounding Box, 
   2 = Polywire, 
   3 = Wireframe, 
   4 = Point Cloud, 
   5 = Shaded Polywire, 
   6 = Shaded"""

def set_stand_in_mode(mode):
    all_stand_ins = cmds.ls(type="aiStandIn")
    for stand_in in all_stand_ins:
        cmds.setAttr(stand_in + ".mode", mode)
         
set_stand_in_mode(6)
