
import temp4
import hashing
import os

path = r"C:\Users\AYESHA\Desktop\img"
dirs = os.listdir(path)

temp4.match(dirs=dirs, path=path)
hashing.perform_hashing(path)