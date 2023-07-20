'''
 # @ Author: German Cano Quiveu, germancq
 # @ Create Time: 2023-07-20 12:54:03
 # @ Modified by: German Cano Quiveu, germancq
 # @ Modified time: 2023-07-20 12:54:16
 # @ Description:
 '''

class Port:
    def __init__(self,port,tree):
        self.direction = port.children[0].data
        name_tree = list(port.find_data(data='name'))
        self.name = name_tree[0].children[0]
        



        self.lower_bound_size = 0
        self.higher_bound_size = 0
