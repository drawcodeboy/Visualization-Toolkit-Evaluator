import visit
import time
visit.OpenDatabase("localhost:D:/Data/ParaView/Grid20_30_30T.ex2")
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