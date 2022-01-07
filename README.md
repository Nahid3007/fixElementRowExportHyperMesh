# Python tool for fixing HyperMesh's *ELEMENT line break                                                                                                    

This script will fix the element row definition in the abaqus input deck exported by HyperMesh (only if needed).
                                                                                             
Example exported by HyperMesh:                                                                                         
*ELEMENT,TYPE=C3D10I,ELSET=eall                                                                                
        1,       133,        38,         2,         1,      2438,      2444,      2592,      2439,             
      743,       739                                                                                           
                                                                                                               
Fixed by the script:
*ELEMENT,TYPE=C3D10I,ELSET=eall                                                                                
1,133,38,2,1,2438,2444,2592,2439,743,739                                                                       







usage: fixElementRowExportHyperMesh.py [-h] --path PATH --infile INFILE