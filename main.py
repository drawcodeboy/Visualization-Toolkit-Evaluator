# In Paraview powershell commands
# exec(open("C:/Users/User/Desktop/Interships/KDW/ETRI_04/evaluator/main.py").read())

from paraview.simple import *

import argparse
import os, sys

def get_args_parser():
    parser = argparse.ArgumentParser(add_help=False)

    parser.add_argument("--package-path", type=str, default="C:/Users/User/Desktop/Interships/KDW/ETRI_04/evaluator")
    parser.add_argument("--data-path", type=str, default="C:/Users/User/Desktop/Interships/KDW/ETRI_04/data/241003/foam/foam/run.foam")
    
    # Scenario
    # 0 = Draw Data
    # 1 = Draw Vector Field
    # 2 = Draw ISO Contour
    # 3 = Draw Stream Line
        # 3.1 = Stream Tracer
        # 3.2 = Stream Tracer -> Tube
        # 3.3 = Stream Tracer -> Glyph
    # 4 = Draw Clip
    # 5 = Draw Slice
    # 6 = Perform Data Scenario
        # 6.1 = Data Extraction
        # 6.2 = Data Time Plot (Data Extraction -> Plot Selection Over Time)
        # 6.3 = Data Time Plot (Plot Over Line)

    # N.M (N = --scenario, M = --scenario-subtype)

    parser.add_argument("--scenario", type=int, default=0)
    parser.add_argument("--scenario-subtype", type=int, default=2)
    
    # Scenario count
    # How many perform scenario
    parser.add_argument("--count", type=int, default=1)

    return parser

def check_and_append_sys_path(package_path):
    r'''
        cannot use __name__ property in Paraview, because we execute this evaluator
        in exec(open("C:/Users/User/Desktop/Interships/KDW/ETRI_04/evaluator/test.py").read())
        so, we don't know __name__ property.
    '''
    if package_path in sys.path:
        pass
    else:
        sys.path.append(package_path)

def del_sys_module():
    r'''
        If you execute once thie file at ParaView, the python shell still have sys.module.
        If you want to modify files and check it is modified, you shoud delete python shell's sys.module.
    '''
    del sys.modules['metrics.methods']
    del sys.modules['metrics.scenario']
    del sys.modules['metrics']

def main(args):
    try:
        del_sys_module()
    except:
        pass

    check_and_append_sys_path(args.package_path)
    '''
        Since the path to the module and package must be in sys.path in order to search for it, 
        I did not include it at the top of the file.
    '''
    
    from metrics import draw_data
    from metrics import draw_vector_field
    from metrics import draw_iso_contour
    from metrics import draw_stream_line
    from metrics import draw_clip
    from metrics import draw_slice
    from metrics import perform_data_scenario

    total_board = {'total time': [],
                   'element time': []}

    for order in range(args.count):
        print(f"==========[{order+1:02d}]==========")
    
        if args.scenario == 0:
            total_time, each_time_li = draw_data(args.data_path)
            print(f"Draw Data: {total_time:.4f}s")
        elif args.scenario == 1:
            total_time, each_time_li = draw_vector_field(args.data_path)
            print(f"Draw Vector Field: {total_time:.4f}s")
        elif args.scenario == 2:
            total_time, each_time_li = draw_iso_contour(args.data_path)
            print(f"Draw ISO Contour: {total_time:.4f}s")
        elif args.scenario == 3:
            total_time, each_time_li = draw_stream_line(args.data_path, args.scenario_subtype)
            print(f"Draw Stream Line type:({args.scenario_subtype:02d}): {total_time:.4f}s")
        elif args.scenario == 4:
            total_time, each_time_li = draw_clip(args.data_path)
            print(f"Draw Clip: {total_time:.4f}s")
        elif args.scenario == 5:
            total_time, each_time_li = draw_slice(args.data_path)
            print(f"Draw Slice: {total_time:.4f}s")
        elif args.scenario == 6:
            total_time, each_time_li = perform_data_scenario(args.data_path, args.scenario_subtype)
            print(f"Perform Data Scenario type:({args.scenario_subtype:02d}): {total_time:.4f}s")

        total_board['total time'].append(total_time)
        total_board['element time'].append(each_time_li)

    # Get All Mean
    print(f"========================")
    for i in range(0, len(total_board['element time'][0])):
        temp = 0
        for j in range(0, len(total_board['element time'])):
            temp += total_board['element time'][j][i]
        temp /= len(total_board['element time'])
        print(f">>[{i+1:02d} func Time(mean)]: {temp:.4f}s")
    print(f">>[Total Time(mean)]: {sum(total_board['total time'])/len(total_board['total time']):.4f}s")
    
    del_sys_module()

parser = argparse.ArgumentParser(parents=[get_args_parser()])
    
args = parser.parse_args()
main(args)