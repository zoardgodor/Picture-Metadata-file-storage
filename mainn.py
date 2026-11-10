from pathlib import Path
from PIL import Image
from PIL.PngImagePlugin import PngInfo
import base64
MAXFILESIZE = 25 * 1024 * 1024
def hide_file():
    duck=input("Enter the path of the image to use as a carrier: ").strip()
    if duck:
            duck=Path(duck)
            if not duck.is_file():
                print("This picture does not exist.")
                return
            else:
                if not duck.suffix.lower()==".png":
                    print("This picture is not a PNG file.")
                    return
                try:
                    asdfghjk=Image.open(duck)
                except Exception:
                    print("Unable to open this image.")
                    return
                ducky=Image.open(duck)
                if not ducky.format=="PNG":
                    print("This picture is not a valid PNG file.")
                    return
                if "hiddenfile" in ducky.info or "hiddenfilename" in ducky.info:
                        print("This picture already has a hidden file.")
                        return
    else:
        print("No image path provided.")
        return            
    filee=input("Path to file to hide: ").strip()
    if filee:
        filecheck=Path(filee)
        if not filecheck.is_file():
            print("File does not exist.")
            return
        if filecheck.stat().st_size>MAXFILESIZE:
            print("File is too large to hide. Maximum size is 25MB.")
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
            output = duck.parent/f"{duck.stem}_pmfs_{counter:03}.png"
            if not output.exists():
                break
            counter+=1
        image.save(output,"PNG",pnginfo=metadata)
        print(f"File hidden in {output}.")
        return
def extract_file():
            imagepath=input("Enter the path of the image to extract from: ").strip()
            if not imagepath:
                print("No image path provided.")
                return
            imagepath=Path(imagepath)
            if not imagepath.is_file():
                print("Image does not exist.")
                return
            if not imagepath.suffix.lower()==".png":
                    print("This picture is not a PNG file.")
                    return
            image = Image.open(imagepath)
            metadata=image.info
            if "hiddenfile" in metadata and "hiddenfilename" in metadata:
                encoded_file=metadata["hiddenfile"]
                filename=metadata["hiddenfilename"]
                filebytes=base64.b64decode(encoded_file, validate=True)
                output=imagepath.parent/ filename
                if output.exists():
                    print(f"File {output} already exists. Extracting file with a different name.")
                    counter=1
                    while output.exists():
                        original=output
                        output=original.with_name(f"{original.stem}_{counter:03}{original.suffix}")
                        counter+=1
                    output.write_bytes(filebytes)
                    print(f"Hidden file extracted to {output}.")
                    return
                else:
                    output.write_bytes(filebytes)
                    print(f"Hidden file extracted to {output}.")
                    return
            else:
                print("No hidden file found in the image.")    
                return
def deletefile():
    print("This will remove the hidden file from the image, but it will not delete the original file. It creates a new image without the hidden file. The original image will remain unchanged.")
    imagepath=input("Enter the path of the image to delete hidden file from: ").strip()
    if not imagepath:
        print("No image path provided.")
        return
    imagepath=Path(imagepath)
    if not imagepath.is_file():
        print("Image does not exist.")
        return
    if not imagepath.suffix.lower()==".png":
            print("This picture is not a PNG file.")
            return
    image = Image.open(imagepath)
    metadata=image.info
    if "hiddenfile" in metadata and "hiddenfilename" in metadata:
        newmetadata = PngInfo()
        counter=1
        while True:
            remoutput=Path(imagepath).parent/f"{imagepath.stem}_nohidden_{counter:03}.png"
            if not remoutput.exists():
                break
            counter+=1
        image.save(remoutput, "PNG", pnginfo=newmetadata)
        print(f"Hidden file removed. The new image is saved as {remoutput}.")
    else:
        print("No hidden file found in the image.")

def main():
    print("----PMFT----")
    print("1. Hide a file in an image")
    print("2. Extract a file from an image")
    print("3. Delete a file from an image")
    print("q - Exit")
    choice=input("Enter your choice (1, 2, 3, or q): ").strip()
    if choice=="1":
        hide_file()
    elif choice=="2":
        extract_file()
    elif choice=="3":
        deletefile()
    elif choice.lower()=="q":
        print("Exiting...")
        return

if __name__ == "__main__":
    main()