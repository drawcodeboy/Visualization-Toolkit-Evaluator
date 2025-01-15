from .start import start
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

    render_view.Update()

    return times