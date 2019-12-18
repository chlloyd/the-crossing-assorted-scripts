# *The Crossing Project* Conventions
Documentation explaining the conventions like naming rules for *'The Crossing'* project. This is to ensure scripts run without error, files are not lost and time is wasted changing names and assets.

## Software and versions
These program versions need to be followed to safeguard us against render errors and file opening errors. They are as follows:
* Maya 2018
* Arnold for Maya 3.2.1
* Zbrush
* Unfold3d
* Houdini 17.0
* Arnold for Houdini 4.1.0
* Nuke X 11.1
* Adobe Premiere Pro
* Logic Pro X


---

## Assets
### Models
#### Naming
All models should have a clear name denoting the what the actual object is. The naming the assets is quite relaxed

#### File Types
All model assets must be either a Maya scene (.ma not .mb), Autodesk FBX (.fbx) or Arnold Scene Source file (.ass) file.

#### Topology
Clean topology is essential. The render must be able to render the object with **both the CPU and GPU Arnold renderers**. Making sure the GPU renders the scene makes other jobs further down the pipeline much easier.

It must not have any abnormalities when being rendered. E.g. Faces inside other face.

---

### Shaders
Only user shaders for Arnold. Not any other renders. This include not using Maya shaders.
#### Naming
All shader names must be named appropriately with it signify what it is. Each word must be separated by an underscore (_) and in lowercase. E.g. *house1_wall_shader*.

#### Reference Location
All images within a shader in the scene must have a working relative path. Relative paths being *sourceimages/assets/environment.ass* not containing drive letter and folders like *D:/The Crossing Group Project/assets/environment.ass*.

When rendering the project, the cloud render or another computer will not have the assets in the same locations. This will creates pink forces for the missing textures and possibly crash the render. Wasting money on the cloud renderer.

#### Shader Options
##### Colour Space
The correct colour space must be selected for each image. If it's a wide colour space image like 32 bit TIFF file, RAW colour space must be selected.

A table has been added to help with this.

Colour Space | File Extension | Supported by Arnold
:---: | :--- | :---
| | .ai 32bit |
| | .exr | ✓
| | .hdr | ✓
| | .hdri | ✓
| | .tiff 32 bit | ✓
| | .cin | ✓
RAW | .dpx | ✓
| | .iff 32 bit | ✓
| | .psd 32 bit | ✓ (only flattened)
| | .rla 32 bit | ✓
| | .sgi 32 bit | ✓
| | .tga 32 bit | ✓
| | | | |
| | .ai 8 and 16 bit |
| | .als |
| | .eps |
| | .gif |
| | .ico | ✓
| | .iff 8 and 16 bit | ✓
| | .jpg | ✓
sRGB | .png | ✓
| | .pnm | ✓
| | .psd 8-24 bit | ✓ (only flattened)
| | .rla 8-24 bit |✓
| | .sgi 8-24 bit | ✓
| | .tga 8-24 bit | ✓
| | .tiff 8-24 bit | ✓
| | .yuv |

From Allegorithmic's website for using textures created with substance painter.

Substance Texture | Colour Space | Arnold Standard Surface
----------------- | ------------ | -----------------------
Base Colour | sRGB | Base Colour
Roughness | RAW + alpha is luminance | Specular Roughness
Metallic | RAW + alpha is luminance | Metalness
Normal | RAW | Bump2D > Normal Camera
Opacity | RAW + alpha is luminance| Opacity
Height | RAW + alpha is luminance| displacementShader > Shading Group displacement Input


##### Alpha is luminance
Enable this for any image where only one colour channel is used. E.g. bump or roughness.

Use these guide for help:

