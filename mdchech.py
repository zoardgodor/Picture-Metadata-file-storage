from pathlib import Path
from PIL import Image
from PIL.PngImagePlugin import PngInfo
image=Image.open("duck_001.png")
metadata=image.info
print(metadata)