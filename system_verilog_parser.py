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

kwargs = dict(rel_to=__file__, start='module')
sv_parser = Lark.open('system_verilog.lark',parser='earley', lexer='standard', **kwargs)


def _read(fn, *args):
    kwargs = {'encoding': 'iso-8859-1'}
    with open(fn, *args, **kwargs) as f:
        return f.read()

def _readHeaderModule(fn, *args):
    kwargs = {'encoding': 'iso-8859-1'}
    r = ""
    start = 0
    pattern_beginModule = r'^module'
    pattern_commentedLine = r'^\/\/'
    pattern_endDeclarationModule = r'[\(\)A-Za-z0-9];'
    with open(fn, *args, **kwargs) as f:
        lines = f.readlines()
        for line in lines:

            if(re.match(pattern_beginModule,line) != None):
                start = 1

            commented_line = re.match(pattern_commentedLine,line)
            if(start == 1 and commented_line == None):
                r += line 

            if(commented_line == None and re.match(pattern_endDeclarationModule,line)!= None):
                #print (r)
                return r
    return r


if __name__ == '__main__':
    with open(sys.argv[1],"r") as f:
        tree = sv_parser.parse(f.read()) 
        print( tree.pretty() )