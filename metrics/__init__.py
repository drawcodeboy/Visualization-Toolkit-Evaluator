from .start import start

def load_scenario(data_path:str,
                  scenario:int=0,
                  scenario_subtype:int=0):
    
    start(data_path)
    
    '''
    if scenario == 0:
        return draw_data(data_path)
    elif scenario == 1:
        return draw_vector_field(data_path)
    elif scenario == 2:
        return draw_iso_contour(data_path)
    elif scenario == 3:
        return draw_stream_line(data_path, scenario_subtype)
    elif scenario == 4:
        return draw_clip(data_path)
    elif scenario == 5:
        return draw_slice(data_path)
    elif scenario == 6:
        return perform_data_scenario(data_path, scenario_subtype)
    else:
        raise NotImplementedError(f"We don't support scenario {scenario} yet.")
    '''
    times = {}
    return times