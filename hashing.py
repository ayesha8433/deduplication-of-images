import hashlib
from imageio import imread
import matplotlib.pyplot as plt
import numpy as np

from hashlib import md5

def file_hash(filepath):
    with open(filepath,'rb') as f:
        return md5(f.read()).hexdigest()

import os
os.getcwd()

os.chdir(r"C:\Users\AYESHA\Desktop\img")
os.getcwd()
files_list=os.listdir()
print(len(files_list))

import hashlib,os
duplicates=[]
hash_keys=dict()
for index, filename in enumerate(os.listdir('.')):
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash=hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys:
            hash_keys[filehash]= index
        else:
            duplicates.append((index,hash_keys[filehash]))
duplicates

for file_indexes in duplicates[:6]:
    try:
        plt.subplot(121),plt.imshow(imread(files_list[file_indexes[1]]))
        plt.title(file_indexes[1]), plt.xticks([]), plt.yticks([])

        plt.subplot(122),plt.imshow(imread(files_list[file_indexes[0]]))
        plt.title(str(file_indexes[0]) + 'duplicate'), plt.xticks([]), plt.yticks([])
        plt.show()

    except OSError as e:
        continue

    for index in duplicates:
        os.remove(files_list[index[0]])
    




