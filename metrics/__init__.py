from .start import *
from .methods import *

from typing import Dict

def load_scenario(data_path:str,
                  scenario:str="Vector-Field",
                  scenario_config:Dict={}):
    input, render_view, times = start(data_path)

    if scenario == "Load Data":
        pass
    elif scenario == 'Vector-Field':
        times = draw_glyph(input, render_view, scenario_config)
    elif scenario == 'ISO Contour':
        times = draw_iso_contour(input, render_view, scenario_config)
    elif scenario == 'Stream Line':
        times = draw_stream_line(input, render_view, scenario_config)
    elif scenario == 'Clip':
        times = draw_clip(input, render_view, scenario_config)
    elif scenario == 'Slice':
        times = draw_slice(input, render_view, scenario_config)

    if scenario in ['Vector-Field']:
        render_view.ResetActiveCameraToPositiveZ()
    elif scenario in ['Stream Line']:
        render_view.ResetActiveCameraToPositiveX()
    else:
        render_view.ApplyIsometricView()
    
    render_view.ResetCamera(False, 0.9)

    return times