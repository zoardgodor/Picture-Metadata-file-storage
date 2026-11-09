from pathlib import Path
from PIL import Image
from PIL.PngImagePlugin import PngInfo
image=Image.open("duck.png")
metadata=PngInfo()
metadata.add_itxt("Duck","Hello, World!")
image.save("duck_with_metadata.png","PNG",pnginfo=metadata)
