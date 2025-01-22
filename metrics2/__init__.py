from .visit_expr import *

def load_scenario(cfg):
    if cfg['scenario'] == 'Load Data':
        visit_load_data()
    elif cfg['scenario'] == 'Vector-Field':
        visit_vector_field(cfg['data_path'])
    elif cfg['scenario'] == 'ISO Contour':
        visit_iso_contour()
    elif cfg['scenario'] == 'Clip':
        visit_clip(cfg['data_path'])
    elif cfg['scenario'] == 'Slice':
        visit_slice(cfg['data_path'])