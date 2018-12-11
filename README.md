# Python Script For Representing CAN or LIN Logs In Color    

Colorflog displays a bus log in the "Time, ID, Data" .csv format with 
chromatic assignment based on ID. Higher IDs occupy the Red end of the color 
spectrum, while lower IDs are blue or black. Visually encoding the data 
allows for more rapid pattern identification in the reverse engineering process. 

## Creating an Example Colorflog 

Runing 
```
python colorflog.py "lin_example.csv" 
```
produces an output, lin_example.html, with color. 

Note that some of the tools from the lin_ret repository may be useful for pre-processing 
LIN logs, depending on the input format, to end up with suitable input files for colorflog. 
