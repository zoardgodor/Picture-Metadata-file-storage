# PMFS
## Picture-Metadata-file-storage
This is a README for my program's first version.
_Sorry for my poor english._

PMFS is a tool that allows hiding files within the iTXt metadata of an image.
Users can select any PNG image as a carrier file and choose which file they want to hide.

## Normal version (PMFS.exe or PMFS.py with tkinter):

There are 3 functions on the main window:

## Hide:
The user choses a PNG file. The program checks if the selected PNG file is
valid PNG file. After that, the program asks for any file. This file is going to be
hidden. The program checks if the file is bigger than 25 MiB.
- Maximum original file size: 25 MiB (actual compatibility may depend on the software handling the PNG).
The program reads the bytes of the file, and codes that into Base64. The Base64 data is going to be written
into the PNG as a iTXt metadata.

## Extract
The user choses a PNG file. The program checks if the selected PNG file is
valid PNG file. After that, the program checks if there any hidden files in the
PNG. If there is, the program decodes the Base64, and makes it into a new file.
The original and the extracted files are the same.

## Remove hidden file
The user choses a PNG file. The program checks if the selected PNG file is
valid PNG file. After that, the program checks if there is any PMFT
file-s in the PNG. If there is, the program overwrites the metadata.
_There is a chance the program removes some other metadatas._ The program makes a new PNG
file without the metadata. The original file remains untouched.

## Requirements

- Python 3
- Pillow
- Pyinstaller for make a .exe file

If you want to recreate the .exe file, just install Pyinstaller, and run the command from the pyinstaller.txt file.



## Old CLI version (PMFS_old_cli.exe and PMFS_old_cli.py):

There are 3 functions:

_(This version of the program is the old version. It is not under active development.)_

## Hide:
The user choses a PNG file. The program checks if the selected PNG file is
valid PNG file. After that, the program asks for the path to a file. This file is going to be
hidden. The program checks if the file is bigger than 25 MiB.
- Maximum original file size: 25 MiB (actual compatibility may depend on the software handling the PNG).
The program reads the bytes of the file, and codes that into Base64. The Base64 data is going to be written
into the PNG as a iTXt metadata.

## Extract
The user choses a PNG file. The program checks if the selected PNG file is
valid PNG file. After that, the program checks if there any hidden files in the
PNG. If there is, the program decodes the Base64, and makes it into a new file.
The original and the extracted files are the same.

## Remove hidden file
The user choses a PNG file. The program checks if the selected PNG file is
valid PNG file. After that, the program checks if there is any PMFT
file-s in the PNG. If there is, the program overwrites the metadata.
There is a chance the program removes some metadata and makes a new PNG
file without the metadata. The original file remains untouched.