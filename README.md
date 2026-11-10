# PMFS
## Picture-Metadata-file-storage
This is a README for my program's first version.
_Sorry for my poor english._

PMFS is a tool that allows for hiding files within the iTXt metadata of an image.
Users can select any PNG image as a carrier file and choose which file they want to hide.

There are 3 tools:

## Hide:
The user choose a PNG file. The program checks the selected PNG file is
a real, working PNG file. After that, the program asks for a path to a file. This file is going to be
hided. The program checks the file is bigger than 25 MiB.
- Maximum original file size: 25 MiB (actual compatibility may depend on the software handling the PNG).
The program reads the bytes of the file, and code that into Base64. The Base64 data is going to
write into the PNG as a iTXt metadata.

## Extract
The user choose a PNG file. The program checks is the selected PNG file is
a real, working PNG file. After that, the program checks is there any hided PMFT file in the
PNG. If there is, the program is reading out the Base64, and decoding that, and makes the new file.
The original and the extracted files are the same.

## Remove hidden file
The user choose a PNG file. The program checks is the selected PNG file is
a real, working PNG file. After that, the program checks is there any PMFT
file-s are in the PNG. If there is, the program overwrites the metadatas.
There is a chance the program removes some other metadatas. And makes a new PNG
file without the metadatas. The original file remains untouched.

## Requirements

- Python 3
- Pillow
- Pyinstaller for make a .exe file

If you want to recreate the .exe file, just install Pyinstaller, and run the command from the pyinstaller.txt file.