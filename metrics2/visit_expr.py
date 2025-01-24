from visit import *

import time

def visit_load_data():
    AddPlot('Mesh', 'Mesh')
    start_time = time.time()
    DrawPlots()
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time:.4f}s")

    v = GetView3D()
    # v.imageZoom=-0.5
    v.RotateAxis(0, 20.0)
    v.RotateAxis(1, 45.0)
    v.RotateAxis(2, 20.0)
    SetView3D(v)

def visit_vector_field(data_path):
    AddPlot('Vector', 'DISPL')
    p = VectorAttributes()
    p.glyphLocation=1
    p.nVectors=5000
    p.autoScale=0
    p.scale= 1 if data_path == "D:/Data/ParaView/Grid20_30_30T.ex2" else 5
    p.lineStem=0
    SetPlotOptions(p)
    start_time = time.time()
    DrawPlots()
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time:.4f}s")

    v = GetView3D()
    v.imageZoom=-0.5
    v.RotateAxis(1, 180.0)
    v.RotateAxis(2, 180.0)
    SetView3D(v)

def visit_iso_contour():
    AddPlot('Contour', 'coordx')
    p = ContourAttributes()
    p.contourNLevels = 8
    SetPlotOptions(p)

    start_time = time.time()
    DrawPlots()
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time:.4f}s")

    v = GetView3D()
    # v.imageZoom=-0.5
    v.RotateAxis(0, 20.0)
    v.RotateAxis(1, 45.0)
    v.RotateAxis(2, 20.0)
    SetView3D(v)

def visit_stream_line():
    raise NotImplementedError('Stream Line is Not Supported in VisIT')

x_half = {
    'Grid20_30_30T.ex2': [1.5, -15.5],
    'Grid200_300_300T.ex2': [15., 0],
    'Grid300_600_600T.ex2': [30., 30.]
}

def visit_clip(data_path):
    AddPlot('Mesh', 'Mesh')
    # DrawPlots()

    AddOperator('Clip')
    c = ClipAttributes()
    c.plane1Origin = (x_half[data_path.split('/')[-1]][0], 0, 0)
    SetOperatorOptions(c)

    start_time = time.time()
    DrawPlots()
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time:.4f}s")

    v = GetView3D()
    # v.imageZoom=-0.5
    v.RotateAxis(0, 20.0)
    v.RotateAxis(1, 45.0)
    v.RotateAxis(2, 20.0)
    SetView3D(v)

def visit_slice(data_path):
    AddPlot('Mesh', 'Mesh')
    DrawPlots()

    AddOperator('Slice')
    s = SliceAttributes()
    s.project2d = 0
    s.originType = 0
    s.originPoint = (0, x_half[data_path.split('/')[-1]][1], 0)
    SetOperatorOptions(s)

    start_time = time.time()
    DrawPlots()
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time:.4f}s")

    v = GetView3D()
    # v.imageZoom=-0.5
    v.RotateAxis(0, 20.0)
    v.RotateAxis(1, 45.0)
    v.RotateAxis(2, 20.0)
    SetView3D(v)