import os
import shutil

path = '/Users/samiulislamsami/Documents/Nand2Tetris/hdl files/nand2tetris/projects/1'
dest = '/Users/samiulislamsami/Prog/github_projects/nand2tetris_work'
files = []
for i in os.listdir(path=path):
    files.append(i)


hdl = []
for i in files:
    if i.endswith('.hdl'):
        hdl.append(i)


select = []
for i in hdl:
    if i.startswith('Xor.hdl') or i.startswith('Not.hdl') or i.startswith('And.hdl') or i.startswith('Or.hdl') or i.startswith('Xor.hdl') or i.startswith('Mux.hdl') or i.startswith('DMux.hdl'):
        select.append(i)


for i in select:
    shutil.copy(path+'/'+i, dest)