import numpy as np 
import pandas as pd 
from sys import argv
input_file  =  argv[1]
output_file = argv[2]

class Convert(object):
    def  __init__(self):
        pass

    def readTable(self,file):
        self.table = pd.read_table(file,sep = '\t',header = None)

    def FillParent(self,child,parent):
        for i in range(1,len(child)):
            if pd.isna(child[i-1]):
                pass
            else :
                parent[i-1] = parent[i-2]
        return parent

    def Dojob(self):
        for i in range(0,5):
            id  =  6-i
            print(f"convert {id-1} as child and {id - 2} as parent")
            child = self.table[id-1]
            parent = self.table[id-2]
            print(f"Doing Job!")
            parent = self.FillParent(child,parent)
            self.table[id-2] = parent

convert =  Convert()
convert.readTable(input_file)
print(">>>>  table read <<<<")
convert.Dojob()
print(">>>>  Done <<<<")
print(convert.table)
convert.table.to_csv(output_file)