* [Substance Painter Textures to Arnold](https://docs.substance3d.com/integrations/arnold-5-for-maya-157352171.html)
* [Substance Painter Export Help](https://docs.substance3d.com/spdoc/export-window-98959396.html)

#### This Animation Project

##### Textures

For this animation project we will be doing the following:

Substance Texture | Colour Space | Arnold Standard Surface
----------------- | ------------ | -----------------------
Base Colour | Utility - sRGB - Texture | Base Colour
Roughness | Utility - RAW + alpha is luminance | Diffuse Roughness
Metallic | Utility - RAW + alpha is luminance | Metalness
Normal | Utility - RAW | aiNormalMap.input - aiNormalMap.outValue > Normal Camera
Opacity | Utility - RAW + alpha is luminance| Opacity
Height | Utility - RAW + alpha is luminance| displacementShader > Shading Group displacement Input

##### Shaders
All shaders will have the following:
* specular roughness at 0.6
* normal weight at 0.1
* base at 1


---

### Textures
#### Naming
Naming must be an exact referral to the shader. It should be the **shader_name_render_pass.ext**. All in lowercase with underscore (_) separating each work.

#### File Formats
Use common easy to use file formats.

For Images use:
* .tiff
* .jpeg/jpg
* .png
* .exr
* .hdri


Render Exports
* .jpg for quite render checks. Not for final shots.
* .exr for final renders sequences.

Do not use the following:
* .psd (Adobe Photoshop files) - These don't work very well with Maya and Arnold.
* .pxr (Pixar Raster Images) - Very old file format. Maybe exclusive to Pixar Renderman. It's pretty much an 8 bit .png.
* .iff (Maya IFF raster Image) - Very much a maya specific file format. Only Adobe Photoshop can open it.

#### Export
Most images exports are going to be 2048 x 2048 pixel in 8-bit tiff unless greater detail is needed. Like for example for larger areas.
The project is only being export in 1080p (1920 x 1080). There isn't much need to go over 2k resolution textures. Greater sizes are a waste of file sizes (AWS, the platform we will be using for rendering charges for uploads and downloads) as well as increasing render times slightly.

#### Shader Networks and Nodes
When connecting all the images textures to the shader, remember the following:

* Connect the textures to the correct shader connector
* Use Arnold specific nodes rather than Maya nodes. There may be some imcompatabilities when exporting to .ass files.
* Change the color space on the file node to the correct color space. The tabe under Shader Options > Colour Space will help with this.

### Simulation Caches
#### Naming
Caching simulation names should be named *shot_####.####.ext*. shot_#### being the shot number and.#### being the frame number.


### Arnold Scene Source Files (.ass)
Before exporting .ass files, remember the following:

* Uncheck Absolute Texture Paths and Absolute Procedual Paths
* Set the Procedural Search Path and Texture Search Path.

#### Naming
A clear name given to them with underscores between words. For a sequence of .ass files, add *.####* before the extension with # being number padding.

#### Environment
.ass files are being used for efficient use of storage in the environment. Once these Arnold Scene Source files are exported, its unchangeable in Maya. They can be changed in text editor but with difficulty. Its much easier to make the changes within the maya scene file and export it once its been finalled.

---

## Rendering
### Naming
Image name must be follow this naming standard. Shot_*SHOTNUMBER.####.ext*. SHOTNUMBER being the rendered shots number, #### being frame number with 4 frame padding and ext being the file extension (.exr).

### Image Format
* .jpg for quite render checks. Not for final shots.
* .exr for final renders sequences.

### Arbitrary Output Variables (AOVs)
A script will be created to select the chosen AOVs for the scene. More may need to be added for additional content within the scene like FX.

The script wills save miss-renders where incorrect AOVs have been selected or to many create giant images.

For this project we will be using the following:
* Direct
* Indirect
* Z
* Emission
* Volume_Z - only us when volumes are being rendered

### Render Settings
The following render settings will be used for all renders:
* Image format: exr
* Compression: zip
* Tiled: off
* Merge AOVs: on
* Colour Space: Using Output Transform
* Frame/Animation: name.#.ext
* Frame Padding: 3 or 4 depending on the frame number size
* Start frame/end frame: to scene frame range
* Renderable camera: Make sure the render camera is renderable
* Image size: 1920x1080 (HD_1080)
* Pixel Aspect Ratio: 1.000

* Camera AA: 1
* Diffues: 2
* Specular: 2
* Transmission: 2
* SSS: 2
* Volume Indirect: 2
* Adaptive Sampling: Enable
* Max Camera: 4
* Adaptive Threshold: 0.015
* Clamping AA Samples: off
* Affect AOVs: off
* Indirect Clamping Value: off
* Lock Sampling Pattern: off
* Ray Depth Total: 8 of 12: depending of glass of volumes is in the scene
* Diffuse: 2
* Specular: 2
* Transmission: 2- Up if glass are in the scene
* Volume Indirect: 0 - Up if volumes of glass are in the scene
* Motion Blur Enable: on


### Rendering Colour Space
Within this project we will use the ACES (Academy Color Encoding System). Specifically ACES-ACES2065-1, rendering in ACEScg. This provides a wider color gamut than sRGB or REC709. ACES will allow for greater detail within the highlights and shadows of the renders and more flexibility within compositing. The image below show the aces colour space compared with sRGB.

![Image of ACES colour space compared with rRGB](https://acescentral.com/uploads/default/original/1X/6c9849deef6788279c062bed799195057fd8fba1.png)

* [Maya Getting Started with Color Management](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2018/ENU/Maya-Rendering/files/GUID-B260195C-A0FE-4F51-9EA2-099B61B7725A-htm.html)
* [Maya Color Space Management Help](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2018/ENU/Maya-Rendering/files/GUID-5CDEBBB6-18F7-4062-B2AF-BDFDF11501F1-htm.html)
* [Arnold ACES Colour Space Tutorial](https://docs.arnoldrenderer.com/display/A5AFMUG/ACES+Workflow)

### Cloud Rendering
We will be using AWS (Amazon Web Services) with a self made custom render queue system. This will be created by the pipeline TD to render the project. If theses a problem with this them Google Zync is a backup which is a pre-made render queue system.

**All images will be exported at 1080p (1920x1080). No more, no less.**

---

## Files Management

### OneDrive
#### Pre-Production Files
Pre-Production files with correct naming and following the project template.

#### Production Files
##### Assets
All models with textures any other assets needed to complete the group project in a single project folder with sub-folders to organise:
* 3d models
* lighting properties files

##### Final Environment

Within this project folder the following should be used:


###### assets
All assets needed to complete the project. This can be:
* 3d models - with correct relative file paths
* lighting properties files

Please note this excludes texture file. These go into the source images folder.

All images textures should have a correct relative file path before being in the folder

###### cache
Houdini and nCloth caches go here. These file can be quite large. There is no need to upload these to OneDrive.


###### images
Where rendered images go. After the render. These will be moved into the post production folder afterwards to start composting.


###### renderData


###### scenes
Where the environment.ass file is and shot_####.ass file with the character animations.

###### sourceimages
All textures for the environment and currently rendering  shot

##### Post-Production Files
All Premiere Pro Files, rushes and dailies.

#### Folder Structure
This what the folder structure should be for the group project folder.
```.
.
├───Pre-Production
│   ├───
│   ├───
│   └───
├───Production
│   ├───assets
│   │   ├───characters
│   │   ├───environment
│   │   └───vehicles
│   ├───final environment
│   │   ├───assets
│   │   │   ├───characters
│   │   │   │   └───sourceimages
│   │   │   ├───environment
│   │   │   │   └───sourceimages
│   │   │   └───vehicles
│   │   │       └───sourceimages
│   │   ├───cachesgi
│   │   ├───images
│   │   │   └───shot_####.exr
│   │   ├───renderData
│   │   ├───sceneAssembly
│   │   ├───scenes
│   │   │   ├───environment.ass
│   │   │   └───shot_###
│   │   │       └───shot_1.####.ass
│   │   ├───sourceimages
│   │   │   ├───characters
│   │   │   ├───environment
│   │   │   └───vehicles
│   │   └───workspace.mel
│   ├───fx
│   ├───r and d
│   └───renderers
└── Post Production
```

#### Location

### GitHub

A collection of scripts will be upload here using git.

A private repo of the entire project will continuly uploaded to github with git-lfs.

---

### Post-Production
Post-production will consist of composting, sound mixing and the final edit.

#### Composting
We will be comping the render with the following:
* AOV colour correction
* Depth of field
* Film Noise
* Distance desaturation
* Roto - only when the shot needs it

A nuke script will be created to speed up the process.

#### Sound Mixing

#### Editing

---

### Helpful links

* [Substance Painter Textures to Arnold](https://docs.substance3d.com/integrations/arnold-5-for-maya-157352171.html)
* [Substance Painter Export Help](https://docs.substance3d.com/spdoc/export-window-98959396.html)
* [Import Arnold Scene Sources to Houdini](https://answers.arnoldrenderer.com/questions/2635/how-to-import-ass-file-in-houdini.html)
* [Using Git for Version Control](https://help.github.com/en/articles/adding-an-existing-project-to-github-using-the-command-line)
* [Using Arnold's Kick Standalone Renderer](https://docs.arnoldrenderer.com/display/A5AFMUG/Getting+Started+With+Kick)
