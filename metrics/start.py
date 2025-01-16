from paraview.simple import *

import time

def print_data_information(input):
    UpdatePipeline() # Need to update

    data_info = input.GetDataInformation()
    print(f"[Data info]")
    # print(data_info.DataInformation) # No Memory information
    print(f"\tDataset Type: {data_info.GetDataSetTypeAsString()}")
    print(f"\t# of Cells: {data_info.GetNumberOfCells()}")
    print(f"\t# of Points: {data_info.GetNumberOfPoints()}")
    print(f"\t# of Time Steps: {data_info.GetNumberOfTimeSteps()}")
    print(f"================================")

def start(data_path):
    '''
        [Docs]
            Initial setting, when use pvpython
        [Scenario]
            1. File>Open, Open Data
            2. click Apply Button
    '''
    times = {}

    #### disable automatic camera reset on 'Show'
    paraview.simple._DisableFirstRenderCameraReset()

    input = None

    if data_path.split('/')[-1].endswith('foam'):
        # create a new 'Open FOAM Reader'
        input = OpenFOAMReader(registrationName=data_path.split('/')[-1], 
                                FileName=data_path)
    elif data_path.split('/')[-1].endswith('ex2'):
        # create a new 'IOSS Reader'
        input = IOSSReader(registrationName=data_path.split('/')[-1], 
                        FileName=data_path)

    # Print data information
    print_data_information(input)

    # get animation scene
    animationScene1 = GetAnimationScene()

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps()

    # animationScene1.Play() # in Python, it doesn't work

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    start_time = time.time()
    inputDisplay = Show(input, renderView1, 'UnstructuredGridRepresentation')
    elapsed_time = time.time() - start_time
    times['Data Rendering Time'] = elapsed_time

    # trace defaults for the display properties.
    inputDisplay.Representation = 'Surface'

    # reset view to fit data
    renderView1.ResetCamera(False, 0.9)

    # get the material library
    materialLibrary1 = GetMaterialLibrary()

    # show color bar/color legend
    # when data expension is .ex2, Can't visualize since below function
    # inputDisplay.SetScalarBarVisibility(renderView1, True)

    # update the view to ensure updated data information
    renderView1.Update()

    '''
    # Not used below any visualization code

    # get color transfer function/color map for 'p'
    pLUT = GetColorTransferFunction('p')

    # get opacity transfer function/opacity map for 'p'
    pPWF = GetOpacityTransferFunction('p')

    # get 2D transfer function for 'p'
    pTF2D = GetTransferFunction2D('p')
    '''

    return input, renderView1, times