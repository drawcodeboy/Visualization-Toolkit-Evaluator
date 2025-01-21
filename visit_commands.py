# visit -cli
# Engine Assignment https://visit-sphinx-github-user-manual.readthedocs.io/en/v3.1.1/gui_manual/ComputeEngines/index.html?highlight=engine
# Options > Host Profiles

## ============[1. Load Data]============ ##
# Grid20_30_30T.ex2
import time
visit.OpenDatabase("localhost:D:/Data/ParaView/Grid20_30_30T.ex2")
AddPlot('Mesh', 'Mesh')
start_time = time.time()
DrawPlots()
elapsed_time = time.time() - start_time
s = SaveWindowAttributes()
s.fileName = "test"
s.format = s.JPEG
s.progressive = 1
print(f"Elapsed Time: {elapsed_time:.4f}s")

# Grid200_300_300T.ex2
import time
visit.OpenDatabase("localhost:D:/Data/ParaView/Grid200_300_300T.ex2")
AddPlot('Mesh', 'Mesh')
start_time = time.time()
DrawPlots()
elapsed_time = time.time() - start_time
print(f"Elapsed Time: {elapsed_time:.4f}s")

# Grid300_600_600T.ex2
import time
visit.OpenDatabase("localhost:D:/Data/ParaView/Grid200_300_300T.ex2")
AddPlot('Mesh', 'Mesh')
start_time = time.time()
DrawPlots()
elapsed_time = time.time() - start_time
print(f"Elapsed Time: {elapsed_time:.4f}s")

## ============[2. Vector-Field]============ ##
# Grid20_30_30T.ex2
import time
visit.OpenDatabase("localhost:D:/Data/ParaView/Grid20_30_30T.ex2")
AddPlot('Vector', 'DISPL')
p = VectorAttributes()
p.nVectors=5000
p.scale=1
SetPlotOptions(p)
start_time = time.time()
DrawPlots()
elapsed_time = time.time() - start_time
print(f"Elapsed Time: {elapsed_time:.4f}s")

# Grid200_300_300T.ex2 
import time
visit.OpenDatabase("localhost:D:/Data/ParaView/Grid200_300_300T.ex2")
AddPlot('Vector', 'DISPL')
p = VectorAttributes()
p.glyphLocation=1
p.nVectors=5000
p.autoScale=0
p.scale=10
p.lineStem=0
SetPlotOptions(p)
start_time = time.time()
DrawPlots()
elapsed_time = time.time() - start_time
print(f"Elapsed Time: {elapsed_time:.4f}s")

# Grid300_600_600T.ex2
import time
visit.OpenDatabase("localhost:D:/Data/ParaView/Grid200_300_300T.ex2")
AddPlot('Vector', 'DISPL')
p = VectorAttributes()
p.glyphLocation=1
p.nVectors=5000
p.autoScale=0
p.scale=10
p.lineStem=0
SetPlotOptions(p)
start_time = time.time()
DrawPlots()
elapsed_time = time.time() - start_time
print(f"Elapsed Time: {elapsed_time:.4f}s")