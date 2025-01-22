from paraview.simple import *

import os, sys
import json

from metrics import *

def main(cfg):
    total_times = {}

    # Perform Scenario
    for count in range(-1, cfg['count']):
        times = load_scenario(cfg['data_path'],
                              cfg['scenario'],
                              cfg[cfg['scenario']])
        
        if count == -1:
            input = read_data(cfg['data_path'])
            print_data_information(input)
            continue
        
        print(f"==============[{count+1:02d}]==============")
        for key, value in times.items():
            print(f"{key}: {value:.4f}s")
            if count == 0:
                total_times[key] = [value]
            else:
                total_times[key].append(value)
        
    # Result (Mean Values)
    print(f"================================")
    for key, value in total_times.items():
        print(f"{key}(Mean): {sum(value)/len(value):.4f}s")

    # Set Window Size
    layout1 = GetLayout()
    layout1.SetSize(1816, 869)

    if cfg['vis'] == 'Interact':
        # Show Window
        Interact()
    elif cfg['vis'] == 'Screenshot':
        SaveScreenshot(f"./screenshots_paraview/{cfg['data_path'].split('/')[-1]}-{cfg['scenario']}.png")

if __name__ == '__main__':
    with open('config.json') as f:
        cfg = json.load(f)
    cfg['data_path'] = cfg['data_path'].replace('\\', '/')
    main(cfg)