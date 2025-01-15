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

# create a new 'Contour'
contour1 = Contour(registrationName='Contour1', Input=runfoam)

# set active source
SetActiveSource(runfoam)

# set active source
SetActiveSource(contour1)

# Properties modified on contour1
contour1.ContourBy = ['POINTS', 'cellind']
contour1.Isosurfaces = [0.10130000114440918, 1.0, 2404717.5555555555, 4809434.111111111, 7214150.666666666, 9618867.222222222, 12023583.777777778, 14428300.333333332, 16833016.888888888, 19237733.444444444, 21642450.0]

# show data in view
contour1Display = Show(contour1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
contour1Display.Representation = 'Surface'

# hide data in view
Hide(runfoam, renderView1)

# show color bar/color legend
contour1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# get color transfer function/color map for 'cellind'
cellindLUT = GetColorTransferFunction('cellind')

# get opacity transfer function/opacity map for 'cellind'
cellindPWF = GetOpacityTransferFunction('cellind')

# get 2D transfer function for 'cellind'
cellindTF2D = GetTransferFunction2D('cellind')

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

Interact()