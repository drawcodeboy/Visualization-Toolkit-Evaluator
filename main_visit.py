# visit -cli -s main_visit.py

from metrics2 import *

import visit

import json

def main(cfg):
    visit.OpenDatabase(f"localhost:{cfg['data_path']}")

    if cfg['scenario'] == 'Load Data':
        visit_load_data()
    elif cfg['scenario'] == 'Vector-Field':
        visit_vector_field(cfg['data_path'])
    else:
        pass

if __name__ == '__main__':
    with open('config.json') as f:
        cfg = json.load(f)
    cfg['data_path'] = cfg['data_path'].replace('\\', '/')
    main(cfg)