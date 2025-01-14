from paraview.simple import *

import os, sys
import json

from metrics import *

def main(cfg):
    total_times = {}

    # Perform Scenario
    for count in range(cfg['count']):
        times = load_scenario(cfg['data_path'],
                              cfg['scenario'],
                              cfg['scenario_subtype'])
        
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

if __name__ == '__main__':
    with open('config.json') as f:
        cfg = json.load(f)
    main(cfg)