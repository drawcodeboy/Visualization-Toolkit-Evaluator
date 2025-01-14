# ParaView Evaluator using PvPython
* <b>Latest: v1.1.0</b>
    * <a href="docs/VERSION_1.1.0.md">v1.1.0 Documentation</a>
    * <a href="docs/VERSION_1.0.0.md">v1.0.0 Documentation</a>
## functions
```
# 데이터 가져오기, 시간이 얼마 들지 않음
OpenFOAMReader(registrationName="데이터 이름(Pipeline Browser에서)",
               FileName="데이터 파일 위치 경로")

# get animation scene, 뭔지 파악 안 됨
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps, 뭔지 파악 안 됨
animationScene1.UpdateAnimationUsingDataTimeSteps() 

# Layout#1 하나 만듬, 창 띄우는 거라 보면 됨
renderView1 = GetActiveViewOrCreate('RenderView')

# 여기가 실제로 화면에 띄우는 부분 (렌더링하는 부분)
runfoamDisplay = Show(data, renderView1, 'UnstructuredGridRepresentation')

# 화면 표현을 어떻게 하겠다는 의미인 듯
runfoamDisplay.Representation = 'Surface'

# 파악 안 됨
renderView1.ResetCamera(False, 0.9)

# 여기서 화면 표현 조정을 했던 부분이 적용되는 듯
runfoamDisplay.SetScalarBarVisibility(renderView1, True) # 여기서 적용 된다.

# Render View의 정보가 여기서 업데이트되는 듯 하다.
renderView1.Update()

## 파악 안 됨
# get color transfer function/color map for 'p'
pLUT = GetColorTransferFunction('p')

# get opacity transfer function/opacity map for 'p'
pPWF = GetOpacityTransferFunction('p')

# get 2D transfer function for 'p'
pTF2D = GetTransferFunction2D('p')


# create a new 'Glyph'
glyph1 = Glyph(registrationName='Glyph1', Input=runfoam,
    GlyphType='Arrow')

# show data in view
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'

# show color bar/color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# hide data in view
Hide(runfoam, renderView1)

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

# 화면 띄우는 거
Interact()
```