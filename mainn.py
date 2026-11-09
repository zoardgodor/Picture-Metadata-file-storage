from pathlib import Path
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import base64
def main():
    duck=Path(__file__).parent/"duck.png"
    if not duck.is_file():
        print("Duck image does not exist.")
        return
    file=input("File path to hide (leave empty and press enter to extract): ").strip()
    if file:
        filecheck=Path(file)
        if not filecheck.is_file():
            print("File does not exist.")
            return
        filebytes=filecheck.read_bytes()
        filename=filecheck.name
        encoded_file=base64.b64encode(filebytes).decode("ascii")
        metadata=PngInfo()
        metadata.add_itxt("hiddenfile",encoded_file)
        metadata.add_itxt("hiddenfilename",filename)
        image=Image.open(duck)
        counter=1
        while True:
            output=duck.parent/f"duck_{counter:03}.png"
            if not output.exists():
                break
            counter+=1
        image.save(output,"PNG",pnginfo=metadata)
        print(f"File hidden in {output}.")
    else:
        image=input("Enter the path of the image to extract from: ").strip()
        if not image:
            print("No image path provided.")
            return
        print("Extracting hidden file...")
        imagecheck=Path(image)
        if not imagecheck.is_file():
            print("Image does not exist.")
            return
        image=Image.open(imagecheck)
        metadata=image.info
        if "hiddenfile" in metadata and "hiddenfilename" in metadata:
            encoded_file=metadata["hiddenfile"]
            filename=metadata["hiddenfilename"]
            filebytes=base64.b64decode(encoded_file, validate=True)
            output=Path(filename)
            counter=1
            while output.exists():
                original=Path(filename)
                output=original.with_name(f"{original.stem}_{counter:03}{original.suffix}")
                counter+=1
            output.write_bytes(filebytes)
            print(f"Hidden file extracted to {output}.")
        else:
            print("No hidden file found in the image.")
if __name__ == "__main__":
    main()