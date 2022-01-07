# Author: Nahid Miah

import argparse
import os

def ParseArgs():
    parser = argparse.ArgumentParser(description='This script will fix the element row definition in the abaqus input deck exported by HyperMesh.')
    parser.add_argument("--path", help="Path to the input files to be fixed.", required=True, type=str, action='store')
    parser.add_argument("--infile", help="Text file with all input files to be fixed (entered row by row).", required=True, type=str, action='store')
    args = parser.parse_args()
    return args
    
if __name__ == '__main__':
    args = ParseArgs()

#########################################################################################################################################################
# main
#########################################################################################################################################################

input_path = args.path
input_list = args.infile
output_directory = os.mkdir(input_path+'/FIXED')

# create a list with all input from text file
with open(input_path+'/'+input_list,'r') as f:
    filename = [file.strip() for file in f]

for file in filename:
    # get all element lines
    element_list = []
    with open(input_path+'/'+file,'r') as f:
        bSet = False
        for line in f:
            line = line.strip()
            if line.startswith('*ELEMENT') or line.startswith('*element') or line.startswith('*Element'):
                bSet = True
            elif bSet == True and not line.startswith('*'):
                element_list.append(line.replace(' ','').split())
            elif bSet == True and line.startswith('** ') or line.startswith('**removed '):
                continue
            elif bSet == True and line.startswith('*'):
                bSet = False

    # concatenate the two separated element lines
    for i in range(len(element_list)):
        if i % 2 == 1:
            element_list[i-1] = [element_list[i-1][0] + element_list[i][0]]
    
    # update file
    with open(input_path+'/'+file,'r') as f, open(input_path+'/'+'FIXED'+'/'+file,'w') as f_out:
        bSet = False
        count = -1
        for line in f:
            line = line.strip()
            if line.startswith('*ELEMENT') or line.startswith('*element') or line.startswith('*Element'):
                bSet = True
                f_out.write(line+'\n')
            elif bSet == True and not line.startswith('*'):
                count += 1
                if count % 2 == 0:
                    f_out.write(element_list[count][0]+'\n')
            elif bSet == True and line.startswith('** ') or line.startswith('**removed '):
                f_out.write(line+'\n')
            elif bSet == True and line.startswith('*'):
                bSet = False
                f_out.write(line+'\n')
            else:
                f_out.write(line+'\n')
    print(f'Updated: FIXED/{file}')
print(f'\nDone.')