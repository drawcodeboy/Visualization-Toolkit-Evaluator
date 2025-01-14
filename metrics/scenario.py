from paraview.simple import *
from .methods import *

from collections import OrderedDict

def draw_data(data_path):
     # (1) File/Open에서 파일열기
    data, func1_time = load_data(data_path, show=True, interact=True)

    times = OrderedDict({
        'Load Data': func1_time,
        'Total Time': func1_time
    })

    return times

# Scenario 1
def draw_vector_field(data_path):
    # (1) File/Open에서 파일열기
    data, func1_time = load_data(data_path, order=1, show=False)

    # (2) Filters/Alphabetical/Cell data to Point Data
    filter, func2_time = cell_data_to_point_data(data, order=2, show=False)

    # (3) Filters/Alphabetical/Glyph
    glyph_modes = [
                    "Uniform Spatial Distribution (Bounds Based)", # Default
                    "All Points", # CONSIDER!
                   ]
                   
    filter, func3_time = glyph(data, order=3, show=True,
                               scale_factor=0.002,
                               glyph_type='Arrow',
                               glyph_mode=glyph_modes[0])

    # Sum all times
    total_time = func1_time + func2_time + func3_time

    each_time_li = [func1_time, func2_time, func3_time]

    return total_time, each_time_li

# Scenario 2
def draw_iso_contour(data_path):
    # (1) File/Open에서 파일열기
    data, func1_time = load_data(data_path, order=1, show=False)

    # (2) ISO Contour
    filter, func2_time = contour(data, order=2,
                                 contour_by="cellind",
                                 isosurfaces=[2404717, 4809434, 7214150, 9618867,
                                              12023583, 14428300, 16833016, 19237733])
    
    # Sum all times
    total_time = func1_time + func2_time

    each_time_li = [func1_time, func2_time]

    return total_time, each_time_li

# Scenario 3
def draw_stream_line(data_path, scenario_subtype=1):
    # Coloring, Line Parameters, Streamline Parameters

    # (1) File/Open에서 파일열기
    data, func1_time = load_data(data_path, order=1, show=False)

    # (2) Filters/Alphabetical/Cell data to Point Data
    filter, func2_time = cell_data_to_point_data(data, order=2, show=False)

    # (3) Filters/Alphabetical/Stream Tracer
    filter, func3_time = stream_tracer(data, order=3, show=True if scenario_subtype == 1 else False,
                                       vectors='vl',
                                       seed_type='Line') # "Line" or "Point Cloud"
    
    # Sum all times
    total_time = func1_time + func2_time + func3_time

    each_time_li = [func1_time, func2_time, func3_time]

    if scenario_subtype == 2:
        # (4) Filters/Alphabetical/Tube
        filter, func4_time = tube(filter, order=4, show=True)
        total_time += func4_time
        each_time_li.append(func4_time)
    elif scenario_subtype == 3:
        # (4) Filters/Alphabetical/Glyph
        filter, func4_time = glyph(filter, order=4, show=True)
        total_time += func4_time
        each_time_li.append(func4_time)
        
    return total_time, each_time_li

# Scenario 4
def draw_clip(data_path):
    # (1) File/Open에서 파일열기
    data, func1_time = load_data(data_path, order=1, show=False)

    # (2) Filters/Alphabetical/Clip
    filter, func2_time = clip(data, order=2, show=True,
                              clip_type='Plane') # 'Cylinder', 'Box'

    # Sum all times
    total_time = func1_time + func2_time

    each_time_li = [func1_time, func2_time]

    return total_time, each_time_li

# Scenario 5
def draw_slice(data_path):
    # (1) File/Open에서 파일열기
    data, func1_time = load_data(data_path, order=1, show=False)

    # (2) Filters/Alphabetical/Clip
    filter, func2_time = slice(data, order=2, show=True,
                               slice_type='Plane') # 'Cylinder', 'Box'

    # Sum all times
    total_time = func1_time + func2_time

    each_time_li = [func1_time, func2_time]

    return total_time, each_time_li

# Scenario 6
def perform_data_scenario(data_path, scenartio_subtype):
    # (1) File/Open에서 파일열기
    data, func1_time = load_data(data_path, order=1, show=False)

    if scenartio_subtype == 1:
        # (2) Filters/Alphabetical/Extract Selection
        filter, func2_time = extract_selection(data, order=2, show=True)
    
        # Sum all times
        total_time = func1_time + func2_time

        each_time_li = [func1_time, func2_time]
    elif scenartio_subtype == 2:
        # (2) Filters/Alphabetical/Extract Selection
        filter, func2_time = extract_selection(data, order=2, show=True)

        # (3) Filters/Alphabetical/Plot Selection Over Time
        filter, func3_time = plot_selection_over_time(data, order=3, show=True)
        # Sum all times
        total_time = func1_time + func2_time + func3_time

        each_time_li = [func1_time, func2_time, func3_time]
    elif scenartio_subtype == 3:
        # (2) Filters/Alphabetical/Plot Over Line
        filter, func2_time = plot_over_line(data, order=2, show=True)
    
        # Sum all times
        total_time = func1_time + func2_time

        each_time_li = [func1_time, func2_time]

    return total_time, each_time_li