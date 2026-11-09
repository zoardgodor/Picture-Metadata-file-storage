# PMFS
## Picture-Metadata-file-storage
This is a README for my program's first version.
_Sorry for my bad english. I am used Google Translator a lot for this_

PMFS is a tool that allows for hiding files within the iTXt metadata of an image.
Currently, the program uses `duck.png` as the base image into which the file is embedded.
The selected file is converted into text (via `read_bytes()`), which is then encoded into Base64;
this Base64 string is subsequently stored as metadata. The file itself (in Base64 format) is
stored under the key "hiddenfile," while the filename is stored under the key "hiddenfilename."
The program currently operates via a command-line interface (CLI). Upon startup, it prompts the
user for the location of the file they wish to embed into the image's metadata. Once provided,
the program verifies the file's existence; if found, it converts the file into Base64 and saves
it—along with its original filename—into the metadata of `duck.png`. Finally, the program outputs
a modified version of the image, named `duck_001.png`. If that filename already exists, it increments
the number (e.g., `duck_002.png`, `duck_003.png`, and so on).

For decoding, when prompted at the beginning to specify the location of the file to be hidden,
simply press Enter without entering anything. You will then be able to select the image from whose
metadata you wish to extract the file. The program verifies that the specified file exists; if it
does, it checks for the presence of the two keys—one containing the file's content (encoded in Base64)
and the other containing the filename. If these keys are found, the program extracts the data,
decodes the Base64, and reconstructs the original file. For instance, if the original filename
was `test.txt`, the decoded file will be named `test_001.txt` (or `test_002.txt` if the former already
exists, and so on).

## Plans for the future:

- Saving to the metadata of your own .png file
- 001 is used when saving the decoded file if a
file with the original filename already exists; otherwise,
it would be saved using the original filename.
- GUI or a better CLI interface
- Executable .exe file created with PyInstaller