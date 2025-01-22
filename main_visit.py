# visit -cli -s main_visit.py

from metrics2 import *

from visit import *

import json, os

def main(cfg):
    OpenDatabase(f"localhost:{cfg['data_path']}")

    if cfg['scenario'] == 'Load Data':
        visit_load_data()
    elif cfg['scenario'] == 'Vector-Field':
        visit_vector_field(cfg['data_path'])
    else:
        pass

    if not os.path.exists('./screenshots_visit'):
        os.mkdir('./screenshots_visit')
    
    if cfg['vis'] == 'Screenshot':
        s = SaveWindowAttributes()
        # D:/Data/ParaView/Grid200_300_300T.ex2
        s.fileName = f"./screenshots_visit/{cfg['data_path'].split('/')[-1]}-{cfg['scenario']}"
        s.format = s.PNG
        s.progressive = 1
        s.fileName = f"./screenshots_visit/{cfg['data_path'].split('/')[-1]}-{cfg['scenario']}"
        SetSaveWindowAttributes(s)
        name = SaveWindow()
        print(f"file name = {name}")

if __name__ == '__main__':
    with open('config.json') as f:
        cfg = json.load(f)
    cfg['data_path'] = cfg['data_path'].replace('\\', '/')
    main(cfg)