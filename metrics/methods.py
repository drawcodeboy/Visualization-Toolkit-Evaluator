from paraview.simple import *
import time

def draw_glyph(input, render_view, config):
    # 1. Fill/Open 2. Apply

    times = {}

    Hide(input, render_view)

    # create a new 'Glyph'
    start_time = time.time()
    glyph1 = Glyph(registrationName='Glyph1', Input=input,
        GlyphType='Arrow')
    elapsed_time = time.time() - start_time
    times['Glyph Create Time'] = elapsed_time

    # show data in view
    start_time = time.time()
    glyph1Display = Show(glyph1, render_view, 'GeometryRepresentation')
    elapsed_time = time.time() - start_time
    times['Glyph Rendering Time'] = elapsed_time

    # trace defaults for the display properties.
    glyph1Display.Representation = 'Surface'

    return times

def draw_iso_contour(input, render_view, config):
    times = {}

    # hide data in view
    Hide(input, render_view)

    # create a new 'Contour'
    start_time = time.time()
    contour1 = Contour(registrationName='Contour1', Input=input)
    elapsed_time = time.time() - start_time
    times['ISO Contour Create Time'] = elapsed_time

    # Properties modified on contour1
    # contour1.ContourBy = ['POINTS', 'cellind']
    input.GetDataInformation()

    min_value, max_value = 0, 1.07281e+08 # 0, 17999 # 0, 1.77908e+07 # 0, 1.07281e+08
    diff = (max_value-min_value) / (config['segments']-1)
    contour1.Isosurfaces = [min_value + i * diff for i in range(0, config['segments'])]

    # show data in view
    start_time = time.time()
    contour1Display = Show(contour1, render_view, 'GeometryRepresentation')
    elapsed_time = time.time() - start_time
    times['ISO Contour Rendering Time'] = elapsed_time

    # trace defaults for the display properties.
    contour1Display.Representation = 'Surface'

    return times

def draw_stream_line(input, render_view, config):
    times = {}

    # create a new 'Stream Tracer'
    start_time = time.time()
    streamTracer1 = StreamTracer(registrationName='StreamTracer1', Input=input,
        SeedType='Point Cloud')
    elapsed_time = time.time() - start_time
    times['Stream Line Create Time'] = elapsed_time

    # show data in view
    start_time = time.time()
    streamTracer1Display = Show(streamTracer1, render_view, 'GeometryRepresentation')
    elapsed_time = time.time() - start_time
    times['Stream Line Rendering Time'] = elapsed_time

    # trace defaults for the display properties.
    streamTracer1Display.Representation = 'Surface'

    # hide data in view
    Hide(input, render_view)

    return times

def draw_clip(input, render_view, config):
    times = {}

    # create a new 'Clip'
    start_time = time.time()
    clip1 = Clip(registrationName='Clip1', Input=input)
    elapsed_time = time.time() - start_time
    times['Clip Create Time'] = elapsed_time

    # show data in view
    start_time = time.time()
    clip1Display = Show(clip1, render_view, 'UnstructuredGridRepresentation')
    elapsed_time = time.time() - start_time
    times['Clip Rendering Time'] = elapsed_time
    
    # trace defaults for the display properties.
    clip1Display.Representation = 'Surface'

    # hide data in view
    Hide(input, render_view)

    # update the view to ensure updated data information
    render_view.Update()

    return times

def draw_slice(input, render_view, config):
    times = {}

    # create a new 'Slice'
    start_time = time.time()
    slice1 = Slice(registrationName='Slice1', Input=input)
    elapsed_time = time.time() - start_time
    times['Slice Create Time'] = elapsed_time

    # get active view
    render_view = GetActiveViewOrCreate('RenderView')

    # show data in view
    start_time = time.time()
    slice1Display = Show(slice1, render_view, 'GeometryRepresentation')
    elapsed_time = time.time() - start_time
    times['Slice Create Time'] = elapsed_time

    # trace defaults for the display properties.
    slice1Display.Representation = 'Surface'

    # hide data in view
    Hide(input, render_view)

    # update the view to ensure updated data information
    render_view.Update()

    return times