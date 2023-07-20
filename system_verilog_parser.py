'''
 # @ Author: German Cano Quiveu, germancq
 # @ Create Time: 2021-04-06 12:06:45
 # @ Modified by: Your name
 # @ Modified time: 2021-04-06 12:07:20
 # @ Description:
 '''
from lark import Lark
import sys
import re
import system_verilog_classes

kwargs = dict(rel_to=__file__, start='module',maybe_placeholders=False)
sv_parser = Lark.open('system_verilog.lark',parser='earley', lexer='basic', **kwargs)


# def _read(fn, *args):
#     kwargs = {'encoding': 'iso-8859-1'}
#     with open(fn, *args, **kwargs) as f:
#         return f.read()


if __name__ == '__main__':
    with open(sys.argv[1],"r") as f:
        tree = sv_parser.parse(f.read()) 
        #print( tree.pretty() )
        ports = tree.find_data(data='port')
        for port in ports:
            #print(port.pretty())
            #print('stop')
            port_inst = system_verilog_classes.Port(port,tree)
            
            print(port_inst.direction)
            print(port_inst.name)
           
