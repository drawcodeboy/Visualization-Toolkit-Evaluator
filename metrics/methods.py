from paraview.simple import *

import time

def load_data(data_path, order, show=False):
    '''
        https://www.paraview.org/paraview-docs/latest/python/paraview.simple.OpenFOAMReader.html?highlight=openfoamreader#paraview.simple.OpenFOAMReader
    '''
    data = OpenDataFile(data_path)

    start_time = time.time()
    if show == True:
        Show(data) # include Render()
    else:
        Hide(data)
    elapsed_time = time.time() - start_time

    print(f"func({order:02d}) [Load]: {elapsed_time:.4f}s")

    return data, elapsed_time

def cell_data_to_point_data(data, order, show=False):
    '''
        https://www.paraview.org/paraview-docs/latest/python/paraview.simple.CellDatatoPointData.html?highlight=celldata
    '''
    filter = CellDatatoPointData(data)
    
    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    print(f"func({order:02d}) [Cell Data to Point Data]: {elapsed_time:.4f}s")

    return filter, elapsed_time

def glyph(data, order, show=True,
          scale_factor=0.002,
          glyph_type='Arrow',
          glyph_mode="Uniform Spatial Distribution (Bounds Based)"):
    '''
        https://www.paraview.org/paraview-docs/latest/python/paraview.simple.Glyph.html?highlight=glyph
    '''
    filter = Glyph(data)
    filter.ScaleFactor = scale_factor
    filter.GlyphType = glyph_type
    filter.GlyphMode = glyph_mode
    
    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    print(f"func({order:02d}) [Glyph]: {elapsed_time:.4f}s")

    return filter, elapsed_time

def contour(data, order, show=True,
            contour_by="cellind",
            isosurfaces=[2404717, 4809434, 7214150, 9618867,
                         12023583, 14428300, 16833016, 19237733]): # 10개 구간(양 끝 없어서 8개 윤곽)
    '''
        https://www.paraview.org/paraview-docs/latest/python/paraview.simple.Contour.html?highlight=contour
    '''
    filter = Contour(data)
    filter.ContourBy = contour_by
    filter.Isosurfaces = isosurfaces
    
    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    print(f"func({order:02d}) [Contour]: {elapsed_time:.4f}s")

    return filter, elapsed_time

def stream_tracer(data, order, show=True,
                  vectors='vl',
                  seed_type='Line'):
    """
        https://www.paraview.org/paraview-docs/latest/python/paraview.simple.StreamTracer.html?highlight=streamtracer
    """
    filter = StreamTracer(data)
    # filter.Vectors = vectors
    # filter.SeedType = seed_type

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    print(f"func({order:02d}) [Stream Tracer]: {elapsed_time:.4f}s")

    return filter, elapsed_time

def tube(data, order, show=True,
         vectors='vl',
         seed_type='Line'):
    """
        https://www.paraview.org/paraview-docs/latest/python/paraview.simple.StreamTracer.html?highlight=streamtracer
    """
    filter = Tube(data)
    filter.Vectors = vectors
    filter.SeedType = seed_type

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    print(f"func({order:02d}) [Tube]: {elapsed_time:.4f}s")

    return filter, elapsed_time

def clip(data, order, show=True,
         clip_type='Plane'):
    filter = Clip(data)
    filter.ClipType = clip_type

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    print(f"func({order:02d}) [Clip]: {elapsed_time:.4f}s")

    return filter, elapsed_time

def slice(data, order, show=True,
          slice_type='Plane'):
    filter = Slice(data)
    filter.SliceType = slice_type

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    print(f"func({order:02d}) [Slice]: {elapsed_time:.4f}s")

    return filter, elapsed_time

def extract_selection(data, order, show=True):
    filter = ExtractSelection(data)

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    print(f"func({order:02d}) [Extract Selection]: {elapsed_time:.4f}s")

    return filter, elapsed_time

def plot_selection_over_time(data, order, show=True):
    filter = PlotSelectionOverTime(data)

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    print(f"func({order:02d}) [Plot Selection Over Time]: {elapsed_time:.4f}s")

    return filter, elapsed_time

def plot_over_line(data, order, show=True):
    filter = PlotOverLine(data)

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    print(f"func({order:02d}) [Plot Over Line]: {elapsed_time:.4f}s")

    return filter, elapsed_time

def tube(data, order, show=True):
    filter = Tube(data)

    start_time = time.time()
    if show == True:
        Show(filter) # include Render()
    elapsed_time = time.time() - start_time

    print(f"func({order:02d}) [Tube]: {elapsed_time:.4f}s")

    return filter, elapsed_time