from paraview.simple import *

import time

def load_data(data_path, show=False, interact=False):
    data = OpenFOAMReader(registrationName=data_path.split('/')[-1],
                          FileName=data_path)
    
    # get animation scene
    animationScene1 = GetAnimationScene()

    # update animation scene based on data timesteps
    animationScene1.UpdateAnimationUsingDataTimeSteps() 

    renderView1 = GetActiveViewOrCreate('RenderView')

    # show data in view
    start_time = time.time()
    runfoamDisplay = Show(data, renderView1, 'UnstructuredGridRepresentation')
    elapsed_time = time.time() - start_time

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
    renderView1.CameraPosition = [0.08451644302948183, -0.21068666041447617, -0.11248287853191463]
    renderView1.CameraFocalPoint = [0.06283199787139893, 0.009999999776482582, 0.02094399929046631]
    renderView1.CameraViewUp = [0.05780590149651594, -0.5123557263579088, 0.8568255875150057]
    renderView1.CameraParallelScale = 0.06698142323301427

    Interact()

    return data, elapsed_time

def cell_data_to_point_data(data, order, show=False):
    filter = CellDatatoPointData(data)
    
    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    return filter, elapsed_time

def glyph(data, order, show=True,
          scale_factor=0.002,
          glyph_type='Arrow',
          glyph_mode="Uniform Spatial Distribution (Bounds Based)"):
    filter = Glyph(data)
    filter.ScaleFactor = scale_factor
    filter.GlyphType = glyph_type
    filter.GlyphMode = glyph_mode
    
    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    return filter, elapsed_time

def contour(data, order, show=True,
            contour_by="cellind",
            isosurfaces=[2404717, 4809434, 7214150, 9618867,
                         12023583, 14428300, 16833016, 19237733]): # 10개 구간(양 끝 없어서 8개 윤곽)
    filter = Contour(data)
    filter.ContourBy = contour_by
    filter.Isosurfaces = isosurfaces
    
    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    return filter, elapsed_time

def stream_tracer(data, order, show=True,
                  vectors='vl',
                  seed_type='Line'):
    filter = StreamTracer(data)
    # filter.Vectors = vectors
    # filter.SeedType = seed_type

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    return filter, elapsed_time

def tube(data, order, show=True,
         vectors='vl',
         seed_type='Line'):
    filter = Tube(data)
    filter.Vectors = vectors
    filter.SeedType = seed_type

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    return filter, elapsed_time

def clip(data, order, show=True,
         clip_type='Plane'):
    filter = Clip(data)
    filter.ClipType = clip_type

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    return filter, elapsed_time

def slice(data, order, show=True,
          slice_type='Plane'):
    filter = Slice(data)
    filter.SliceType = slice_type

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    return filter, elapsed_time

def extract_selection(data, order, show=True):
    filter = ExtractSelection(data)

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    return filter, elapsed_time

def plot_selection_over_time(data, order, show=True):
    filter = PlotSelectionOverTime(data)

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    return filter, elapsed_time

def plot_over_line(data, order, show=True):
    filter = PlotOverLine(data)

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    return filter, elapsed_time

def tube(data, order, show=True):
    filter = Tube(data)

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    return filter, elapsed_time