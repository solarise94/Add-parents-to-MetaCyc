import pandas as pd 
import numpy as np 
from sys import argv

input_file = argv[1]
input_dict = argv[2]
output_result = argv[3]
# import files

Table = pd.read_table(input_file,sep="\t")
Dict = pd.read_csv(input_dict,sep=",",header = None, index_col=None)
# read files 
class Search(object):
    def __init__(self,dictionary,Table):
        self.dict = dictionary
        self.table = Table
        self.result = []
        self.debugcount = 0

    def Search(self,child,dictTable,i):
        try :
            #print(dictTable)
            dictlist = dictTable[5-i].values.tolist()
            #print(f">>>>> try class {5-i+1}")
            id = dictlist.index(child)
        except ValueError:
            if i == 5 :
                self.result.append(["Can't match"])
            else:
                pass
            return True
        else:
            #pd.concat(self.result,self.dict[id+1])
            self.result.append(self.dict[id:id+1].values.tolist())
            self.debugcount = self.debugcount +1
            #print(f">>>> match {self.debugcount} times")
            return False

    def RunEgine(self):
        ChildList = self.table['description']
        for Keyword in ChildList:
            self.doSearch(Keyword)
    
    def doSearch(self,Keyword):
        for i in range(0,6):
            if self.Search(Keyword,self.dict,i) and i < 5:
                continue
            #elif self.Search(Keyword,self.dict,i) and i == 5:
            #    print(">>> can't match")
                #print(">>>> try to break")
                #thing = True
            else:
                break
            #if thing :
                #print(">>>> break failed")

search = Search(Dict,Table)
search.RunEgine()
df = pd.DataFrame(search.result) 
print(df)
df.to_csv(output_result)