# trace generated using paraview version 5.13.1
#import paraview
#paraview.compatibility.major = 5
#paraview.compatibility.minor = 13

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Open FOAM Reader'
runfoam = OpenFOAMReader(registrationName='run.foam', FileName='C:\\Users\\User\\Desktop\\Interships\\KDW\\ETRI_04\\data\\241003\\foam\\foam\\run.foam')

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')

# show data in view
runfoamDisplay = Show(runfoam, renderView1, 'UnstructuredGridRepresentation')

# trace defaults for the display properties.
runfoamDisplay.Representation = 'Surface'

# reset view to fit data
renderView1.ResetCamera(False, 0.9)

# get the material library
materialLibrary1 = GetMaterialLibrary()

# show color bar/color legend
runfoamDisplay.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=runfoam)

# show data in view
import time
start_time = time.time()
clip1Display = Show(clip1, renderView1, 'UnstructuredGridRepresentation')
elapsed_time = time.time() - start_time

# trace defaults for the display properties.
clip1Display.Representation = 'Surface'

# hide data in view
Hide(runfoam, renderView1)

# show color bar/color legend
clip1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

#================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
#================================================================

# get layout
layout1 = GetLayout()

#--------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1816, 869)

#-----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [-0.1580763258305807, 0.1234090098960997, 0.09383746824586832]
renderView1.CameraFocalPoint = [0.06283199787139893, 0.009999999776482582, 0.02094399929046631]
renderView1.CameraViewUp = [0.4114167603626751, 0.8987686921533219, -0.15149616265004376]
renderView1.CameraParallelScale = 0.06698142323301427


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------
print(f"elapsed time: {elapsed_time:.4f}s")
Interact()