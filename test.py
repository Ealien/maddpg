import os
import pickle

dataList = [[1, 1, 'yes'],
            [1, 1, 'yes'],
            [1, 0, 'no'],
            [0, 1, 'no'],
            [0, 1, 'no']]

dirpath = "/home/guotao/hello"
filename = "/home/guotao/hello/pickle.txt"
if os.path.exists(dirpath):
    print("The dir is exist.")
else:
    os.mkdir(dirpath)
with open(filename, 'wb') as f:
    pickle.dump(dataList, f)
