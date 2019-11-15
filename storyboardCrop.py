from PIL import Image
import os

"""imagecrop = [337, 406, 1103, 873], [1251, 405, 2014, 875], [2122, 407, 2886, 878], [338, 1245, 1103, 1710], [1250, 1242,
            2013, 1711], [2121, 1242, 2884, 1716]

imagecrop = [349, 421, 1193, 935], [1365, 425, 2207, 939], [2337, 423, 3177, 937], [353, 1353, 1195, 1867], [1367, 1355,
            2209, 1873], [2335, 1357, 3181, 1875]"""

imagecrop = [229, 485, 1109, 1027], [1284, 487, 2162, 1030], [2295, 492, 3173, 1033], [230, 1462, 1109, 2003], [1283, 1465,
            2162, 2007], [2294, 1467, 3176, 2008]

path = os.path.dirname(__file__)
storyboard_path = path + "/storyboards"
storyboards = os.listdir(storyboard_path)

counter = 145
for storyboard in storyboards:
    img = Image.open(storyboard_path + "/" + storyboard)
    print(storyboard_path + "/" + storyboard)
    for i in range(1, 7):
        crop = img.crop(imagecrop[i-1])
        crop.save(path+"/out/storyboard_" + str(counter)+".jpg")
        print(path+"/out/storyboard_" + str(counter)+".jpg")
        counter += 1
