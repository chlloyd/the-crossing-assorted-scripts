import maya.cmds as cmds

try:
    cmds.delete("file1")  # Delete the file node used for a HDRI map for test renders

except ValueError:
    pass

filenodes = cmds.ls(type="file")  # select all file nodes

for filenode in filenodes:

    filenodepath = cmds.getAttr(filenode + ".fileTextureName")
    # try statement used as some file paths used "/" and some used "\"
    try:
        newfilepath = "sourceimages/Houses/" + filenodepath.split("/")[-2] + "/" + filenodepath.split("/")[-1]
        print(newfilepath)
        cmds.setAttr(filenode + ".fileTextureName", newfilepath, type="string")

    except IndexError:
        newfilepath = "sourceimages/Houses/" + filenodepath.split("\\")[-2] + "/" + filenodepath.split("\\")[-1]
        print(newfilepath)
        cmds.setAttr(filenode + ".fileTextureName", newfilepath, type="string")

    imagepass = cmds.getAttr(filenode + ".fileTextureName").split("_")[-1].split(".")[0]
    # changing some parameters for file nodes depending on which image map they are
    if imagepass == "Normal":
        cmds.setAttr(filenode + ".colorSpace", "Raw", type="string")

    elif imagepass == "Roughness":
        cmds.setAttr(filenode + ".colorSpace", "Raw", type="string")
        cmds.setAttr(filenode + ".alphaIsLuminance", True)
