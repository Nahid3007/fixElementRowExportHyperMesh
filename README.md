# Python tool for fixing HyperMesh's *ELEMENT line break                                                                                                    

This script will fix the element row definition in the abaqus input deck exported by HyperMesh (only if needed; e.g. when input will be postprocess with other scripts). 

This problem occurs for example if second order tetraherda elements are used. The last two nodes of the Tet10 element are represented in a new row.
                                                                                             
Example exported by HyperMesh:                                                                                         
*ELEMENT,TYPE=C3D10I,ELSET=eall                                                                                
        1,       133,        38,         2,         1,      2438,      2444,      2592,      2439,             
      743,       739                                                                                           
                                                                                                               
Fixed by the script:
*ELEMENT,TYPE=C3D10I,ELSET=eall                                                                                
1,133,38,2,1,2438,2444,2592,2439,743,739                                                                       


## How to use fixElementRowExportHyperMesh.py:

Usage: fixElementRowExportHyperMesh.py [-h] --path PATH --infile INFILE

Execute: python fixElementRowExportHyperMesh.py --path [Path to the input file directory] --infile [Text file which contains all input files to be fixed in a row]

The fixed input files will be copied into the new created /FIXED directory.

## Optional: createFile.py:

If for example all files of a directory must fixed, this script will write all input file in a text file automatically.

Usage: createFile.py  [-h] --path PATH --outfile OUTFILE

Execute: python .py --path [Path to the input file directory] --outfile [Name of the output text file]
