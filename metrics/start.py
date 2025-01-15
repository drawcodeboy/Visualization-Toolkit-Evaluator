from paraview.simple import *

def start(data_path):
    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    # create a new 'Open FOAM Reader'
    runfoam = OpenFOAMReader(registrationName=data_path.split('/')[-1], 
                             FileName=data_path)

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