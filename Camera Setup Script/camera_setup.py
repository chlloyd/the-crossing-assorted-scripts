import maya.cmds as cmds
import json
import os

height, width = 200, 200

with open(os.path.dirname(os.path.realpath(__file__)) + "/camera_data.json", "r") as camera_data:
    camera_json = json.load(camera_data)


class MayaCameraSetup:
    def __init__(self):
        self.window = "Create Camera"
        self.title = "Arri Alexa Camera Select"
        self.size = (height, width)

    def buildUI(self):
        if cmds.window(self.window, exists=True):
            self.close()
        self.window = cmds.window(self.window, title=self.title, widthHeight=self.size)
        self.mainForm = cmds.formLayout(numberOfDivisions=100)
        cmds.rowColumnLayout(width=width)
        self.camera_option = cmds.optionMenu(label="Camera")
        for camera_menu_item in self.list_all_cameras():
            cmds.menuItem(label=camera_menu_item)
        cmds.rowColumnLayout(nc=2, cw=[(1, width / 2), (2, width / 2)])
        cmds.button(label="Apply", command=self.apply_btn)
        cmds.button(label="Cancel", command=self.close)
        cmds.rowColumnLayout(width=width)
        cmds.showWindow()

    def apply_btn(self, *args):
        if return_selected_camera() is None:  # if a camera isn't selected
            pass
        name = cmds.optionMenu(self.camera_option, query=True, value=True)
        print self.get_camera_data(name)
        #self.create_camera(name, camera_height, camera_width)
        #print name, camera_height, camera_width
        # set film back of selected camera
        pass

    def close(self, *args):
        cmds.deleteUI(self.window, window=True)

    def set_camera_film_back(self, film_width, film_height):
        camera = self.return_selected_camera()
        cmds.setAttr(camera+".")

    def create_camera(self, camera_name, camera_height, camera_width):
        self.camera = cmds.camera(name=camera_name, horizontalFilmAperture=camera_width, verticalFilmAperture=camera_height)

    def list_all_cameras(self):
        camera_list = []
        for camera in camera_json["cameras"]:
            camera_list.append(camera["name"])
        return camera_list

    def get_camera_data(self, camera_name):
        for camera in camera_json["cameras"]:
            if camera["name"] == camera_name:
                return camera["name"], camera["units"], camera["sensor_width"], camera["sensor_height"]

    def return_selected_camera(self):
        return cmds.ls(selection=True, type="camera")


cameraSetup = MayaCameraSetup()
cameraSetup.buildUI()
