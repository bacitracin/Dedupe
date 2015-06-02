# -*- coding: utf-8 -*-
"""
Created on Mon May 18 16:01:30 2015
@author: Tracy

"""

import csv
names_set = set()

# Builds names_set. Use the CSV 'babynames.csv' 
def build_the_names_set(filename):
    with open(filename, 'r') as fd:
        for row in fd:
            names_set.add(row)
        fd.close()
        return names_set

def write_names():    
    with open('SNcleaned_file.csv', 'w') as fd:
        writer = csv.writer(fd)
        for [item] in names_set:        
            writer.writerows(item)
        fd.close()

 