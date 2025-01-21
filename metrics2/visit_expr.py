from visit import *

import time

def visit_load_data():
    AddPlot('Mesh', 'Mesh')
    start_time = time.time()
    DrawPlots()
    elapsed_time = time.time() - start_time
    print(f"Elapsed Time: {elapsed_time:.4f}s")

def visit_vector_field(data_path):
    AddPlot('Vector', 'DISPL')
    p = VectorAttributes()
    p.glyphLocation=1
    p.nVectors=5000
    p.autoScale=0
    p.scale= 1 if data_path == "D:/Data/ParaView/Grid20_30_30T.ex2" else 10
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