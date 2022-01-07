import argparse
import os

def ParseArgs():
    parser = argparse.ArgumentParser(description='This script creates a text file for all files listed in the input file directory.')
    parser.add_argument("--path", help="Path where the text file should be created.", required=True, type=str, action='store')
    parser.add_argument("--outfile", help="Name of the output text file.", required=True, type=str, action='store')
    args = parser.parse_args()
    return args
    
if __name__ == '__main__':
    args = ParseArgs()

#########################################################################################################################################################
# main
#########################################################################################################################################################

input_path = args.path
output_file = args.outfile

files_in_dir = os.listdir(input_path)

with open(input_path+'/'+output_file,'w') as f_out:
    for file in files_in_dir:
        file = file.strip()
        if not file.endswith('inp'):
            continue
        f_out.write(f'{file}\n')
print(f'\nDone.')